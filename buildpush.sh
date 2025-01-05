#!/usr/bin/env bash
set -v
cp -r ../../pelican-themes/Flex ./pelican-themes-backup
pelican content -s publishconf.py
git add . 
git commit -m "update content"
git push origin main
ghp-import output -b gh-pages --cname=jerrychi.com
git checkout gh-pages
git push origin gh-pages
git checkout main
