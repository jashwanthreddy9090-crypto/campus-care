# Campus Care 360 — Code Map and Refactoring Plan

## Why this file exists

The application currently lives mainly in `app.py`. It contains Flask setup, database compatibility code, schema migrations, route handlers, and a large embedded HTML/CSS/JavaScript interface. This guide is the index for finding the right place to make changes without accidentally changing unrelated features.

**Safety rule:** work on `refactor/code-organization-guide` or another preview branch first. Do not push structural changes directly to the production branch. Test the Vercel preview before merging anything.

## 1. Where to make common changes

| If you want to change… | Start looking in… | Be careful about… |
|---|---|---|
| App startup, Flask configuration, request guards | Top of `app.py` | Route names referenced by guards and redirects |
| Database connection / Neon PostgreSQL / local SQLite | `DATABASE_URL`, `PostgresConnection`, `get_db()` | Connection pooling, transaction cleanup, placeholders and serverless limits |
| Brief database-pool saturation / service health | `DatabaseBusyError`, `_get_pooled_connection()`, `/healthz` in `app.py` | A busy pool returns HTTP 503 with `Retry-After: 2`; `/healthz` does not prove Neon is healthy |
| Database tables or upgrades | `initialize_database()` | Existing users, complaints and records; use additive migrations and never drop tables casually |
| Complaint categories, priority rules, statuses and allowed image extensions | `campus_config.py` (`CATEGORIES`, `PRIORITIES`, `STATUSES`, `ALLOWED_EXTENSIONS`, `priority_for_category()`) | Safety categories must not be assigned a lower priority by form input |
| Campus contact numbers | `campus_config.py` → `CONTACTS` | Verify numbers with the campus before relying on them |
| Login, sessions, passwords and role permissions | Authentication and account routes in `app.py` | Password hashing, admin-only account creation, session checks |
| Student profile or dashboard links | Embedded HTML/template strings in `app.py` | Keep route endpoints and `url_for(...)` names in sync |
| Complaint form, status, admin actions | Complaint-related route handlers and their embedded templates | Preserve complaint IDs, status history and existing records |
| Lost & Found | Lost & Found routes and embedded templates | Image upload handling and persistence on Vercel |
| Notices and notifications | Notice/notification handlers and embedded templates | Read/unread state and account ownership |
| Emergency SOS history, callback requests and admin follow-up | `emergency_call_logs`, `/emergency/sos-log`, `/emergency/request-callback`, `/admin/emergency-call/<id>` and `/webhooks/telephony/calls` in `app.py` | SOS taps are not proof a call completed; incoming phone-call logs require a configured telephony provider and `TELEPHONY_WEBHOOK_TOKEN` |
| Colors, spacing, responsive layout or mobile menu | Embedded CSS and JavaScript in the main page/template strings | Test narrow mobile widths and all role dashboards |
| Packages | `requirements.txt` | Vercel build compatibility |
| Vercel deployment region/config | `vercel.json` | Do not change production deployment settings casually |

The shared category/priority/status/contact rules have been extracted to `campus_config.py`; `app.py` imports them. Database access, routes and embedded templates remain in `app.py` for now. The exact implementation is the source of truth. Use GitHub's file view and search for the function/constant name before editing; do not rely on line numbers because they change as the code evolves.

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
- **Completed first sub-step:** shared complaint categories, priority rules, statuses, allowed image extensions, contact directory and campus-email validation are in `campus_config.py`.
- Next, move environment/configuration values into `config.py`.
- Move the Neon connection pool, PostgreSQL adapter, `get_db()`, and schema initialization into `db/`.
- Preserve current environment-variable names and database compatibility.
- Verify startup and basic reads/writes against a preview database before proceeding.

### Stage 3 — Separate business rules and route groups
- Complaint priority and shared validation currently live in `campus_config.py`; if later moved into `services/`, keep the import compatibility and add tests first.
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

## 4. Emergency traffic and temporary database saturation

- The Emergency & SOS page currently opens the phone dialler with `tel:112`; it does **not** automatically send an SOS alert or contact multiple people from the server.
- `/healthz` is a lightweight platform check and intentionally does not consume a Neon connection. It confirms that the Flask handler responds, not that database reads/writes are working.
- The Neon pool remains capped at five connections per running app instance. When all are busy, a request waits briefly (up to about 1.5 seconds) for a connection; if the pool remains full, the app returns HTTP 503 with `Retry-After: 2` rather than failing with an unhandled pool-exhaustion error.
- This is graceful overload handling, not a guarantee against all traffic spikes. Real capacity depends on Vercel concurrency/scaling, Neon limits, request duration and other database clients. Load-test only a Preview deployment and monitor Vercel/Neon metrics before making capacity claims.
- In an immediate emergency in India, call 112 directly; do not wait for the website to recover.

### Emergency Call History & Callback Management

- `emergency_call_logs` is created additively by `initialize_database()`; it does not replace or delete existing tables or records.
- The SOS shortcut makes a best-effort request to `/emergency/sos-log` before opening `tel:112`. This records a tap, not a confirmed or completed phone call.
- Students can submit a campus callback request from the Emergency & SOS page. The request includes a phone number, emergency category and optional details.
- Admins see recent events in the Admin Dashboard, can use `tel:<caller number>` to call back, and can update the callback status and notes.
- To capture real incoming calls made to a phone number, connect a telephony provider to `POST /webhooks/telephony/calls`. Set `TELEPHONY_WEBHOOK_TOKEN` in the Vercel Preview environment and configure the provider to send the same value in the `X-Campus-Webhook-Token` header. Provider payloads must include a caller number and a unique call ID. This generic endpoint is not a substitute for completing and testing a provider-specific integration.
- Until a provider is configured and tested, only app SOS taps and app callback requests are recorded; calls made directly to a normal mobile phone are not automatically visible to the website.
- Keep the admin dashboard restricted to authorized accounts. Mobile numbers and callback notes are personal information and should only be retained as long as operationally necessary.

## 5. Rules that prevent accidental damage

1. **Never reset or recreate the production database** as part of a code-organization change.
2. Keep database changes additive; do not delete tables or records during refactoring.
3. Do not rename environment variables without a compatibility plan.
4. Keep secrets and connection strings out of source files and commits.
5. Preserve Flask route names, form field names, session keys, database column names and complaint IDs unless a deliberate migration is reviewed.
6. Keep each stage in a separate commit so a regression can be traced or reverted.
7. Check Vercel build logs and test the preview URL after each deployment.
8. A refactor should change structure, not user-visible behaviour. Feature changes belong in separate commits.

## 6. Definition of done for each stage

- The code imports and the application starts.
- No unrelated route or feature disappears.
- Existing database records remain intact.
- The Vercel Preview deployment reaches **Ready**.
- The affected workflow is manually tested on desktop and mobile.
- The commit and preview URL are recorded before moving to the next stage.
