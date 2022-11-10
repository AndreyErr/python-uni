class main:
    def __init__(self):
        self.__state = 'A'

    def crawl(self):
        if self.__state == 'A':
            return 1
        raise KeyError

    def close(self):
        if self.__state == 'A':
            self.__state = 'B'
            return 0
        if self.__state == 'B':
            self.__state = 'F'
            return 5
        if self.__state == 'D':
            self.__state = 'E'
            return 7
        if self.__state == 'E':
            self.__state = 'F'
            return 8
        raise KeyError

    def exit(self):
        if self.__state == 'A':
            self.__state = 'F'
            return 2
        if self.__state == 'B':
            self.__state = 'C'
            return 4
        if self.__state == 'C':
            self.__state = 'D'
            return 6
        raise KeyError

    def slip(self):
        if self.__state == 'A':
            self.__state = 'D'
            return 3
        raise KeyError

    def getstate(self):
        return self.__state