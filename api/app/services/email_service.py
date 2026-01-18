import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

from app.config import settings
from app.schemas.contact import ContactMessage

logger = logging.getLogger(__name__)


class EmailService:
    def __init__(self):
        self.smtp_host = settings.smtp_host
        self.smtp_port = settings.smtp_port
        self.smtp_user = settings.smtp_user
        self.smtp_password = settings.smtp_password
        self.email_from = settings.email_from

    async def send_contact_email(self, message: ContactMessage):
        """Envia email de contato"""
        if not self.smtp_user or not self.smtp_password:
            logger.warning("Email credentials not configured - skipping email send")
            return

        try:
            # Email para o admin
            admin_msg = MIMEMultipart('alternative')
            admin_msg['Subject'] = f"[Portfolio Contact] {message.subject or 'Nova mensagem'}"
            admin_msg['From'] = self.email_from
            admin_msg['To'] = self.email_from

            admin_html = f"""
            <html>
                <body>
                    <h2>Nova mensagem de contato</h2>
                    <p><strong>Nome:</strong> {message.name}</p>
                    <p><strong>Email:</strong> {message.email}</p>
                    {f'<p><strong>Telefone:</strong> {message.phone}</p>' if message.phone else ''}
                    <p><strong>Assunto:</strong> {message.subject or 'N/A'}</p>
                    <hr>
                    <h3>Mensagem:</h3>
                    <p>{message.message.replace(chr(10), '<br>')}</p>
                </body>
            </html>
            """

            admin_msg.attach(MIMEText(admin_html, 'html'))

            # Email de confirmação para o cliente
            client_msg = MIMEMultipart('alternative')
            client_msg['Subject'] = 'Mensagem recebida - Portfolio Gabriel Orellana'
            client_msg['From'] = self.email_from
            client_msg['To'] = message.email

            client_html = f"""
            <html>
                <body>
                    <h2>Olá {message.name}!</h2>
                    <p>Recebi sua mensagem e entrarei em contato em breve.</p>
                    <p>Obrigado pelo interesse!</p>
                    <hr>
                    <p><strong>Sua mensagem:</strong></p>
                    <p>{message.message.replace(chr(10), '<br>')}</p>
                    <br>
                    <p>Atenciosamente,<br>Gabriel Orellana</p>
                </body>
            </html>
            """

            client_msg.attach(MIMEText(client_html, 'html'))

            # Enviar emails
            async with aiosmtplib.SMTP(
                hostname=self.smtp_host,
                port=self.smtp_port,
                start_tls=True
            ) as smtp:
                await smtp.login(self.smtp_user, self.smtp_password)
                await smtp.send_message(admin_msg)
                await smtp.send_message(client_msg)

            logger.info(f"Contact email sent from {message.email}")

        except Exception as e:
            logger.error(f"Error sending email: {e}")
            raise
