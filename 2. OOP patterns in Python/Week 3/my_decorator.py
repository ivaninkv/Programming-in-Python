from abc import ABC, abstractmethod


class Character:
    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass
    
    @abstractmethod
    def get_stats(self):
        pass


class Hero(Character):
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        
        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,
            
            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        } 
        
    def get_positive_effects(self):
        return self.positive_effects.copy()
    
    def get_negative_effects(self):
        return self.negative_effects.copy()
    
    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(ABC, Hero):
    @abstractmethod
    def get_positive_effects(self):
        raise NotImplementedError

    @abstractmethod
    def get_negative_effects(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_stats(self):
        raise NotImplementedError


class AbstractPositive(AbstractEffect):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        return self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        return self.base.get_stats()


class AbstractNegative(AbstractEffect):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        return self.base.get_negative_effects()

    @abstractmethod
    def get_stats(self):
        return self.base.get_stats()


class Berserk(AbstractPositive):
    def get_stats(self):
        result =  super().get_stats()
        result['HP'] += 50
        result['Strength'] += 7
        result['Endurance'] += 7
        result['Agility'] += 7
        result['Luck'] += 7

        result['Perception'] -= 3
        result['Charisma'] -= 3
        result['Intelligence'] -= 3

        return result

    def get_positive_effects(self):
        result = super().get_positive_effects()
        result.append(self.__class__.__name__)
        return result

    def get_negative_effects(self):
        return super().get_negative_effects()


class Blessing(AbstractPositive):
    def get_stats(self):
        result =  super().get_stats()        
        result['Strength'] += 2
        result['Endurance'] += 2
        result['Agility'] += 2
        result['Luck'] += 2
        result['Perception'] += 2
        result['Charisma'] += 2
        result['Intelligence'] += 2

        return result

    def get_positive_effects(self):
        result = super().get_positive_effects()
        result.append(self.__class__.__name__)
        return result

    def get_negative_effects(self):
        return super().get_negative_effects()


class Weakness(AbstractNegative):
    def get_stats(self):
        result =  super().get_stats()        
        result['Strength'] -= 4
        result['Endurance'] -= 4
        result['Agility'] -= 4

        return result

    def get_positive_effects(self):
        return super().get_positive_effects()

    def get_negative_effects(self):        
        result = super().get_negative_effects()
        result.append(self.__class__.__name__)
        return result


class EvilEye(AbstractNegative):
    def get_stats(self):
        result =  super().get_stats()        
        result['Luck'] -= 10

        return result

    def get_positive_effects(self):
        return super().get_positive_effects()

    def get_negative_effects(self):        
        result = super().get_negative_effects()
        result.append(self.__class__.__name__)
        return result        


class Curse(AbstractNegative):
    def get_stats(self):
        result =  super().get_stats()        
        result['Strength'] -= 2
        result['Endurance'] -= 2
        result['Agility'] -= 2
        result['Luck'] -= 2
        result['Perception'] -= 2
        result['Charisma'] -= 2
        result['Intelligence'] -= 2

        return result

    def get_positive_effects(self):
        return super().get_positive_effects()

    def get_negative_effects(self):        
        result = super().get_negative_effects()
        result.append(self.__class__.__name__)
        return result



def main():
    h = Hero()    
    print(h.get_stats())
    h = Berserk(h)
    print(h.get_stats())
    h = Blessing(h)
    print(h.get_stats())
    h = Curse(h)
    print(h.get_stats())
    print(h.get_positive_effects())
    print(h.get_negative_effects())
    print(h.get_stats())

if __name__ == '__main__':
    main()