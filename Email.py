from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email.mime.application
import smtplib

import config


def send(subject, message, to, filename=None):
        
    mime_message = MIMEText(message, "plain")
    mime_message["From"] = 'Agrofruta <'+config.user+'>'
    mime_message["To"] = to
    mime_message["Subject"] = subject

    if filename != None:
        mime_message = MIMEMultipart()
        mime_message["From"] = 'Agrofruta <'+config.user+'>'
        mime_message["To"] = to
        mime_message["Subject"] = subject

        fp=open(filename,'rb')
        att = email.mime.application.MIMEApplication(fp.read(),_subtype="json")
        fp.close()
        att.add_header('Content-Disposition','attachment',filename=filename)
        mime_message.attach(att)

    else:
        mime_message = MIMEText(message, "plain")
        mime_message["From"] = 'Agrofruta <'+config.user+'>'
        mime_message["To"] = to
        mime_message["Subject"] = subject
    
    try:
        server = smtplib.SMTP(config.smtp, 587)
        server.starttls()
        server.login(config.user, config.password)

        server.sendmail(config.user, to,  mime_message.as_string())
    except:
        print('error al enviar email')
        return False
    finally:
        server.quit()
    return True


#email.send('test de prueba 1', 'mesaje enviado desde python mediante smtplib', 'jaibarra1@miuandes.cl')