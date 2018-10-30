import random
from abc import ABC

class AbstractLevel:
    @classmethod
    def get_map(cls):
        return cls.Map()

    @classmethod
    def get_objects(cls):
        return cls.Objects()
    
    class Map(ABC):
        pass

    class Objects(ABC):
        pass

class EasyLevel(AbstractLevel):  

    class Map:
        def __init__(self):
            self.map_ = [[0 for _ in range(5)] for _ in range(5)]
            for i in range(5):
                for j in range(5):
                    if i == 0 or j == 0 or i == 4 or j == 4:
                        self.map_[j][i] = -1  # граница карты
                    else:
                        # случайная характеристика области
                        self.map_[j][i] = random.randint(0, 2)

        def get_map(self):
            return self.map_

    
    class Objects:
        def __init__(self):
            # размещаем переход на след. уровень
            self.objects = [('next_lvl', (2, 2))]

        def get_objects(self, map_):
            # размещаем противников
            for obj_name in ['rat']:
                coord = (random.randint(1, 3), random.randint(1, 3))
                # ищем случайную свободную локацию
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 3), random.randint(1, 3))

                self.objects.append((obj_name, coord))

            return self.objects


class MediumLevel(AbstractLevel):
    
    class Map:
        def __init__(self):
            self.map_ = [[0 for _ in range(8)] for _ in range(8)]
            for i in range(8):
                for j in range(8):
                    if i == 0 or j == 0 or i == 7 or j == 7:
                        self.map_[j][i] = -1  # граница карты
                    else:
                        # случайная характеристика области
                        self.map_[j][i] = random.randint(0, 2)

        def get_map(self):
            return self.map_


    class Objects:
        def __init__(self):
            # размещаем переход на след. уровень
            self.objects = [('next_lvl', (4, 4))]

        def get_objects(self, map_):
            # размещаем врагов
            for obj_name in ['rat', 'snake']:
                coord = (random.randint(1, 6), random.randint(1, 6))
                # ищем случайную свободную локацию
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 6), random.randint(1, 6))

                self.objects.append((obj_name, coord))

            return self.objects


class HardLevel(AbstractLevel):

    class Map:
        def __init__(self):
            self.map_ = [[0 for _ in range(10)] for _ in range(10)]
            for i in range(10):
                for j in range(10):
                    if i == 0 or j == 0 or i == 9 or j == 9:
                        # граница карты
                        self.map_[j][i] = -1
                    else:
                        # характеристика области (-1 для непроходимой обл.)
                        self.map_[j][i] = random.randint(-1, 8)

        def get_map(self):
            return self.map_


    class Objects:
        def __init__(self):
            # размещаем переход на след. уровень
            self.objects = [('next_lvl', (5, 5))]

        def get_objects(self, map_):
            # размещаем врагов
            for obj_name in ['rat', 'snake']:
                coord = (random.randint(1, 8), random.randint(1, 8))
                # ищем случайную свободную локацию
                intersect = True
                while intersect:
                    intersect = False
                    # print(map_[coord[0]][coord[1]])
                    if map_.get_map()[coord[0]][coord[1]] == -1:
                        intersect = True
                        coord = (random.randint(1, 8), random.randint(1, 8))
                        continue
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 8), random.randint(1, 8))

                self.objects.append((obj_name, coord))

            return self.objects


# def main():
#     def create_level(factory):
#         return list((factory.get_map(), factory.get_objects()))

#     for factory in [EasyLevel, MediumLevel, HardLevel]:
#         level = create_level(factory)
#         # print(level)            
#         print(level[1].get_objects(level[0].get_map()))

#     hl = HardLevel()
#     hl.get_objects
#     hl.get_map()
    
# if __name__ == '__main__':
#     main()