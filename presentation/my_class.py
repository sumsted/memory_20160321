SOME_CONSTANT = 4


class MyClass():
    def __init__(self, some_number):
        self._some_number = some_number
        self._a_name = None

    def do_something(self, some_other_number, a_name):
        self._a_name = a_name
        return self._some_number + some_other_number

    def greet(self):
        return 'Hello ' + self._a_name


def start():
    my_object = MyClass(123)
    print(my_object.do_something(321, 'Bob'))
    print(my_object.greet())


if __name__ == '__main__':
    start()