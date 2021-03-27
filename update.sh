#! /bin/bash
while true; do if git pull; then break; fi; done
while true; do if git submodule update --remote --merge; then break; fi; done
make html
git status
echo '[y/n]'
read a
if [ $a = 'y' ]
then
git add .
git commit -m "update"
while true; do if git push; then break; fi; done
fi
