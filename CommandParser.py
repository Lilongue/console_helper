"""
Строка документирования файла
"""
# Секция импорта
import pyperclip
import shelve
import sys

class Parser(object):
    """
    Класс для разбора параметров командной строки
    """
    pass

class RecordWork(object):
    """
    Для обслуживания записей
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            #cls._instance.__connection_string = connection_string
            return cls._instance
#        return super().__new__()
        return cls._instance
    
    def __connect():
        pass

    def __init__(self, connection_string) -> None:
        super().__init__()
        self.__connection_string = connection_string

    @property
    def Connection_string(self):
        return self.__connection_string

    

class ClipBoard(object):
    """
    Класс для работы с буфером обмена
    """
    pass

if __name__ == "__main__":
    print("At work")

