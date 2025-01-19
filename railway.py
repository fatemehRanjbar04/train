class Train:
    
    def __init__(self, last_visited_city, weight_capacity, is_on_trip):
        self.last_visited_city = last_visited_city
        self.weight_capacity = weight_capacity
        self.is_on_trip = is_on_trip


class Trip:

    all_cities = ('Arak', 'Ardabil', 'Urmia', 'Isfahan', 'Ahvaz', 'Ilam', 'Bojnord', 'Bandar Abbas', 'Bushehr', 'Birjand', 'Tabriz', 'Tehran', 'Khorramabad', 'Rasht', 'Zahedan', 'Zanjan', 'Sari', 'Semnan', 'Sanandaj', 'Shahr-e Kord', 'Shiraz', 'Qazvin', 'Qom', 'Karaj', 'Kermanshah', 'Gorgan', 'Mashhad', 'Hamadan', 'Yasuj', 'Yazd')

    def __init__(self, origin_city, destination_city, train):
        self.train = self.train_validation(train)
        self.destination_city = destination_city
        self.origin_city = self.origin_city_validation(origin_city)
        self.passengers = []
    
    def origin_city_validation(self, origin_city):

        if origin_city not in self.all_cities:
            raise ValueError("This input is not a verified city!")
        if origin_city == self.destination_city:
            raise ValueError("Origin and destination cities can't be the same!")
        if origin_city != self.train.last_visited_city:
            raise ValueError("The train of the trip is not available in the origin city!")
        else:
            return origin_city
        
        
    def train_validation(self, train):
        if not isinstance(train, Train):
            raise ValueError("This input is not a train!")
        if train.is_on_trip:
            raise ValueError("This train is not available!")
        else:
            return train

    def __call__(self):
        total_weight = sum([passenger.load_weight for passenger in self.passengers])
        remaining_capacity = self.train.weight_capacity - total_weight
        return remaining_capacity
    
class Passenger:

    def __init__(self, fullname, load_weight):
        self.fullname = fullname
        self.load_weight = load_weight
        
    def attend_trip(self, trip):
        
        remaining_capacity = trip()  
        if self.load_weight <= remaining_capacity:
            trip.passengers.append(self)
        else:
            raise ValueError("Heavy load!")

    def cancel_trip(self, trip):
        if self in trip.passengers:
            trip.passengers.remove(self)
        else:
            raise ValueError("This passenger is not attended to this trip!")

    def __str__(self):
        return self.fullname
    



#----------Test----------


# #ایجاد یک قطار با ظرفیت 1000 کیلوگرم و قطار آماده سفر نیست
train = Train(last_visited_city="Tehran", weight_capacity=1000, is_on_trip=False)

# # ایجاد یک سفر از تهران به مشهد
# trip = Trip(origin_city="Tehran", destination_city="Mashhad", train=train)

# # ایجاد مسافران
# passenger1 = Passenger(fullname="Ali", load_weight=300) 
# passenger2 = Passenger(fullname="Sara", load_weight=200) 
# passenger3 = Passenger(fullname="Mohammad", load_weight=600)  
# passenger4 = Passenger(fullname="Nadia", load_weight=150) 

# passenger1.attend_trip(trip)  
# passenger2.attend_trip(trip)  
# print("passengers in trip:", [str(p) for p in trip.passengers])
# print("remainig capacity:", trip())


