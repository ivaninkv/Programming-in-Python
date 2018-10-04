import os
import csv

class BaseCar:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def __str__(self):
        return(f'{self.car_type} - {self.brand}, {self.carrying}')

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(BaseCar):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):        
        super(Car, self).__init__(car_type, brand, photo_file_name, carrying)
        self.car_type = car_type
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(BaseCar):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super(Truck, self).__init__(car_type, brand, photo_file_name, carrying)
        self.car_type = car_type
        self.body_width = float(body_whl.split('x')[0]) if len(body_whl) > 0 else 0.
        self.body_height = float(body_whl.split('x')[1]) if len(body_whl) > 0 else 0.
        self.body_length = float(body_whl.split('x')[2]) if len(body_whl) > 0 else 0.

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(BaseCar):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(car_type, brand, photo_file_name, carrying)
        self.car_type = car_type
        self.extra = extra



def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) == 7:
                car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
                if car_type == 'car':                    
                    car_list.append(Car(car_type, brand, photo_file_name, carrying, passenger_seats_count))
                elif car_type == 'truck':                    
                    car_list.append(Truck(car_type, brand, photo_file_name, carrying, body_whl))
                elif car_type == 'spec_machine':                    
                    car_list.append(SpecMachine(car_type, brand, photo_file_name, carrying, extra))
    return car_list

def main():
    # car = Truck('truck', 'volvo', '/tmp/photo.jpg', '111', '1x2x3')
    # print(car.body_width, car.body_height, car.body_length)
    cl = get_car_list('coursera_week3_cars.csv')
    for c in cl:
        print(c)
    

if __name__ == '__main__':
    main()
    