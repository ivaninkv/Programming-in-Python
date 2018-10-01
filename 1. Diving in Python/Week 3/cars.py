import os

class BaseCar:
    def __init__(self, brand, photo_file_name, carrying):
        # self.car_type = ''
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carryng = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):        
        super(Car, self).__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = passenger_seats_count


class Truck(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super(Truck, self).__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_width = float(body_whl.split('x')[0]) if len(body_whl) > 0 else 0
        self.body_height = float(body_whl.split('x')[1]) if len(body_whl) > 0 else 0
        self.body_length = float(body_whl.split('x')[2]) if len(body_whl) > 0 else 0


class SpecMachine(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra



def get_car_list(csv_filename):
    car_list = []
    return car_list

def main():
    car = Truck('volvo', '/tmp/photo.txt', '123', '1x2.5x3')    
    print(car.body_width, car.body_height, car.body_length)
    

if __name__ == '__main__':
    main()


