from datetime import datetime

class Notification():
    def __init__(self, message):
        self.message = message
        self.created_at = datetime.now()

    def send(self):
        print(self.message)

    def __str__(self):
        return self.message


class EmailNotification(Notification):
    def send(self):
        print(f"Email gönderildi: {self.message}")

class SMSNotification(Notification):
    def send(self):
        print(f"SMS gönderildi: {self.message}")

class PushNotification(Notification):
    def send(self):
        print(f"Push Notification: {self.message}")