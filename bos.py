test_age = int(input('Enter your age: '))

if test_age < 11:
    print('Passengers younger than 11 do not require a test')
else:
    print('Passengers older than 11 require a Covid test')

test_result = input('Insert the result you see on the device: ').lower()
print('Your test result is:', test_result)

if test_result == 'positive':
    print('Unfortunately, you have to self-isolate for 10 days.')

if test_result == 'negative':
    print('You can travel')


