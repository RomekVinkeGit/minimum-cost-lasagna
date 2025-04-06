import os
import subprocess
from datetime import datetime, timedelta

# --- Config ---
REPO_URL = "https://github.com/supermarkt/checkjebon.git"
LOCAL_REPO = "checkjebon"
TARGET_FILE = "data/supermarkets.json"
OUTPUT_DIR = "supermarkets_versions"

# --- Clone repo if not already cloned ---
if not os.path.exists(LOCAL_REPO):
    subprocess.run(["git", "clone", REPO_URL])

os.chdir(LOCAL_REPO)

# --- Get all commits that modified the target file ---
log_output = subprocess.check_output([
    "git", "log", "--format=%H %ad", "--date=short", "--", TARGET_FILE
]).decode().splitlines()

# --- Parse commits into (hash, date) tuples ---
commits = []
for line in log_output:
    commit_hash, commit_date = line.strip().split(" ")
    commits.append((commit_hash, datetime.strptime(commit_date, "%Y-%m-%d")))

# --- Filter: one commit per week ---
commits.sort(key=lambda x: x[1])  # sort by date
weekly_commits = []
last_date = None

for commit_hash, commit_date in commits:
    if not last_date or (commit_date - last_date >= timedelta(days=7)):
        weekly_commits.append((commit_hash, commit_date))
        last_date = commit_date

# --- Ensure output directory exists ---
os.makedirs(f"../{OUTPUT_DIR}", exist_ok=True)

# --- Checkout each commit, save file if it exists ---
for commit_hash, commit_date in weekly_commits:
    subprocess.run(["git", "checkout", commit_hash], stdout=subprocess.DEVNULL)

    if not os.path.exists(TARGET_FILE):
        print(f"Skipped {commit_hash} ({commit_date.strftime('%Y-%m-%d')}): file not found.")
        continue

    output_path = f"../{OUTPUT_DIR}/supermarkets_{commit_date.strftime('%Y-%m-%d')}.json"
    with open(TARGET_FILE, "r", encoding="utf-8") as src, open(output_path, "w", encoding="utf-8") as dst:
        dst.write(src.read())
    print(f"Saved: {output_path}")

# --- Return to main branch (optional, or use 'master' if needed) ---
subprocess.run(["git", "checkout", "main"], stdout=subprocess.DEVNULL)
