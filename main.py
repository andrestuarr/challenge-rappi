#!/usr/bin/env python3
import snowflake.connector

def main():
    conn = snowflake.connector.connect(
        user='andrestuarr10000',
        password='qwer.1234O',
        account='HD55087.us-central1.gcp',
        session_parameters={
            'QUERY_TAG': 'EndOfMonthFinancials',
        }
    )
    conn.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS rappibank_warehouse")
    conn.cursor().execute("CREATE DATABASE IF NOT EXISTS rappibankdb")
    conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS andrestuarrdb")
    conn.cursor().execute("PUT file:///Users/andres/Downloads/archive/members.csv* @%members")
    conn.cursor().execute("COPY INTO members")

    conn.close()

if __name__ == "__main__":
    main()
