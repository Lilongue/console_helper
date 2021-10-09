"""
Строка документации класса
"""
import json
import  sys
import os

class DataExplore():
    """
    Строка документации класса
    """
    def __init__(self, path='store.log'):
        self.path = path
        assert os.path.exists(self.path), "Файл не существует"
        self.data = self.read_data()
        assert isinstance(self.data, dict), "Данные не соответствуют ожидаемому формату"
        
    def read_data(self):
        """
        Строка документации метода read_data
        """
        with open(self.path, 'r') as fp:
            return json.load(fp)
    
    def save_data(self, path=None):
        """
        Строка документации метода save_data
        """
        if path:
            self.path = path
        with open(self.path, 'w') as fp:
            json.dump(self.data, fp)
        
    def del_record(self, name):
        """
        Строка документации метода del_record
        """
        return  self.data.pop(name, defoult=None)
        
    def add_record(self, name, record):
        """
        Строка документации метода add_record
        """
        self.data[name] = record
        
    def view_record(self, name):
        """
        Строка документации метода view_record
        """
        return self.data.get(name)
        
    def view_records(self):
        """
        Строка документации метода view_records
        """
        return self.data.keys()
