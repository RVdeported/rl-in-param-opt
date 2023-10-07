import psycopg as pg
import time
from schemas import KLINES, DEPTH_DIFF
import json

# Connect to an existing QuestDB instance

class FinQuestDB:
    def __init__(self,
                 symbols  : list,
                 conn_str : str='user=admin password=quest host=127.0.0.1 port=8812 dbname=qdb',
                 ):
        
        self.symbols = symbols
        self.conn_str = conn_str
        self.create_tables()
    
    def insert(self, item):
        if item[0]["e"] == "kline":
            self.insert_klines(item)
        if item[0]["e"] == "depthUpdate":
            print("!!!! RECORDING INTERNAL!!!")
            self.insert_depth_diff(item)

    def insert_depth_diff(self, item):
        with pg.connect(self.conn_str, autocommit=True) as connection:
            with connection.cursor() as cur:
                timestamp = time.time_ns() // 1000
                args = []
                for n in item:
                    args.extend(
                        [                        
                        timestamp,
                        n["E"]*1000,
                        n["s"],
                        n["U"],
                        n["u"],
                        json.dumps(n["b"]),
                        json.dumps(n["a"])
                        ]
                    )
                print(args)
                cur.execute(f"""
                    INSERT INTO {self.compose_name("DEPTH_D", item[0]["s"])}
                        VALUES {('(%s, %s, %s, %s, %s, %s, %s),' * len(item))[:-1]};
                    """, args)
                
    def insert_klines(self, item):

        with pg.connect(self.conn_str, autocommit=True) as connection:
            with connection.cursor() as cur:
                timestamp = time.time_ns() // 1000
                args = []
                for n in item:
                    args.extend(
                        [                        timestamp,
                        n["E"]*1000,
                        n["s"],
                        n["k"]["t"]*1000,
                        n["k"]["T"]*1000,
                        n["k"]["i"],
                        n["k"]["f"],
                        n["k"]["L"],
                        n["k"]["o"],
                        n["k"]["c"],
                        n["k"]["h"],
                        n["k"]["l"],
                        n["k"]["v"],
                        n["k"]["n"],
                        "True" if n["k"]["x"] else "False"]
                    )

                cur.execute(f"""
                    INSERT INTO {self.compose_name("KLINES", item[0]["s"])}
                        VALUES {('(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s),' * len(item))[:-1]};
                    """, args)

    def compose_name(self, type="KLINES", symbol="BTCUSDT"):
        return symbol + "_" + type + "_BINANCE"

    def create_tables(self):
        with pg.connect(self.conn_str, autocommit=True) as connection:
            
            
            with connection.cursor() as cur:

                # klines tables
                for symbol in self.symbols:
                    cur.execute(KLINES.replace("<|name|>"    , self.compose_name("KLINES",  symbol)))
                    cur.execute(DEPTH_DIFF.replace("<|name|>", self.compose_name("DEPTH_D", symbol)))
                
                # depth table
                


if __name__ == "__main__":
    db = FinQuestDB("BUSDT")
    db.create_tables()


# with pg.connect(conn_str, autocommit=True) as connection:

#     # Open a cursor to perform database operations

#     with connection.cursor() as cur:

#         # Execute a command: this creates a new table

#         cur.execute('''
#           CREATE TABLE IF NOT EXISTS test_pg (
#               ts TIMESTAMP,
#               name STRING,
#               value INT
#           ) timestamp(ts);
#           ''')

#         print('Table created.')

#         # Insert data into the table.

#         for x in range(10):

#             # Converting datetime into millisecond for QuestDB

#             timestamp = time.time_ns() // 1000

#             cur.execute('''
#                 INSERT INTO test_pg
#                     VALUES (%s, %s, %s);
#                 ''',
#                 (timestamp, 'python example', x))

#         print('Rows inserted.')

#         #Query the database and obtain data as Python objects.

#         cur.execute('SELECT * FROM test_pg;')
#         records = cur.fetchall()
#         for row in records:
#             print(row)

# the connection is now closed
