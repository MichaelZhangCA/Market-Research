import appconfig
from repobase import MysqlConnection
from emailhelper import EmailHelper
from logger import Logger

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

    Logger.init_logger(appconfig.environment['env'], 'Aanlysis')
