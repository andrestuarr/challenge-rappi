#!/usr/bin/env python3
import snowflake.connector

def main():
    conn = snowflake.connector.connect(
        user='andrestuarr10000',
        password='XXXX',
        account='HD55087.us-central1.gcp',
        session_parameters={
            'QUERY_TAG': 'EndOfMonthFinancials'
        }
    )
    conn.cursor().execute('USE WAREHOUSE "rappibank"')
    conn.cursor().execute('USE DATABASE "challenge"')
    conn.cursor().execute('USE SCHEMA "andrestuarr"')
    print(conn)
    conn.cursor().execute('PUT file:///Users/andres/Downloads/archive/members.csv* @%"members" PARALLEL = 90')
    print('termino')
    conn.cursor().execute('''COPY INTO "members" FILE_FORMAT = (SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY = '"' REPLACE_INVALID_CHARACTERS = TRUE)''')

    conn.close()

if __name__ == "__main__":
    main()
