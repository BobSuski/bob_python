class Shape(object):

    def __init__(self,name=None,width=None,height=None):
            self.name=name
            self.width=width
            self.height=height

    def __str__(self):
        return f'{self.name} with {self.height}x{self.width}'

    def __eq__(self, other):
        return self.height==other.height



    pass