#!/usr/bin/env fish

# Git setup
set GIT_NAME "Your Name"
set GITHUB_USER "your-github-username"
set GIT_EMAIL "$GITHUB_USER@users.noreply.github.com"

git config --global user.name "$GIT_NAME"
git config --global user.email "$GIT_EMAIL"

echo "Git user set to $GIT_NAME <$GIT_EMAIL>"
