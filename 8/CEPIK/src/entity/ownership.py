class Ownership(object):

    def __init__(self,name=None, surname=None):
        self.name=name
        self.surname=surname

    def __str__(self):
        return(f'name={self.name}, surname={self.surname}')
