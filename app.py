from flask import Flask, render_template_string, request, redirect, url_for, session, flash, send_from_directory, jsonify, Response, abort
import sqlite3, os, uuid, re, json, logging, base64
from urllib.parse import urlparse, quote_plus
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)
application = app  # WSGI alias for deployment platforms
app.secret_key = os.environ.get("SECRET_KEY", "")
if not app.secret_key:
    # A stable secret is mandatory in production; local development gets a warning-safe generated fallback.
    app.secret_key = os.urandom(32).hex()
    if os.environ.get("VERCEL"):
        raise RuntimeError("Set SECRET_KEY in Vercel Environment Variables before deploying.")
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax", SESSION_COOKIE_SECURE=bool(os.environ.get("VERCEL")))
logging.basicConfig(level=logging.INFO)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = (os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL") or os.environ.get("POSTGRES_PRISMA_URL") or "").strip()
DATABASE = os.path.join("/tmp", "campuscare.db") if os.environ.get("VERCEL") else os.path.join(BASE_DIR, "campuscare.db")
UPLOAD_FOLDER = os.path.join("/tmp", "campuscare_uploads") if os.environ.get("VERCEL") else os.path.join(BASE_DIR, "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["MAX_CONTENT_LENGTH"] = 6 * 1024 * 1024  # 6 MB total request limit

CATEGORIES = ["Hostel","Classroom","Laboratory","Washroom","Electricity","Water","Wi-Fi","Food/Mess","Cleaning","Security","Other"]
PRIORITIES = ["Low","Medium","High","Emergency"]
STATUSES = ["Submitted","Assigned","In Progress","Resolved","Closed"]
ALLOWED_EXTENSIONS = {"png","jpg","jpeg","gif","webp"}

def valid_campus_email(email):
    return bool(re.fullmatch(r"[^@\s]+@campus\.360", email.strip().lower()))

DEMO_WORKERS = [
    ("Ravi Kumar", "Electrical", "9876543210"),
    ("Suresh Reddy", "Plumbing", "9876543211"),
    ("Arjun Kumar", "Cleaning", "9876543212"),
    ("Naveen Kumar", "Maintenance", "9876543213"),
    ("Mahesh", "Wi-Fi & Network", "9876543214"),
    ("Prakash", "Security", "9876543215"),
]

CONTACTS = [
    ("Campus Admin", "Administration", "9876500001"),
    ("Hostel Warden", "Hostel Office", "9876500002"),
    ("Maintenance Desk", "Maintenance", "9876500003"),
    ("Security Desk", "Security", "9876500004"),
    ("Emergency Help", "Emergency", "112"),
]

class PostgresConnection:
    """Small SQLite-compatible adapter for managed PostgreSQL (Neon/Vercel Postgres)."""
    def __init__(self, dsn):
        try:
            import psycopg2
            from psycopg2.extras import DictCursor
        except ImportError as exc:
            raise RuntimeError("DATABASE_URL is set but psycopg2-binary is missing. Add it to requirements.txt.") from exc
        if dsn.startswith("postgres://"):
            dsn = "postgresql://" + dsn[len("postgres://"):]
        self._driver = psycopg2
        self._conn = psycopg2.connect(dsn, cursor_factory=DictCursor, sslmode="require")
    def execute(self, sql, params=()):
        cur = self._conn.cursor()
        if sql.strip().upper().startswith("PRAGMA TABLE_INFO("):
            table = re.search(r"PRAGMA\s+table_info\(([^)]+)\)", sql, re.I).group(1).strip().strip('"`')
            cur.execute("SELECT ordinal_position-1 AS cid, column_name AS name, data_type AS type, 0 AS not_null, column_default AS dflt_value, 0 AS pk FROM information_schema.columns WHERE table_schema=current_schema() AND table_name=%s ORDER BY ordinal_position", (table,))
            return cur
        cur.execute(sql.replace("?", "%s"), tuple(params or ()))
        return cur
    def executescript(self, script):
        # DDL statements in our schema contain no embedded semicolons.
        for statement in script.split(";"):
            statement = statement.strip()
            if statement:
                statement = re.sub(r"INTEGER\s+PRIMARY\s+KEY\s+AUTOINCREMENT", "SERIAL PRIMARY KEY", statement, flags=re.I)
                self.execute(statement)
    def commit(self): self._conn.commit()
    def rollback(self): self._conn.rollback()
    def close(self): self._conn.close()


def get_db():
    if DATABASE_URL:
        return PostgresConnection(DATABASE_URL)
    con = sqlite3.connect(DATABASE, timeout=20)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con

def initialize_database():
    con = get_db()
    con.executescript("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
