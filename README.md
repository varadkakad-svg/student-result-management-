# Student Result Management System

## Overview
A beginner-friendly console application written in Python. It collects student details and marks in five subjects, validates the input, and calculates total marks, percentage, grade, and pass/fail status.

## Requirements
- Python 3.8 or newer
- No third-party packages required

## How to run
1. Install Python 3 if it is not already installed.
2. Open a terminal or command prompt in this folder.
3. Run:
   ```bash
   python student_result.py
   ```
   On some systems, use `python3 student_result.py`.

## Features
- Student name and roll-number input
- Five predefined subjects
- Validation for marks from 0 to 100
- Total and percentage calculation
- Grade calculation
- Pass/fail check (minimum 35 marks in every subject)
- Menu to calculate more than one result

## Grade scale
| Percentage | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| Below 40 | F |

## GitHub upload
Create a new repository on GitHub, then upload `student_result.py` and `README.md`. Alternatively, use Git:
```bash
git init
git add student_result.py README.md
git commit -m "Add student result management system"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
Replace the example repository URL with your own. Do not include passwords or access tokens in the repository.
