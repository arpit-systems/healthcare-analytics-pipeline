from sqlalchemy import create_engine, text

database_url = "postgresql://airflow:airflow123@healthcare-db.cr8mwuquuzbk.ap-south-1.rds.amazonaws.com:5432/postgres"

engine = create_engine(database_url)

with engine.connect() as conn:

    result = conn.execute(text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
        ORDER BY table_name;
    """))

    print("\nData Warehouse Tables\n")

    for row in result:
        print(row[0])

print("\nWarehouse Check Completed Successfully")