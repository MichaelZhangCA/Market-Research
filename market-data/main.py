from crossreference import *

# import from common-lib project
import appvariable
from repobase import MysqlConnection
from emailhelper import EmailHelper
from logger import Logger

import appconfig
from loader import refresh_symbollist, update_companyinfo, batchupdate_marketindices, dump_symbolhistoricdata

def app_init():
    # load configuratino from ini file
    appconfig.init_appconfig()
    #print(appconfig.environment)

    # init Mysql database connection for all repositories
    MysqlConnection.init_connection(appconfig.mysql['server'], appconfig.mysql['database'], appconfig.mysql['user'], appconfig.mysql['password'])

    # init Email parameters
    EmailHelper.init_paramters(appconfig.environment['env'], appconfig.notification['smtpserver'], 
                               appconfig.notification['info_sender'], appconfig.notification['info_recipients'],
                               appconfig.notification['error_sender'], appconfig.notification['error_recipients'])

    Logger.init_logger(appconfig.environment['env'], 'CDS History Service')


def main():

    app_init()
    
    # update the symbol list with latest data
    refresh_symbollist()
    print("Symbol list updated")
    
    # patch all new symbol's company data
    update_companyinfo()
    print("Company info updated")

    # update market indicies
    batchupdate_marketindices()
    print("Index constituent updated")

    # load index live symbol list
    dump_symbolhistoricdata()
    print("")
    print("History data updated")

if (__name__ == '__main__'):
    main()
