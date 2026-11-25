# Ayoo! Rooms

Ayoo! Rooms is a Python Tkinter hotel-room booking demo backed by MySQL.

## Demo login

- Username: `demo_user`
- Password: `demo1234`

This account is created automatically when the app starts. It is for classroom
demonstration only. Do not use it for real accounts or real personal data.

## !!! System Requirements
* **Python Version:** Supported up to **Python 3.12.10** (`>=3.10.0, <=3.12.10`).
* **Compatibility Warning:** Versions newer than Python 3.12.10 (including 3.12.11+ and 3.13+) are not supported and may break.

## Run the app

1. Install Python and MySQL Community Server. Start the MySQL Server service.
2. Open PowerShell in this `Ayoo` folder.
3. Run:

   ```powershell
   $python = Join-Path $env:LOCALAPPDATA "Python\bin\python.exe"
   if (-not (Test-Path $python)) { $python = "py" }
   & $python -m pip install -r requirements.txt
   $env:AYOO_DB_PASSWORD = Read-Host "Enter your MySQL password"
   & $python .\ayoo.pyw
   ```

The app creates the `ayoo` database, tables, sample rooms, and demo account on
startup. See [MYSQL_SETUP.md](MYSQL_SETUP.md) for Workbench verification and
safe table-structure demo steps.

## Project parts

- `ayoo.pyw`: Tkinter desktop interface
- `ayoosql.py`: MySQL connection, schema setup, and demo data
- `requirements.txt`: Python MySQL connector dependency

The demo account uses a simple password and stores passwords as the existing
project expects. Use it only with a local classroom demo database.
