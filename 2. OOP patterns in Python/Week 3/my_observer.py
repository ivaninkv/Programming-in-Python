from abc import ABC, abstractmethod

class Engine:
    pass


class ObservableEngine(Engine):
    def __init__(self):
         self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, achive:dict):
        for subscriber in self.__subscribers:
            subscriber.update(achive)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self):
        raise NotImplementedError


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achive:dict):
        self.achievements.add(achive['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, achive:dict):
        if achive not in self.achievements:
            self.achievements.append(achive)


def main():
    notify = {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}
    short = ShortNotificationPrinter()
    full = FullNotificationPrinter()
    obs_engine = ObservableEngine()
    obs_engine.subscribe(short)
    obs_engine.subscribe(full)
    obs_engine.notify(notify)

    print(short.achievements, full.achievements)


if __name__ == '__main__':
    main()