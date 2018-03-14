import datetime
from repobase import MysqlConnection

def refresh_dividend(symbol, dividends):

    ins = "INSERT INTO `market.dividend` \
            (`symbol`, `exdate`, `payment_date`, `record_date`, `declared_date`, `amount`, `flag`, `devidend_type`, `qualified`, `indicated`) \
           VALUES \
            ('{}', %(exDate)s, %(paymentDate)s, %(recordDate)s, %(declaredDate)s, %(amount)s, %(flag)s, %(type)s, %(qualified)s, %(indicated)s) \
            ON DUPLICATE KEY UPDATE \
            `payment_date` = %(paymentDate)s, `record_date`=%(recordDate)s, `declared_date`=%(declaredDate)s, \
            `amount`=%(amount)s, `flag`=%(flag)s, `devidend_type`=%(type)s, `qualified`=%(qualified)s, `indicated`=%(indicated)s" \
           .format(symbol)

    clr = "DELETE FROM `market.dividend` WHERE symbol='{}'".format(symbol)

    with MysqlConnection() as cnx:
        cur = cnx.cursor()

        # clear current record
        cur.execute(clr)
        cnx.commit()

        # insert from the list
        for row in dividends:
            if (row['declaredDate']==''):
                row['declaredDate'] = None
            if (row['recordDate']==''):
                row['recordDate'] = None
            if (row['amount']==''):
                row['amount'] = None

            # put effective date to query
            cur.execute(ins, row)
                
        cnx.commit()
        cur.close()

    pass
