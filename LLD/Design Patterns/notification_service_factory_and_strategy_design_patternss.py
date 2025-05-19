# Since here we have choices like which medium to send the notifications by, so we'll use strategy design pattern.
# Also, we'll need to create different strategy objects loosely, so we'll also need factory design pattern.
#
# Our components -
# NotificationStrategy interface with  send() method it it
# EmailNotification implementing NotificationStrategy interface
# SMSNotification implementing NotificationStrategy interface
# PushNotification implementing NotificationStrategy interface
# NotificationFactory Concrete class
# NotificationService Main driver class which will call factory, get strategy and call send() method on it
#
# Classes definitions-

from abc import ABC, abstractmethod


class NotificationStrategy(ABC):
    @abstractmethod
    def send(self, content):
        pass


class EmailNotification(NotificationStrategy):
    def send(self,content):
        return f"{content} sent via Email"


class SmsNotification(NotificationStrategy):
    def send(self,content):
        return f"{content} sent via SMS"


class PushNotification(NotificationStrategy):
    def send(self,content):
        return f"{content} sent via Push Notification"


class SlackNotification(NotificationStrategy):
    def send(self,content):
        return f"{content} sent via slack Notification"


class NotificationFactory:
    @staticmethod
    def getStrategy(medium):
        if medium == "email":
            return EmailNotification()
        elif medium == "sms":
            return SmsNotification()
        elif medium == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown Notification Medium {medium}. Use one of ['email', 'sms', 'push']")


class NotificationService:
    def sendNotification(self,medium, content):
        factory = NotificationFactory()
        try:
            strategy = factory.getStrategy(medium)
            print(strategy.send(content))
        except ValueError as e:
            print(e)


# Final Call from frontend-
service = NotificationService()
service.sendNotification('slack', "Hi How are you doing")
