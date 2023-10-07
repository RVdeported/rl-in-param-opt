KLINES = '''
                    CREATE TABLE IF NOT EXISTS <|name|> (
                        local_ts    TIMESTAMP,
                        exchange_ts TIMESTAMP,
                        symbol      STRING,
                        t_start     TIMESTAMP,
                        t_end       TIMESTAMP,
                        interval    STRING,
                        first_trade LONG,
                        end_trade   LONG,
                        open        DOUBLE,
                        close       DOUBLE,
                        high        DOUBLE,
                        low         DOUBLE,
                        volume      DOUBLE,
                        trades_num  INT,
                        kline_closed BOOLEAN
                    ) timestamp(local_ts);
                    '''
DEPTH_DIFF = '''
                    CREATE TABLE IF NOT EXISTS <|name|> (
                        local_ts    TIMESTAMP,
                        exchange_ts TIMESTAMP,
                        symbol      STRING,
                        first_u     LONG,
                        last_u      LONG,
                        bids_upd    STRING,
                        asks_upd    STRING
                    ) timestamp(local_ts);
                    '''