git config user.name "Suriya-Z"
git config user.email "suriya-z@users.noreply.github.com"
git stash
git pull origin main --rebase
git stash pop
git add .
git commit -m "Fix synchronous model load hang, add Render deployment configs, and fix requirements.txt"
git push origin main
