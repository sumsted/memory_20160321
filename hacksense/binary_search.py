from guess import guess

MIN = 0
MAX = 999
MESSAGE = 'MEMPY!'


def binary_search():
    minimum = MIN
    maximum = MAX
    tries = 0
    while minimum <= maximum:
        tries += 1
        number = minimum + (maximum - minimum) // 2
        response = guess(number, MESSAGE)
        print(tries, maximum, minimum, number, response)
        if response == 'correct':
            break
        elif response == 'too low':
            minimum = number + 1
        elif response == 'too high':
            maximum = number - 1
    print(tries, number)


if __name__ == '__main__':
    binary_search()
