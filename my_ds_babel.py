import sqlite3
import pandas as pd
import csv
from io import StringIO


def sql_to_csv(database, table_name):
    conn = sqlite3.connect(database)
    cmd = "SELECT * FROM " + table_name + ";"
    cursor = conn.execute(cmd)
    names = list(map(lambda x: x[0], cursor.description))
    df = pd.DataFrame(cursor, columns=names)
    csv_name = "list_" + table_name + ".csv"
    df.to_csv(csv_name, index=False)
    return df.to_csv(index=False)


def csv_to_sql(csv_content, database, table_name):
    df = pd.read_csv(csv_content)
    db = sqlite3.connect(database)
    df.to_sql(table_name, db, if_exists="replace", index=False)