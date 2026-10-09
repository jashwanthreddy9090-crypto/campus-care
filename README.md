# Campus Care 360°

A Flask-based campus support portal for students, administrators, and maintenance workers. The interface uses the Campus Care red, cream, white, and charcoal theme.

## Features

- Student complaint submission and status tracking
- Admin dashboard and admin-created student accounts
- Worker login and assigned-work portal
- Emergency help and campus contact links
- Admin-reviewed password reset requests
- Campus notices and in-app notifications
- Lost & Found listings
- Admin-managed campus map and service directory
- Rules/data-based Campus Care AI assistant with saved chat history
- Password hashing and secure session-cookie settings
- PostgreSQL support for persistent hosted data; SQLite for local development

## Project files

Keep these files at the **root of the GitHub repository**:

```text
app.py
requirements.txt
vercel.json
README.md
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

- Open your repository and upload/commit `app.py`, `requirements.txt`, `vercel.json`, and `README.md` at the repository root.
- Confirm the latest commit appears on the branch configured for production (commonly `main`).
- Never commit passwords, secret keys, or database credentials.

### 2. Connect the repository in Vercel

- Open the Vercel dashboard and choose **Add New → Project**.
- Import the correct GitHub repository and grant Vercel access to it.
- If the project already exists, open **Settings → Git** and verify the connected repository and production branch.

### 3. Configure environment variables

In **Vercel → Project → Settings → Environment Variables**, add the following for the **Production** environment (and Preview too, if needed):

| Variable | Required | Purpose |
|---|---|---|
| `SECRET_KEY` | Yes | Long, random session-signing secret. The app intentionally stops on Vercel if this is missing. |
| `DATABASE_URL` | Strongly recommended for hosted use | Connection string for a managed PostgreSQL database. `POSTGRES_URL` and `POSTGRES_PRISMA_URL` are also recognized. |
| `ADMIN_EMAIL` | To bootstrap the first admin | Must end in `@campus.360`, for example `admin@campus.360`. |
| `ADMIN_PASSWORD` | To bootstrap the first admin | Strong initial password; the app hashes it before storing it. |
| `ADMIN_NAME` | Optional | Display name for the first admin. |
| `ADMIN_MOBILE` | Optional | Admin contact number. |

Save the variables, then redeploy so the deployment receives them.

### 4. Sign in and configure the campus

- Open your deployed site and sign in through `/login`.
- The first admin account is created only when the configured email does not already exist. Changing `ADMIN_PASSWORD` later does not automatically change an existing account's password.
- Use the admin portal to create student accounts and worker credentials.
- Add verified campus locations and official contact numbers before students rely on them.

## If Vercel says “Git information retrieval failed”

This is normally a repository integration/permissions problem, not an `app.py` syntax error.

1. Check that the GitHub repository still exists and that your latest commit is pushed.
2. In Vercel, open **Project → Settings → Git** and verify the correct repository is connected.
3. In GitHub, open **Settings → Applications → Installed GitHub Apps**, select Vercel, and make sure it has access to the repository.
4. Return to Vercel and retry the deployment. If the repository was renamed or moved, reconnect the correct repository in Vercel.
5. If Git-based deployments remain unavailable, use the Vercel CLI from the project root after installing/signing in to the CLI. Fix repository access before relying on automatic Git deployments.

## Database and file-storage notes

- Vercel's local filesystem (including `/tmp`) is temporary. SQLite on Vercel is **not persistent**. Configure a managed PostgreSQL database through `DATABASE_URL` before using the hosted app for real data.
- Existing SQLite records are not copied automatically when switching to PostgreSQL. The optional `migrate_sqlite_to_postgres.py` script can migrate a local database; back up both databases and review the script before running it.
- Complaint image uploads are currently stored in the app's local upload folder. On Vercel these files are not durable. Use object storage (for example, Vercel Blob or another persistent file service) for production uploads.
- The Campus Map starts empty until an administrator adds locations.
- Replace sample/demo worker and emergency contact numbers with verified campus numbers before public use.
- Emergency links open the device dialler; the app does not silently contact emergency services or transmit a user's location.
- The AI assistant uses application rules and stored data. It is not connected to a hosted generative AI API and cannot know details that have not been entered into the app.

## Security checklist

- Keep `SECRET_KEY`, `ADMIN_PASSWORD`, and database credentials out of GitHub.
- Use a unique, strong admin password and verify identity before approving password resets.
- Use PostgreSQL and durable object storage for hosted use.
- Replace all sample contact details before rollout.
- Test admin, student, worker, complaint, and password-reset workflows in a staging deployment before real campus use.
