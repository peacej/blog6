pelican content -s publishconf.py
git add . 
git commit -m "update content"
git push origin main
ghp-import output -b gh-pages
git checkout gh-pages
git push origin gh-pages
git checkout main