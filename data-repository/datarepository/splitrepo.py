import datetime
from repobase import MysqlConnection

def refresh_split(symbol, splits):

    ins = "INSERT INTO `market.split` (`symbol`, `exdate`, `declare_date`, `record_date`, `payment_date`, `ratio`, `to_factor`, `for_factor`) \
           VALUES (`{}`, %(exDate)s, %(declareDate)s, %(recordDate)s, %(paymentDate)s, %(ratio)s, %(toFactor)s, %(forFactor)s) \
           ON DUPLICATE KEY UPDATE \
           `declare_date`=%(declareDate)s, `record_date`=%(recordDate)s, `payment_date`=%(paymentDate)s, \
           `ratio`=%(ratio)s, `to_factor`=%(toFactor)s, `for_factor`=%(forFactor)s" \
           .format(symbol)

    clr = "DELETE FROM `market.split` WHERE symbol='{}'".format(symbol)

    with MysqlConnection() as cnx:
        cur = cnx.cursor()

        # clear current record
        cur.execute(clr)
        cnx.commit()

        # insert from the list
        for row in splits:
            # put effective date to query
            cur.execute(ins, row)
            
        cnx.commit()
        cur.close()

    pass
