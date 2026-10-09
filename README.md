CAMPUS CARE 360° — UPDATED FLASK PROJECT

Included features
- Existing student complaint submission and status tracking
- Admin dashboard, admin-issued student accounts and worker portal
- Emergency / SOS centre and campus contacts
- Admin-approved password reset requests
- Student Life dashboard with latest notices and unread notification count
- Admin-published campus notices with student notifications
- Notifications for complaint submission, admin assignment/status changes and worker updates
- Lost & Found listings with private claim requests and admin resolution
- Admin-managed Campus Map / campus services directory with optional external map links
- Context-aware, database-aware AI assistant with account-specific persistent chat history
- PostgreSQL persistence using DATABASE_URL, POSTGRES_URL or POSTGRES_PRISMA_URL; SQLite fallback for local development
- Hashed passwords, HTTP-only session cookies, SameSite=Lax, secure cookies on Vercel, no public self-registration

Deploy on Vercel
1. Upload/commit app.py, requirements.txt and vercel.json to your GitHub repository.
2. Create a managed PostgreSQL database (for example, a Vercel-supported Postgres integration or Neon).
3. Add the database connection string as DATABASE_URL in Vercel Environment Variables. The app also recognizes POSTGRES_URL and POSTGRES_PRISMA_URL.
4. Set SECRET_KEY to a long random secret. Vercel startup intentionally fails if this is missing.
5. Set ADMIN_EMAIL to an email ending in @campus.360, ADMIN_PASSWORD to a strong initial password, and optionally ADMIN_NAME / ADMIN_MOBILE.
6. Set the variables for Production (and Preview if needed), then redeploy.
7. Sign in at /login. The app creates the first admin only if the configured admin email does not already exist. It does not overwrite an existing admin password on each cold start.
8. Admins can create student accounts at /admin/students and worker credentials at /admin/workers.
9. Admins publish notices at /notices and add campus places at /campus-map.

Important database notes
- SQLite is used only as a local fallback. Vercel's /tmp SQLite storage is temporary and is NOT persistent. Configure DATABASE_URL before using the deployed app for real accounts or complaints.
- Switching an existing deployment from SQLite to PostgreSQL does not automatically copy old records. Use migrate_sqlite_to_postgres.py if you have a local campuscare.db and want to migrate its rows after the PostgreSQL schema has been initialized. Review the source and destination before running it.
- Complaint photo uploads are still stored in the local uploads folder (/tmp on Vercel), so uploaded images may not persist across serverless instances. For production, use object storage such as Vercel Blob or another durable file store.
- Campus Map starts empty. An admin must add verified campus locations and actual map links. Demo campus phone numbers must be replaced with official contacts before real use.
- Emergency links open the device dialler; this app does not silently dispatch an SOS or transmit location.
- The AI assistant is a context-aware rules/data retrieval assistant, not a hosted generative AI API. It can surface available notices and a student's own recent complaint statuses. It should not be treated as an official source for unrecorded campus details.

Local development
- Install dependencies: python -m pip install -r requirements.txt
- Set SECRET_KEY, ADMIN_EMAIL and ADMIN_PASSWORD in your local environment.
- Run: python app.py
- Open http://127.0.0.1:5000

Security checklist
- Never commit real passwords, database URLs or SECRET_KEY to GitHub.
- Verify identity before approving password reset requests.
- Replace all demo contact numbers with official campus contacts.
- Use persistent PostgreSQL and durable file storage before a real campus rollout.
- Back up the database and test account recovery before deployment.
