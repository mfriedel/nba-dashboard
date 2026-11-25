# Deploying to Streamlit Community Cloud

Step-by-step instructions for deploying this dashboard. You only do the one-time
setup (steps 1–3) once; after that, pushing to GitHub updates the live app
automatically.

**App coordinates used below:**

| Field | Value |
| --- | --- |
| Repository | `mfriedel/nba-dashboard` |
| Branch | `main` |
| File path | `app.py` |
| Python version | `3.12` |

> **Read this before step 3.** The Python version **cannot be changed after the
> app is deployed.** The only way to change it later is to delete the app and
> redeploy it. Set it to 3.12 under *Advanced settings* the first time.

---

## 1. Sign in to Streamlit Community Cloud

1. Go to **[share.streamlit.io](https://share.streamlit.io)**.
2. Click **Continue to sign-in**.
3. Click **Continue with GitHub**.
4. Enter your GitHub credentials and complete GitHub's authentication.
5. Fill in your account information and click **I accept**.

## 2. Connect your GitHub account

Signing in with GitHub is *not* the same as granting Streamlit access to your
repositories. Do this explicitly:

1. Click **Workspaces** in the upper-left corner.
2. Select **Connect GitHub account** from the dropdown.
3. Enter your GitHub credentials if prompted.
4. Click **Authorize streamlit**.

Your repository is public, so this is all the access Streamlit needs. (For a
private repo you would additionally go to your GitHub username in the upper-left
→ **Settings** → **Linked accounts** → under *Source control* click
**Connect here** → **Authorize streamlit**.)

## 3. Create the app

1. Click **Create app** in the upper-right corner of your workspace.
2. When asked *"Do you already have an app?"*, choose **Yup, I have an app.**
3. Fill in the deployment form:
   - **Repository:** `mfriedel/nba-dashboard`
   - **Branch:** `main`
   - **File path:** `app.py`
   - **App URL:** optional custom subdomain — pick something like
     `nba-dashboard` if it is available, or leave the default.
4. Click **Advanced settings**.
5. In the **Python version** dropdown, select **3.12**.
   This matches the local environment the app was built and tested against.
   Community Cloud happens to default to 3.12 today, but select it explicitly
   rather than relying on the default — the default moves as new Python
   versions are released, and this setting is permanent for the app.
6. Leave the **Secrets** field empty. This app reads a CSV committed to the
   repository and uses no API keys or credentials.
7. Click **Save** to close Advanced settings.
8. Click **Deploy**.

The build log appears while the app starts. Streamlit installs the packages
listed in `requirements.txt`, so the first deploy takes a few minutes.

## 4. Verify the deployment

Once the app loads, confirm:

- The title **NBA Dashboard** renders, with the row count and date range caption
  beneath it (2,460 team-game rows).
- All three tabs are present: **Explore Data**, **Logistic Regression**,
  **Clustering**.
- No red error box appears.

If something fails, click **Manage app** in the lower-right corner of the running
app to open the logs.

---

## Updating the deployed app

Community Cloud watches the `main` branch. Every push redeploys automatically —
there is nothing to click.

```bash
git add -A
git commit -m "Describe the change"
git push
```

Code changes appear almost immediately. Changes to `requirements.txt` take
longer, because the environment is rebuilt.

**Keep `requirements.txt` in step with the code.** The local development
environment (`~/code/DS6021_F26`) has far more packages installed than this
repository pins. A new import can therefore work locally and still crash the
deployed app with `ModuleNotFoundError`. Whenever `app.py` gains an import, add
the matching pinned package to `requirements.txt` in the same commit.

## Managing the app

From your workspace at [share.streamlit.io](https://share.streamlit.io), click
the overflow menu (**⋮**) next to the app, or click **Manage app** in the
lower-right corner of the running app:

- **Reboot** — restart the app; useful if it becomes unresponsive.
- **Settings** — change the app URL, sharing/visibility, and secrets.
- **Delete** — remove the app. Also the first half of changing the Python
  version: note your subdomain and settings, delete, then repeat step 3 with the
  new version selected.

## Troubleshooting

| Symptom | Likely cause |
| --- | --- |
| `ModuleNotFoundError` | The package is installed locally but missing from `requirements.txt`. |
| `FileNotFoundError: data/nba.csv` | The CSV was not committed. Confirm with `git ls-tree -r --name-only origin/main`. |
| Repository not listed in the form | GitHub account not connected — redo step 2. |
| App builds but behaves oddly | Version drift between local and deployed packages; confirm pins match the local versions. |

## Sources

- [Deploy your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy)
- [Quickstart / sign-in](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart)
- [App dependencies](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies)
- [Upgrade Python version](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-python)
- [App settings](https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-settings)
