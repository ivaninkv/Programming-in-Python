class Value:
    def __init__(self):
        self.value = None
    
    @staticmethod
    def _prepare_value(obj, value):
        return int(value - value * obj.commission)

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(obj, value)

class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission


def main():
    new_acc = Account(0.1)
    new_acc.amount = 100
    print(new_acc.amount)

if __name__ == '__main__':
    main()        