from abc import ABC, abstractmethod

class DAOInterface(ABC):
    @abstractmethod
    def get_all_data(self):
        pass

    @abstractmethod
    def print(self, data):
        pass

    @abstractmethod
    def search(self,  mode, field, value):
        pass

    @abstractmethod
    def delete(self,  mode, field, value):
        pass

    @abstractmethod
    def count(self,database_path, mode, field, value):
        pass

    @abstractmethod
    def add(self,  row):
        pass

    @abstractmethod
    def update(self, mode, search_field, search_value, change_field, change_val):
        pass