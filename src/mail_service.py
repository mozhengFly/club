import os
import smtplib
from email.mime.text import MIMEText


class MailService:
    """邮件发送服务，对应 Java MailService.sendSimpleMail。"""

    def __init__(
        self,
        smtp_host: str,
        smtp_username: str,
        smtp_password: str,
        smtp_port: int = 465,
        use_ssl: bool = True,
    ):
        if not smtp_host:
            raise ValueError("smtp_host 未配置，无法初始化 MailService")
        self._host = smtp_host
        self._port = smtp_port
        self._username = smtp_username
        self._password = smtp_password
        self._from = smtp_username
        self._use_ssl = use_ssl

    @classmethod
    def from_env(cls) -> "MailService":
        """从环境变量加载配置：SMTP_HOST, SMTP_USERNAME, SMTP_PASSWORD, SMTP_PORT, SMTP_USE_SSL"""
        return cls(
            smtp_host=os.getenv("SMTP_HOST", ""),
            smtp_username=os.getenv("SMTP_USERNAME", ""),
            smtp_password=os.getenv("SMTP_PASSWORD", ""),
            smtp_port=int(os.getenv("SMTP_PORT", "465")),
            use_ssl=os.getenv("SMTP_USE_SSL", "true").lower() in ("1", "true", "yes"),
        )

    def send_simple_mail(self, to: str, subject: str, content: str) -> None:
        """发送纯文本邮件，对应 Java sendSimpleMail。"""
        message = MIMEText(content, "plain", "utf-8")
        message["From"] = self._from
        message["To"] = to
        message["Subject"] = subject

        if self._use_ssl:
            with smtplib.SMTP_SSL(self._host, self._port) as server:
                server.login(self._username, self._password)
                server.sendmail(self._from, [to], message.as_string())
        else:
            with smtplib.SMTP(self._host, self._port) as server:
                server.starttls()
                server.login(self._username, self._password)
                server.sendmail(self._from, [to], message.as_string())
