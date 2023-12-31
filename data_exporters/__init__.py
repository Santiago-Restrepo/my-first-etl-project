import pandas as pd
from sqlalchemy import create_engine, MetaData
from sqlalchemy.dialects.postgresql import insert
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get environment variables
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_db = os.getenv("POSTGRES_DB")
postgres_port = os.getenv("POSTGRES_PORT")

# Database definition
engine = create_engine(
    f'postgresql://{postgres_user}:{postgres_password}@localhost:{postgres_port}/{postgres_db}'
)


def export_to_sql(data):
    table_names = data.keys()
    with engine.connect() as conn:
        transaction = conn.begin()
        for table_name in table_names:
            df = data[table_name]
            upsert_table(conn, table_name, df)
        transaction.commit()


def upsert_table(conn, table_name: str, df: pd.DataFrame):
    metadata = MetaData()
    metadata.reflect(bind=conn.engine)
    table = metadata.tables.get(table_name)
    if table is not None:
        # Create an insert statement
        stmt = insert(table)
        # # Update columns in the statement with data from the DataFrame
        stmt = stmt.values(df.to_dict(orient='records'))

        # # Specify the conflict target columns for the upsert
        conflict_columns = [
            col.name for col in table.columns if col.primary_key]

        # # Add the ON CONFLICT clause for upsert
        stmt = stmt.on_conflict_do_update(
            index_elements=conflict_columns,
            set_={col.name: col for col in stmt.excluded}
        )

        # # Execute the statement
        conn.execute(stmt)
    else:
        print('Table does not exist')
