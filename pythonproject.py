from random import randint
player=input('rock(r),paper(p) or scissor(s)?')
print('player choses',player)
chosen=randint(1,3)
#print(chosen)
if chosen==1:
    computer='r'
elif chosen==2:
    computer='p'
else:
    computer='s'
print('computer choses',computer)
print(player,'vs',end=' ')
chosen=randint(1,3)
#print(chosen)
print(computer)
if player==computer:
    print('draw!')
elif player=='r' and computer =='s':
    print('player wins')
elif player=='r' and computer =='p':
    print('computer wins')
elif player=='p' and computer=='s':
    print('computer wins')
elif player=='s' and computer =='r':
    print('computer wins')
elif player=='p' and computer =='r':
    print('player wins')
elif player=='s' and computer=='p':
    print('player wins')
elif player=='r' and computer=='p':
    print('player wins')
