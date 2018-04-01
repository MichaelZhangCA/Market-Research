from configobj import ConfigObj

from repobase import MysqlConnection
from emailhelper import EmailHelper
from gmailhelper import GmailHelper
from logger import Logger
import httphelper

# define global variables
mysql = {
    'server' : "",
    'user' : "",
    'password' : '',
    'database' : ''
    }


notification = {
    'smtpserver' : 'mail.gmail.com',
    'info_sender' : '',
    'error_sender' : '',
    'info_recipients' :  [],	#, "isg-quant@hoopp.com"]
    'error_recipients' :  []
    }

gmail = {
    'smtpserver' : 'mail.gmail.com',
    'sender' : '',
    'password' : '',
    'recipients' :  []	#, "isg-quant@hoopp.com"]
    }

environment = {
    'env' : 'HOME',
    'servicename' : 'N/A'
    }

http = {
    'ssl_verify' : True
    }

"""
called at the very beginning of application to load proper configration in to config class
"""
def __load_appconfig():
    config = ConfigObj('.\\appconfig.ini')
    
    if ('mysql' in config):
        mysql['server'] = config['mysql']['servername']
        mysql['user'] = config['mysql']['username']
        mysql['password'] = config['mysql']['password']
        mysql['database'] = config['mysql']['databasename']

    if ('notification' in config):
        notification['smtpserver'] = config['notification']['smtpserver']
        notification['info_sender'] = config['notification']['info_sender']
        notification['error_sender'] = config['notification']['error_sender']
        notification['info_recipients'] = list(set(config['notification']['info_recipients']))
        notification['error_recipients'] = list(set(config['notification']['error_recipients']))

    if ('gmail' in config):
        gmail['smtpserver'] = config['gmail']['smtpserver']
        gmail['sender'] = config['gmail']['sender']
        gmail['password'] = config['gmail']['password']
        gmail['recipients'] = list(set(config['gmail']['recipients']))

    if ('environment' in config):
        environment['env'] = config['environment']['env']
        environment['servicename'] = config['environment']['servicename']

    if ('http' in config):
        http['ssl_verify'] = config['http']['ssl_verify']

    pass


def apply_common_config():

    # load configuratino from ini file
    __load_appconfig()

    # init Mysql database connection for all repositories
    MysqlConnection.init_connection(mysql['server'], mysql['database'], mysql['user'], mysql['password'])

    # init Email parameters
    EmailHelper.init_parameters(environment['env'], notification['smtpserver'], 
                               notification['info_sender'], notification['info_recipients'],
                               notification['error_sender'], notification['error_recipients'])

    # Gmail
    GmailHelper.init_parameters(gmail['sender'], gmail['password'], gmail['recipients'])

    # logger
    Logger.init_logger(environment['env'], environment['servicename'])

    # http settings
    httphelper.ssl_verify = http['ssl_verify']
        