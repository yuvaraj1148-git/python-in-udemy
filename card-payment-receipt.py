# manual space
card = input('Enter your card number : ')

last = ""

for i in range(15,len(card)):
    last += card[i]

print('XXXX XXXX XXXX',last)

# automatic

card = input('ENTER A CARD NUMBER : ')
last = card[12:len(card)]
four = 'X'*4 + ' '
disp = four*3 + last
print(disp)

# automatic
card1 = input('Enter your first four digit : ')
card2 = input('Enter your second four digit : ')
card3 = input('Enter your third four digit : ')
card4 = input('Enter your fouth four digit : ')

card = card1 + ' ' + card2 + ' ' + card3 + ' ' + card4
last = ""

for i in range(15,len(card)):
    last += card[i]

print('XXXX XXXX XXXX',last)

Card_no = input('Enter a card number : ')
number = Card_no[12:17]
print('XXXX XXXX XXXX',number)