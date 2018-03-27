# Import smtplib for the actual sending function
import smtplib
# Here are the email package modules we'll need
# from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class GmailHelper(object):

    smtpserver = "smtp.gmail.com"
    sender = 'symbol.notification@gmail.com'
    password = 'Tripal147'
    recipients =  ['michael.zh@gmail.com', 'mzhang@hoopp.com']

    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @staticmethod
    def init_parameters(user, password, recipients):
        GmailHelper.sender = user
        GmailHelper.password = password
        GmailHelper.recipients = recipients if type(recipients) is list else [recipients]


    def sendemail(self, title, message):
        # Create the container (outer) email message.
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.recipients)
        #msg['X-Priority'] = priotiry
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
        #try:
        # Send the email via our own SMTP server.
        s = smtplib.SMTP(self.smtpserver, 587)
        s.ehlo()
        s.starttls()
        s.login(self.sender, self.password)
        s.sendmail(self.sender, self.recipients, msg.as_string())
        s.close()
        #s.quit()
        #except:
        #    print('sent email failed')

    pass
