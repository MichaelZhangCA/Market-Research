from crossreference import *

# import from common-lib project
import appvariable
# from repobase import MysqlConnection
# from emailhelper import EmailHelper
# from logger import Logger

import appconfig
from loader import process_symbollist, process_companyinfo, batchupdate_marketindices, process_symbol_historicprice, process_dividend, process_split

"""
def app_init():
    # load configuratino from ini file
    appconfig.init_appconfig()
    #print(appconfig.environment)

    # init Mysql database connection for all repositories
    MysqlConnection.init_connection(appconfig.mysql['server'], appconfig.mysql['database'], appconfig.mysql['user'], appconfig.mysql['password'])

    # init Email parameters
    EmailHelper.init_parameters(appconfig.environment['env'], appconfig.notification['smtpserver'], 
                               appconfig.notification['info_sender'], appconfig.notification['info_recipients'],
                               appconfig.notification['error_sender'], appconfig.notification['error_recipients'])

    Logger.init_logger(appconfig.environment['env'], 'CDS History Service')
"""

def main():

    appconfig.apply_common_config()
    print("Application initialized, start processing ...")

    # update the symbol list with latest data
    print(" -> Process symbol list")
    process_symbollist()
    
    # patch all new symbol's company data
    print(" -> Process company info")
    process_companyinfo()

    # update market indicies
    print(" -> Process index constituent")
    batchupdate_marketindices()

    # refreh dividend list
    print(' -> Process dividend list')
    process_dividend()

    # refreh split list
    print(' -> Process split list')
    process_split()

    # load index live symbol historic data
    print('')
    print(" -> Process history stock price")
    process_symbol_historicprice()

    print('')
    print(" -> 2nd run for rocessing history stock price")
    process_symbol_historicprice()

if (__name__ == '__main__'):
    main()
