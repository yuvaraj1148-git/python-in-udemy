# it is a way to check a value with multiple  possible pattern
# same like nested elif 
# match-case = a cleaner way to handle many possible values

day = int(input('Enter a number:'))

match day:
    case 0:
        print('monday')
    case 1:
        print('Tuesday')
    case 2:
        print('Wednesday')
    case 3:
        print('Thursday')
    case 4:
        print('Friday')
    case 5:
        print('Saturady')
    case _ :
        print('Sunday')