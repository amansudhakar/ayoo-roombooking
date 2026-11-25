# Ayoo! Rooms: MySQL setup

## Requirements

- Windows with Python 3 installed
- MySQL Community Server running locally on port 3306
- The Python package in `requirements.txt`

## First run (PowerShell)

Open PowerShell in this `Ayoo` folder and run:

```powershell
$python = Join-Path $env:LOCALAPPDATA "Python\bin\python.exe"
if (-not (Test-Path $python)) { $python = "py" }
& $python -m pip install -r requirements.txt
$env:AYOO_DB_PASSWORD = Read-Host "Enter your MySQL password"
& $python .\ayoo.pyw
```

The app creates the `ayoo` database and its four tables on first run, then adds
any missing sample rooms and the `demo_user` account (`demo1234`). This account is for classroom demonstration only. The password is read from the current PowerShell
session and is not saved in the project. Each computer needs its own running
MySQL Server and its own password; `localhost` means that computer.

Optional connection settings use `AYOO_DB_HOST`, `AYOO_DB_PORT`, and
`AYOO_DB_USER`; they default to `localhost`, `3306`, and `root`.

## Verify in MySQL Workbench

Connect to the local server, open a query tab, and run:

```sql
USE ayoo;
SHOW TABLES;
SELECT COUNT(*) AS room_count FROM room;
SELECT * FROM room ORDER BY Room_no LIMIT 10;
```

The tables should include `admin`, `room`, `user_data`, and `bookings`. In the app, add a room with number 901, then run `SELECT * FROM room WHERE Room_no = 901;` in Workbench; it should show the row. Delete room 901 in the app and run the query again; it should return no rows.

The application currently supports adding and deleting rooms. The `room`
table can also be edited directly in Workbench, for example:

```sql
UPDATE room SET Price = 5500 WHERE Room_no = 123;
```

## Demonstrate changing the table structure safely

Use a throwaway table so the application's `room` table stays intact:

```sql
USE ayoo;
CREATE TABLE room_schema_demo LIKE room;
ALTER TABLE room_schema_demo ADD COLUMN DemoNote VARCHAR(50);
SHOW COLUMNS FROM room_schema_demo;
ALTER TABLE room_schema_demo DROP COLUMN DemoNote;
SHOW COLUMNS FROM room_schema_demo;
DROP TABLE room_schema_demo;
```



