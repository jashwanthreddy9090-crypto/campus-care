# Campus Care - Vercel Ready

Original Campus Care app with only Vercel compatibility and the `@campus.360` email restriction.

Only emails ending exactly with `@campus.360` can register or log in.

Vercel settings: Root `./`, Build Command empty, Output Directory empty, Install Command `pip install -r requirements.txt`.

Optional admin environment variables: `ADMIN_EMAIL`, `ADMIN_PASSWORD`, `ADMIN_NAME`, `ADMIN_MOBILE`, `SECRET_KEY`.

Vercel `/tmp` storage is temporary; use a hosted database for permanent production data.
