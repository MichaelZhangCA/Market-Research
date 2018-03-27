from configobj import ConfigObj

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
    'passowrd' : '',
    'recipients' :  []	#, "isg-quant@hoopp.com"]
    }

environment = {
    'env' : 'HOME',
    'servicename' : 'N/A'
    }

"""
called at the very beginning of application to load proper configration in to config class
"""
def init_appconfig():
    config = ConfigObj('.\\appconfig.ini')
    
    mysql['server'] = config['mysql']['servername']
    mysql['user'] = config['mysql']['username']
    mysql['password'] = config['mysql']['password']
    mysql['database'] = config['mysql']['databasename']

    notification['smtpserver'] = config['notification']['smtpserver']
    notification['info_sender'] = config['notification']['info_sender']
    notification['error_sender'] = config['notification']['error_sender']
    notification['info_recipients'] = list(set(config['notification']['info_recipients']))
    notification['error_recipients'] = list(set(config['notification']['error_recipients']))

    gmail['smtpserver'] = config['gmail']['smtpserver']
    gmail['sender'] = config['gmail']['sender']
    gmail['password'] = config['gmail']['password']
    gmail['recipients'] = list(set(config['gmail']['recipients']))

    environment['env'] = config['environment']['env']
    environment['servicename'] = config['environment']['servicename']

    pass
