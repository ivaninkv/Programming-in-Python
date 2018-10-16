from abc import ABC, abstractmethod


class Character(ABC):
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


class AbstractEffect(Hero):
    def __init__(self, base):
        self.base = base

    def get_positive_effects(self):
        self.base.get_positive_effects()

    def get_negative_effects(self):
        self.base.get_negative_effects()

    def get_stats(self):
        self.get_stats()


class AbstractPositive(AbstractEffect):
    pass


class AbstractNegative(AbstractEffect):
    pass


class Berserk(AbstractPositive):
    pass


class Blessing(AbstractPositive):
    pass


class Weakness(AbstractNegative):
    pass


class EvilEye(AbstractNegative):
    pass


class Curse(AbstractNegative):
    pass