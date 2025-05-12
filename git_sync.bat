@echo off
cd /d "C:\python\python journey"
git add .
set /p message="Commit message: "
git commit -m "%message%"
git push
pause
