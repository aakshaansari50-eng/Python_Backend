class Notification:
    def send(self):
        print("Sending notification")

class EmailNotification(Notification):
    def send(self):
        super().send()
        print("Sending email notification")

class SMSNotification(Notification):
    def send(self):
        super().send()
        print("Sending SMS notification")

e = EmailNotification()
e.send()

s = SMSNotification()
s.send()