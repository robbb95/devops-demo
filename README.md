# DevOps Demo

A simple CI/CD demo using GitHub Actions and GitHub Pages.

## What it does

Every time you push code to `main`:
1. **Tests run automatically** (pytest)
2. **If tests pass**, the site deploys to GitHub Pages
3. **If tests fail**, deployment is blocked

## Setup (one-time)

1. Push this folder to your `devops-demo` repo on GitHub
2. Go to **Settings > Pages** in your repo
3. Under "Build and deployment", select **Source: GitHub Actions**
4. Push a commit — the pipeline will run automatically

Your site will be live at: `https://robbb95.github.io/devops-demo/`

## Live demo script

During the presentation:

1. Open GitHub repo → show the code
2. Edit `index.html` (e.g. change the version number)
3. Commit & push
4. Go to **Actions** tab → watch the pipeline run in real time
5. Once green, refresh the site → change is live!
