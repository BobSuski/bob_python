class Vehicle(object):

    def __init__(self,vin=None, model=None):
        self.vin=vin
        self.model=model

    def __str__(self):
        return(f'vin={self.vin}, model={self.model}')
