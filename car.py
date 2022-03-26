class car():

    def __init__(self, name):
        self.name = name

    def rides_forward(self):
        return(self.name + 'едит вперёд')

    def drift_to_the_right(self):
        return(self.name + 'дрефтит на право')

    def drift_to_the_left(self):
        return(self.name + 'дрефтит на лево')

    def Vanya_is_lucky_in_karate(self):
        return(self.name + 'везет ваню на карате')

car1 = car('Tesla ')

