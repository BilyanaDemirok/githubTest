days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# print(days[1])
for day in days:
    # print(days.index(day) + 1, day)
    print(f'{days.index(day) + 1} - {day}')
    if day == 'Sat' or day == 'Sun':
        print(' Weekend')

