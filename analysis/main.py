from crossreference import *

from repobase import MysqlConnection
import analysis

serverName = "127.0.0.1"
userName = 'michael'
password = 'Password2017'
databaseName = 'stock_market'

def main():
    # set database connection info
    MysqlConnection.init_connection(serverName, databaseName, userName, password)
    
    analysis.process_jc_study('MSFT')

if (__name__ == '__main__'):
    main()
