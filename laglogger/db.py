#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
import os


DBURL = os.getenv("DATABASE_URL", "postgres://postgres@localhost:7539/postgres")


def query(sql, auto=False):
    conn = psycopg2.connect(DBURL)
    with conn.cursor() as cur:
        conn.autocommit = auto
        cur.execute(sql)
        result = cur.fetchall()
    return result


if __name__ == "__main__":
    r = query('select version()')
    print(r)
