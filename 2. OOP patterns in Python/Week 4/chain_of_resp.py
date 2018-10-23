

class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__ (self , kind):
        self.kind = kind


class EventSet:
    def __init__(self, value):
        self.value = value


class NullHandler:
    def __init__ (self, successor=None):        
        self.__successor = successor

    def handle (self, obj, event): 
        if self.__successor is not None:
            return self.__successor.handle (obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if event.kind == int:
                return obj.integer_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value, int):
                obj.integer_field = event.value
            else:
                super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if event.kind == float:
                return obj.float_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value, float):
                obj.float_field = event.value
            else:
                super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if event.kind == str:
                return obj.string_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value, str):
                obj.string_field = event.value
            else:
                super().handle(obj, event)


def main():
    obj = SomeObject()
    chain = IntHandler(FloatHandler(StrHandler(NullHandler())))
    chain.handle(obj, EventSet(111))
    chain.handle(obj, EventSet(11.1))
    chain.handle(obj, EventSet('str'))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))


if __name__ == '__main__':
    main()