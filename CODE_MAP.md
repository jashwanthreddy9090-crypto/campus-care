# Campus Care 360 — Code Map and Refactoring Plan

## Why this file exists

The application currently lives mainly in `app.py`. It contains Flask setup, database compatibility code, schema migrations, route handlers, and a large embedded HTML/CSS/JavaScript interface. This guide is the index for finding the right place to make changes without accidentally changing unrelated features.

**Safety rule:** work on `refactor/code-organization-guide` or another preview branch first. Do not push structural changes directly to the production branch. Test the Vercel preview before merging anything.

## 1. Where to make common changes

| If you want to change… | Start looking in… | Be careful about… |
|---|---|---|
| App startup, Flask configuration, request guards | Top of `app.py` | Route names referenced by guards and redirects |
| Database connection / Neon PostgreSQL / local SQLite | `DATABASE_URL`, `PostgresConnection`, `get_db()` | Connection pooling, transaction cleanup, placeholders and serverless limits |
| Database tables or upgrades | `initialize_database()` | Existing users, complaints and records; use additive migrations and never drop tables casually |
| Complaint categories and automatic priority | `COMPLAINT_CATEGORIES`, `PRIORITIES`, `priority_for_category()` | Safety categories must not be assigned a lower priority by form input |
| Campus contact numbers | `CONTACTS` | Verify numbers with the campus before relying on them |
| Login, sessions, passwords and role permissions | Authentication and account routes in `app.py` | Password hashing, admin-only account creation, session checks |
| Student profile or dashboard links | Embedded HTML/template strings in `app.py` | Keep route endpoints and `url_for(...)` names in sync |
| Complaint form, status, admin actions | Complaint-related route handlers and their embedded templates | Preserve complaint IDs, status history and existing records |
| Lost & Found | Lost & Found routes and embedded templates | Image upload handling and persistence on Vercel |
| Notices and notifications | Notice/notification handlers and embedded templates | Read/unread state and account ownership |
| Help & Support / emergency contacts | Help/support route, `CONTACTS`, and related template | Keep verified contact details; do not imply an alert was sent if it was not |
| Colors, spacing, responsive layout or mobile menu | Embedded CSS and JavaScript in the main page/template strings | Test narrow mobile widths and all role dashboards |
| Packages | `requirements.txt` | Vercel build compatibility |
| Vercel deployment region/config | `vercel.json` | Do not change production deployment settings casually |

The exact implementation is the source of truth. Use GitHub's file view and search for the function/constant name before editing; do not rely on line numbers because they change as the code evolves.

## 2. Recommended target structure

This is the planned destination, not a claim that these files have already been extracted. Moving code will be done in small, reviewable stages.

```text
campus-care/
├── app.py                    # Small Flask app factory/startup entry point
├── config.py                 # Environment variables and app configuration
├── db/
│   ├── __init__.py
│   ├── connection.py         # Neon pool and SQLite/PostgreSQL adapter
│   └── schema.py             # Safe schema initialization and migrations
├── services/
│   ├── complaints.py         # Complaint rules and priority calculation
│   ├── notifications.py      # Notification creation/read state
│   └── accounts.py           # Account-related business rules
├── routes/
│   ├── auth.py               # Login, logout and password reset
│   ├── student.py            # Student dashboard/profile/complaints
│   ├── admin.py              # Admin-only operations
│   ├── lost_found.py         # Lost & Found
│   └── support.py            # Help & Support and emergency contacts
├── templates/                # HTML templates, extracted incrementally
├── static/
│   ├── css/                  # Shared stylesheets
│   ├── js/                   # Shared browser scripts
│   └── images/               # Non-secret image assets
├── tests/                    # Regression tests
├── CODE_MAP.md               # This guide
├── requirements.txt
├── vercel.json
└── README.md
```

Only create a module when the corresponding code is actually moved and imported by the app. Keep the current single-file app working until each extraction is verified.

## 3. Staged refactor — one safe step at a time

### Stage 1 — Map and document the existing app
- Keep the current routes, templates, database schema and behaviour unchanged.
- Use this map to identify the responsible function/section before editing.
- Fix outdated documentation separately from application behaviour.

### Stage 2 — Separate configuration and database code
- Move environment/configuration values into `config.py`.
- Move the Neon connection pool, PostgreSQL adapter, `get_db()`, and schema initialization into `db/`.
- Preserve current environment-variable names and database compatibility.
- Verify startup and basic reads/writes against a preview database before proceeding.

### Stage 3 — Separate business rules and route groups
- Extract pure business rules first (such as complaint priority) into `services/`.
- Move routes in small groups, beginning with low-coupling support pages, then student and admin flows.
- Preserve every existing endpoint name or update every reference consistently.
- Do not remove or rename routes just to make the structure look cleaner.

### Stage 4 — Extract HTML, CSS and JavaScript
- Move embedded page templates into `templates/` and shared assets into `static/`.
- Replace inline template rendering with `render_template()` incrementally.
- Test navigation, forms, uploads, responsive styles and role-specific dashboards after each group.

### Stage 5 — Add regression checks and preview verification
- Add tests for login/permissions, complaint submission and tracking, priority rules, Lost & Found, notifications and database persistence.
- Deploy only to a Vercel Preview deployment while refactoring.
- Compare important pages and workflows against the current preview.
- Merge to production only after the owner explicitly approves.

## 4. Rules that prevent accidental damage

1. **Never reset or recreate the production database** as part of a code-organization change.
2. Keep database changes additive; do not delete tables or records during refactoring.
3. Do not rename environment variables without a compatibility plan.
4. Keep secrets and connection strings out of source files and commits.
5. Preserve Flask route names, form field names, session keys, database column names and complaint IDs unless a deliberate migration is reviewed.
6. Keep each stage in a separate commit so a regression can be traced or reverted.
7. Check Vercel build logs and test the preview URL after each deployment.
8. A refactor should change structure, not user-visible behaviour. Feature changes belong in separate commits.

## 5. Definition of done for each stage

- The code imports and the application starts.
- No unrelated route or feature disappears.
- Existing database records remain intact.
- The Vercel Preview deployment reaches **Ready**.
- The affected workflow is manually tested on desktop and mobile.
- The commit and preview URL are recorded before moving to the next stage.
