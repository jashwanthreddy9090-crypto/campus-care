"""Configuration constants and complaint-validation rules for Campus Care 360.

Keep category labels, status choices, contact directory entries, and the
server-side priority mapping here. Update this file when those shared rules
change; Flask routes and templates remain in app.py for now.
"""
import re

CATEGORIES = [
    "Hostel", "Classroom", "Laboratory", "Washroom", "Electricity", "Water",
    "Wi-Fi", "Food/Mess", "Cleaning", "Security", "Ragging / Bullying",
    "Sexual Harassment / Misconduct", "Threats / Violence", "Discrimination",
    "Medical Emergency", "Fire / Safety Hazard", "Electrical Hazard",
    "Water Leakage / Plumbing", "Theft / Missing Belongings",
    "Mental Health / Student Welfare", "Transport", "Other",
]

PRIORITIES = ["Low", "Medium", "High", "Emergency"]
STATUSES = ["Submitted", "Assigned", "In Progress", "Resolved", "Closed"]
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}

CONTACTS = [
    ("Campus Admin", "Administration", "9876500001"),
    ("Hostel Warden", "Hostel Office", "9876500002"),
    ("Maintenance Desk", "Maintenance", "9876500003"),
    ("Security Desk", "Security", "9876500004"),
    ("Emergency Help", "Emergency", "112"),
]


def priority_for_category(category):
    """Return a complaint priority based on its category, not form input."""
    category = (category or "").strip().casefold()
    emergency_categories = {
        "medical emergency", "fire / safety hazard", "threats / violence",
    }
    high_categories = {
        "ragging / bullying", "sexual harassment / misconduct", "discrimination",
        "security", "electrical hazard", "water leakage / plumbing", "electricity",
        "theft / missing belongings", "mental health / student welfare", "hostel",
    }
    low_categories = {"wi-fi", "cleaning", "food/mess", "classroom", "laboratory"}

    if category in emergency_categories:
        return "Emergency"
    if category in high_categories:
        return "High"
    if category in low_categories:
        return "Low"
    return "Medium"


def valid_campus_email(email):
    """Validate the app's campus email format."""
    return bool(re.fullmatch(r"[^@\s]+@campus\.360", (email or "").strip().lower()))
