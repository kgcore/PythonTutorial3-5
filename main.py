# import the modules
import datetime
from random import randint
now = datetime.datetime.now()


"""print("Here/'s a picture of a dog")
print('o----') 
print('||||')
endDate = 2025

# born = int(input('What year were you born? '))
born = 1969

age = endDate - born

dogAge = (now.year - born) * 7

print('In ' + str(endDate) + ' You\'ll be ' + str(age) + ' years old!')
print('Also, you will be ' + str(age * 7) + " in dog years!")
print('Today you are ' + str(dogAge) + ' in dog years!')

print("ha" + " !" * 4)
"""
while True:
    player = input('fire(f) logs(l) water(w)? ').lower()
    if player in ('f', 'l', 'w'):
        break
    print('You entered ' + player + ' not f, l or w')

print(player, 'vs', end=' ')
chosen = randint(1, 3)
# print('Computer ' + str(chosen))
if chosen == 1:
    computer = 'f'
elif chosen == 2:
    computer = 'l'
else:
    computer = 'w'

print('Computer ' + computer)

message = list()

message.append('fire burns logs you idiot')
message.append('logs make a bridge over water')
message.append('water puts out a fire you idiot')

if player == computer:
    print("DRAW!!!")
elif player == 'f' and computer == 'l':
    print('Player wins ' + message[0] + '!!!')
elif player == 'l' and computer == 'f':
    print('Computer wins ' + message[0] + '!!!')
elif player == 'l' and computer == 'w':
    print('Player wins ' + message[1] + '!!!')
elif player == 'w' and computer == 'l':
    print('Computer wins ' + message[1] + '!!!')
elif player == 'w' and computer == 'f':
    print('Player wins ' + message[2] + '!!!')
else:
    print('Computer wins ' + message[2] + '!!!')
    