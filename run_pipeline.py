import subprocess
import sys
import duckdb

def run_pipeline():
    # 1. Fetch raw data
    print("📥 Step 1: Fetching raw data from Yahoo Finance...")
    subprocess.run([sys.executable, "data_fetch/fetch.py"], check=True)

    # 2. Run SQL transformations in order
    print("🔄 Step 2: Running SQL transformations with DuckDB...")
    con = duckdb.connect()  # Creates an in-memory DuckDB database
    
    sql_files = [
        "sql/phase-b.sql",
        "sql/phase-c.sql",
        "sql/phase-d.sql",
        "sql/phase-e.sql"
    ]
    
    for sql_file in sql_files:
        print(f"  Executing {sql_file}...")
        with open(sql_file, "r") as f:
            con.execute(f.read())
            
    print("✅ Pipeline completed successfully! Outputs generated in analysis_data/")

    # 3. Launch Streamlit dashboard
    print("📊 Step 3: Launching Streamlit dashboard...")
    try:
        subprocess.run(["streamlit", "run", "app/app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped. Goodbye!")

if __name__ == "__main__":
    run_pipeline()
    