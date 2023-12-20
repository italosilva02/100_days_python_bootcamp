print('Welcome to the tip calculator.')

total_bill = float(input('What was the total bill?\n'))
tip = int(input('What percentage tip would you like to give? 10, 12 or 15?\n'))
people = int(input('How many people to split?\n'))

total = 0
if tip == 10:
    total = total_bill + (total_bill * 0.1)
elif tip == 12:
    total = total_bill + (total_bill * 0.12)
elif tip == 15:
    total = total_bill + (total_bill * 0.15)
else:
    print('Incorrect value ')

print(f'Your bill was U$ {total: .2f}')
print(f'Each person should pay U$ {total/people: .2f}')