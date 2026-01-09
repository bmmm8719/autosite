import os
import subprocess
from datetime import datetime

# -------------------------------
# CONFIGURATION
# -------------------------------
GITHUB_USERNAME = "bmmm8719"        # your GitHub username
REPO_NAME = "autosite"               # your repository name

# Read GitHub token from environment variable
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN environment variable not set. Run: export GITHUB_TOKEN='your_token_here'")

SITE_DIR = "."

# -------------------------------
# HELPER FUNCTION
# -------------------------------
def run(cmd):
    """Run a shell command and raise error if it fails"""
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

# -------------------------------
# MAIN FUNCTION
# -------------------------------
def main():
    # Step 1: Generate site content
    # (Replace this with your article generation code)
    # For demo, we just create a timestamp file
    os.makedirs(SITE_DIR, exist_ok=True)
    filename = f"{SITE_DIR}/article_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(filename, "w") as f:
        f.write(f"# Auto-generated article {datetime.now()}\n\nThis is a demo article.")

    print("✅ Website generated successfully.")
    print(f"📁 Files located in the /{SITE_DIR} folder.")

    # Step 2: Initialize git repo
    run("git init")

    # Step 3: Configure Git user
    run('git config user.name "Bryan"')
    run('git config user.email "bryan.macias@gmail.com"')

    # Step 4: Set remote origin safely
    remote_url = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
    run(f"git remote remove origin || true")  # remove if exists
    run(f"git remote add origin {remote_url}")

    # Step 5: Commit changes
    run("git add .")
    run(f'git commit -m "Auto update {datetime.now()}"')

    # Step 6: Push to GitHub
    run("git push -f origin main")

    print("✅ Article generated and published automatically")

# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    main()