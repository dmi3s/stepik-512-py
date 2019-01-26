import time
from typing import List


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(List, Loggable):
    def append(self, obj):
        self.log(obj)
        List.append(self, obj)


def main():
    l = LoggableList()
    l.append(10)
    l.append(20)


if __name__ == '__main__':
    main()
