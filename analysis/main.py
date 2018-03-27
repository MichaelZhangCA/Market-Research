from crossreference import *
from emailhelper import EmailHelper 
from gmailhelper import GmailHelper
import appinit

def main():
    appinit.app_init()

    with GmailHelper() as eh:
        eh.sendemail('test email','from my home email server')
        print('email sent')
    pass    

if (__name__ == '__main__'):
    main()
