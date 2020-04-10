@echo off

echo ----------------------------------------------------------------
echo start of working
echo ----------------------------------------------------------------
echo ----------------------------------------------------------------

echo enter repo name
set /p "reponame=Enter the folder name to be created: "||(pause &goto :eof)

 python remote.py  %reponame%>output

set /p myvar=<output

echo %myvar%
cd /d D:/projects/

md "%reponame%"
echo "%reponame%"
cd %reponame%

git init 
echo  init readme >Readme.md
 git add Readme.md
 git commit -m "frist commit"
 git remote add origin %myvar%
 git push -u origin master




