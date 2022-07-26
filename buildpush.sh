git add . 
git commit -m "update content"
pelican content -s publishconf.py
git checkout main
git push origin main
ghp-import output -b gh-pages
git checkout gh-pages
git pull
git push origin gh-pages
git checkout main