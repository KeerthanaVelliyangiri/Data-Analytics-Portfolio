import sqlite3, json, os
DB_PATH = os.getenv("RESUMESYNC_DB", "resumesync.db")


def _connect():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def init_db():
    with _connect() as con:
        con.execute("CREATE TABLE IF NOT EXISTS reports (id INTEGER PRIMARY KEY AUTOINCREMENT, workspace TEXT NOT NULL, mode TEXT NOT NULL, candidate_name TEXT, report_json TEXT NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        con.execute("CREATE INDEX IF NOT EXISTS idx_reports_workspace ON reports(workspace)")


def save_report(workspace, mode, candidate_name, report):
    safe_report = {k:v for k,v in report.items() if k != "resume_chunks"}
    with _connect() as con:
        con.execute("INSERT INTO reports(workspace, mode, candidate_name, report_json) VALUES(?,?,?,?)", (workspace, mode, candidate_name, json.dumps(safe_report, ensure_ascii=False)))


def get_reports(workspace, mode=None):
    with _connect() as con:
        if mode:
            rows = con.execute("SELECT report_json FROM reports WHERE workspace=? AND mode=? ORDER BY created_at DESC", (workspace, mode)).fetchall()
        else:
            rows = con.execute("SELECT report_json FROM reports WHERE workspace=? ORDER BY created_at DESC", (workspace,)).fetchall()
    return [json.loads(row[0]) for row in rows]
