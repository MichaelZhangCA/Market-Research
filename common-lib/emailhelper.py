# Import smtplib for the actual sending function
import smtplib

# Here are the email package modules we'll need
# from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailHelper(object):

    '''
    env = "DEV"
    smtpserver = "mail.hoopp.com"
    info_sender = 'quant.info@hoopp.com'
    error_sender = 'quant.alert@hoopp.com'
    info_recipients =  ["mzhang@hoopp.com"]	#, "isg-quant@hoopp.com"]
    error_recipients =  ["mzhang@hoopp.com", "isg-quant@hoopp.com"]
    '''

    # some predefined parameters
    env = ""
    smtpserver = "mail.hoopp.com"
    info_sender = ''
    error_sender = ''
    info_recipients =  []
    error_recipients =  []

    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @staticmethod
    def init_paramters(env, smtp, infosender, inforecipients, errorsender, errorrecipients):
        """ have to explicit change the Class varibles, otherwise Python will automatically create new variables """
        EmailHelper.env = env
        EmailHelper.smtpserver = smtp
        EmailHelper.info_sender = infosender
        EmailHelper.info_recipients = inforecipients
        EmailHelper.error_sender = errorsender
        EmailHelper.error_recipients = errorrecipients


    def __sendemail(self, sender, recipients, priotiry, title, message):
        # Create the container (outer) email message.
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        msg['X-Priority'] = priotiry
        msg['Subject'] = title
        msg.attach(MIMEText(message))

        # Assume we know that the image files are all in PNG format
        """
        for file in pngfiles:
            # Open the files in binary mode.  Let the MIMEImage class automatically guess the specific image type.
            with open(file, 'rb') as fp:
                img = MIMEImage(fp.read())
            msg.attach(img)
        """

        # Send the email via our own SMTP server.
        s = smtplib.SMTP(self.smtpserver)
        s.sendmail(sender, recipients, msg.as_string())
        s.quit()

    def sendinfo(self, title, msg):
        self.__sendemail(self.info_sender, self.info_recipients, '0', self.env + " - Info -" + title, msg )

    def sendalert(self, title, msg):
        self.__sendemail(self.error_sender, self.error_recipients, '1', self.env + " - Alert - " + title, msg )

