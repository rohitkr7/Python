class Person(object):
    def __init__(self,name):
        self.name = name
    
    def reveal_identity(self):
        print("My name is {}".format(self.name))
    

class SuperHero(Person):
    def __init__(self, name, hero_Name):
        super(SuperHero, self).__init__(name)
        self.hero_Name = hero_Name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("... and i am {}".format(self.hero_Name))


rohit = Person("Rohit")
rohit.reveal_identity()


wade = SuperHero('Wade Wilson', 'Deadpool')
wade.reveal_identity()