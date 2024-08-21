
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Setup email notifier:
FROM_ADDR = "C:/Users/tharu/OneDrive/Desktop/blockathon/c3s.html"
password_file = "c3scal"  # File containing email password
send_alerts_to = ["tharun206abishek193@gmail.com"]  # Recipients

def send_alert(subject, body):
    """Prepare and send an alert message"""
    msg = MIMEMultipart()
    msg['From'] = FROM_ADDR
    msg['To'] = ", ".join(send_alerts_to)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('your.smtp.domain', 587)
    server.starttls()
    server.login(FROM_ADDR, open(password_file).read().strip())
    text = msg.as_string()
    server.sendmail(FROM_ADDR, send_alerts_to, text)
    server.quit()

# The following could be integrated into a CRON job for periodic execution
def observe_logs():
    """Regularly check web application logs for intrusions"""
    # Example of parsing Apache logs
    log_file = "/var/log/apache2/error.log"
    hack_alert_strings = ["possible break-in attempt", "unsuccessful authentication attempt"]

    for line in open(log_file):
        if any([alert_str in line for alert_str in hack_alert_strings]):
            send_alert("Intrusion Detected", "A suspicious activity was recorded at {0}".format(time.asctime()))
            
if __name__ == '__main__':
    observe_logs()