#! /bin/bash
git pull
git submodule update --remote --merge
make html
git status
echo '[y/n]'
read a
if [ $a = 'y' ]
then
git add .
git commit -m "update"
git push
fi