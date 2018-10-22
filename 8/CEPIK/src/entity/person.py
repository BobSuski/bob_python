class Person(object):

    def __init__(self,pesel=None, name=None, surname=None):
        self.pesel=pesel
        self.name=name
        self.surname=surname

    def __str__(self):
        return(f'pesel={self.pesel}, name={self.name}, surname={self.surname}')
