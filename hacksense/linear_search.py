from guess import guess

for i in range(999):
    response = guess(i, 'cookies')
    print(i, response)
    if response == 'correct':
        print('code is: ', i)
        break

