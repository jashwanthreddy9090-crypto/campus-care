# Campus Care 360°

A Flask-based campus support portal with a red, cream, white, and charcoal interface.

## Current features

- Student complaint submission and status tracking
- Admin dashboard and admin-created student accounts
- Emergency help and campus contact links
- Admin-reviewed password reset requests
- Campus notices and in-app notifications
- Lost & Found listings
- Help & Support and emergency contact directory
- Password hashing and secure session-cookie settings
- PostgreSQL support for persistent hosted data; SQLite for local development

The worker portal, Campus Map, and AI chat have been retired from the current preview branch. Legacy database tables, if already present, are left untouched so stored data is not accidentally deleted.

## Code map — start here before editing

**Read [CODE_MAP.md](CODE_MAP.md) before changing application code.** It explains where common changes belong and lays out a staged plan for moving the current large `app.py` into smaller modules without changing app behaviour all at once.

Current code is primarily in `app.py`, including Flask routes, database compatibility code, and embedded HTML/CSS/JavaScript. The proposed folder structure in `CODE_MAP.md` is a plan; files should only be moved there as each stage is implemented and tested.

## Project files

Keep these deployment files at the **root of the GitHub repository**:

```text
app.py
requirements.txt
vercel.json
README.md
CODE_MAP.md
migrate_sqlite_to_postgres.py  # optional, only for migrating an existing SQLite database
```

Do not put these files one folder deeper inside the repository.

## Run locally (Windows PowerShell)

1. Install Python 3.10 or newer.
2. Open PowerShell in the folder containing `app.py`.
3. Create and activate a virtual environment (optional but recommended):

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Set local environment variables. Use your own long random secret and a strong admin password. The configured admin email must end in `@campus.360`.

   ```powershell
   $env:SECRET_KEY = "replace-with-a-long-random-secret"
   $env:ADMIN_EMAIL = "admin@campus.360"
   $env:ADMIN_PASSWORD = "replace-with-a-strong-password"
   ```

6. Start the application:

   ```powershell
   python app.py
   ```

7. Open `http://127.0.0.1:5000` in your browser.

## Deploy to Vercel using GitHub

### 1. Push the project to GitHub

- Keep `app.py`, `requirements.txt`, `vercel.json`, and documentation at the repository root.
- Verify the branch connected to the Vercel project before pushing.
- Never commit passwords, secret keys, or database credentials.

### 2. Connect the repository in Vercel

- Open the Vercel dashboard and choose **Add New → Project** to import the repository if it is not already connected.
- If the project already exists, open **Settings → Git** and verify the connected repository and production branch.

### 3. Configure environment variables

In **Vercel → Project → Settings → Environment Variables**, configure the variables for the required environments:

| Variable | Required | Purpose |
|---|---|---|
| `SECRET_KEY` | Yes | Long, random session-signing secret. |
| `DATABASE_URL` | Strongly recommended for hosted use | Connection string for managed PostgreSQL. `POSTGRES_URL` and `POSTGRES_PRISMA_URL` are also recognized. |
| `ADMIN_EMAIL` | To bootstrap the first admin | Must end in `@campus.360`, for example `admin@campus.360`. |
| `ADMIN_PASSWORD` | To bootstrap the first admin | Strong initial password; the app hashes it before storing it. |
| `ADMIN_NAME` | Optional | Display name for the first admin. |
| `ADMIN_MOBILE` | Optional | Admin contact number. |

Save changed variables and redeploy the relevant environment.

### 4. Sign in and configure the campus

- Open your deployed site and sign in through `/login`.
- The first admin account is created only when the configured email does not already exist. Changing `ADMIN_PASSWORD` later does not automatically change an existing account's password.
- Use the admin portal to create student accounts.
- Verify emergency and official campus contact numbers before students rely on them.

## If Vercel says “Git information retrieval failed”

This is normally a repository integration/permissions problem, not necessarily an `app.py` syntax error.

1. Check that the GitHub repository exists and the intended commit is pushed.
2. In Vercel, open **Project → Settings → Git** and verify the connected repository.
3. In GitHub, open **Settings → Applications → Installed GitHub Apps**, select Vercel, and check its repository access.
4. Retry the deployment. If the repository was renamed or moved, reconnect the correct repository.
5. If Git-based deployments remain unavailable, use the Vercel CLI from the project root after installing and signing in to it.

## Database and file-storage notes

- Vercel's local filesystem (including `/tmp`) is temporary. SQLite on Vercel is **not persistent**. Configure managed PostgreSQL through `DATABASE_URL` for hosted data.
- Existing SQLite records are not copied automatically when switching to PostgreSQL. Back up both databases and review `migrate_sqlite_to_postgres.py` before running a migration.
- Complaint image uploads stored in the app's local upload folder are not durable on Vercel. Use object storage for production uploads.
- Replace sample emergency/contact details with verified campus numbers.
- Emergency links may open the device dialler; do not assume that a call or alert was sent merely because a button was tapped.

## Security and refactoring checklist

- Keep `SECRET_KEY`, `ADMIN_PASSWORD`, and database credentials out of GitHub.
- Verify identity before approving password resets.
- Preserve existing database records and production settings during refactoring.
- Make structural changes in small commits on a preview branch.
- Test login, permissions, complaints, Lost & Found, notifications, database persistence, and mobile layouts on the preview deployment before merging to production.
