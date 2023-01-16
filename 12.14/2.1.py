#мост
from abc import ABC, abstractmethod
# Пассажирские и грузовые  
 
class Carrier(ABC): 
    @abstractmethod
    def carry_military(self, items): 
        pass 
        
    @abstractmethod
    def carry_commercial(self, items): 
        pass 
 
class Cargo(Carrier): 
    def carry_military(self, items): 
        print("The plane carries ", items," military cargo") 
 
    def carry_commercial(self, items): 
        print("The plane carries ", items," commercial cargo") 
 
class Passenger(Carrier): 
    def carry_military(self, passengers): 
        print("The plane carries ", passengers , " military passengers") 
 
    def carry_commercial(self, passengers): 
        print("The plane carries ", passengers , " commercial passengers") 
 
 # военные и комерческие самолеты 
class Plane(ABC): 
    def __init__(self, Carrier): 
        self.carrier = Carrier 
    @abstractmethod
    def display_description(self): 
        pass 
    @abstractmethod
    def add_objects(self): 
        pass 
 
class Commercial(Plane): 
    def __init__(self, Carrier, objects): 
        super().__init__(Carrier) 
        self.objects = objects 
 
    def display_description(self): 
        self.carrier.carry_commercial(self.objects) 
 
    def add_objects(self, new_objects): 
        self.objects += new_objects 

class Military(Plane): 
    def __init__(self, Carrier, objects): 
        super().__init__(Carrier) 
        self.objects = objects 
 
    def display_description(self): 
        self.carrier.carry_military(self.objects) 
 
    def add_objects(self, new_objects): 
        self.objects += new_objects 


cargo = Cargo() 
passenger = Passenger() 
 
 # военный и груз
military1 = Military(cargo , 123) 
military1.display_description() 
military1.add_objects(12) 
military1.display_description()

