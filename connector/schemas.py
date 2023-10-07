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

AGGR_TRADE = '''
        CREATE TABLE IF NOT EXISTS <|name|> (
            local_ts    TIMESTAMP,
            exchange_ts TIMESTAMP,
            symbol      STRING,
            aggr_id     LONG,
            price       DOUBLE,
            volume      DOUBLE,
            first_id    LONG,
            last_id     LONG,
            trade_ts    TIMESTAMP,
            mm          BOOLEAN,
            ignore      BOOLEAN
        ) timestamp(local_ts);
        '''

AGGR_TRADE = '''
        CREATE TABLE IF NOT EXISTS <|name|> (
            local_ts    TIMESTAMP,
            exchange_ts TIMESTAMP,
            symbol      STRING,
            aggr_id     LONG,
            price       DOUBLE,
            volume      DOUBLE,
            first_id    LONG,
            last_id     LONG,
            trade_ts    TIMESTAMP,
            mm          BOOLEAN,
            ignore      BOOLEAN
        ) timestamp(local_ts);
        '''

ORDER_BOOK = '''
        CREATE TABLE IF NOT EXISTS <|name|> (
            local_ts    TIMESTAMP,
            last_id     LONG,

            bids_p_01     DOUBLE,
            bids_q_01     DOUBLE,
            bids_p_02     DOUBLE,
            bids_q_02     DOUBLE,
            bids_p_03     DOUBLE,
            bids_q_03     DOUBLE,
            bids_p_04     DOUBLE,
            bids_q_04     DOUBLE,
            bids_p_05     DOUBLE,
            bids_q_05     DOUBLE,
            bids_p_06     DOUBLE,
            bids_q_06     DOUBLE,
            bids_p_07     DOUBLE,
            bids_q_07     DOUBLE,
            bids_p_08     DOUBLE,
            bids_q_08     DOUBLE,
            bids_p_09     DOUBLE,
            bids_q_09     DOUBLE,
            bids_p_10     DOUBLE,
            bids_q_10     DOUBLE,
            bids_p_11     DOUBLE,
            bids_q_11     DOUBLE,
            bids_p_12     DOUBLE,
            bids_q_12     DOUBLE,
            bids_p_13     DOUBLE,
            bids_q_13     DOUBLE,
            bids_p_14     DOUBLE,
            bids_q_14     DOUBLE,
            bids_p_15     DOUBLE,
            bids_q_15     DOUBLE,

            asks_p_01     DOUBLE,
            asks_q_01     DOUBLE,
            asks_p_02     DOUBLE,
            asks_q_02     DOUBLE,
            asks_p_03     DOUBLE,
            asks_q_03     DOUBLE,
            asks_p_04     DOUBLE,
            asks_q_04     DOUBLE,
            asks_p_05     DOUBLE,
            asks_q_05     DOUBLE,
            asks_p_06     DOUBLE,
            asks_q_06     DOUBLE,
            asks_p_07     DOUBLE,
            asks_q_07     DOUBLE,
            asks_p_08     DOUBLE,
            asks_q_08     DOUBLE,
            asks_p_09     DOUBLE,
            asks_q_09     DOUBLE,
            asks_p_10     DOUBLE,
            asks_q_10     DOUBLE,
            asks_p_11     DOUBLE,
            asks_q_11     DOUBLE,
            asks_p_12     DOUBLE,
            asks_q_12     DOUBLE,
            asks_p_13     DOUBLE,
            asks_q_13     DOUBLE,
            asks_p_14     DOUBLE,
            asks_q_14     DOUBLE,
            asks_p_15     DOUBLE,
            asks_q_15     DOUBLE

        ) timestamp(local_ts);
        '''