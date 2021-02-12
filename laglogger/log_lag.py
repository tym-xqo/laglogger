#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

import db

logging.basicConfig(filename='example.log', level=logging.DEBUG)


def main():
    lagsql = ("select clock_timestamp() t "
              ", clock_timestamp() - pg_last_xact_replay_timestamp() lag")
    result = db.query(lagsql)
    result = result[0]  # .isoformat()  # [0][0]
    payload = f"t: {result[0]} lag: {result[1]}"
    print(payload)
    logging.info(payload)


if __name__ == "__main__":
    main()
