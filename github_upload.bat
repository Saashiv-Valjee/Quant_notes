@echo off
REM Add all changes to git, excluding what's in .gitignore
git add .

REM Commit the changes
git commit -m "Auto-update: Added latest changes to Quant Notes"

REM Push the changes to GitHub
git push origin main

REM Confirm the process is complete
echo "Your Quant Notes and Images have been successfully pushed to GitHub."
pause