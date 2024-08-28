from flask_mail import Mail, Message
from flask import current_app as app

class MailConfig:
    def __init__(self,app):
        self.app = app
        self.mail = Mail(self.app)
    def setup_mail(self):
        self.app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        self.app.config['MAIL_PORT'] = 587
        self.app.config['MAIL_USE_TLS'] = True
        self.app.config['MAIL_USE_SSL'] = False
        self.app.config['MAIL_USERNAME'] = 'rajashri26chhatrikar@gmail.com'  # Your email
        self.app.config['MAIL_PASSWORD'] = 'oneq tdmt cuph wikm'  # Your email password or app-specific password
        self.app.config['MAIL_DEFAULT_SENDER'] = 'rajashri26chhatrikar@gmail.com'


class MailServer:
    def __init__(self):
        self.mail = Mail(app)
        self.app = app

    def send_mail(self, email, bodylink):
        msg = Message(
            subject="Course Link",
            body=f"Join the course using the following link: {bodylink}",
            recipients=[email]  # Replace with the recipient's email
        )
        try:
            self.mail.send(msg)
            return "Mail sent successfully"
        except Exception as e:
            self.app.logger.error(f"Failed to send mail: {str(e)}")
            return f"Failed to send mail: {str(e)}"