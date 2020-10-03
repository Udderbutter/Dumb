import random

Bowser_is_best = ['Did your mother Chris Brown you as a baby? You fucking retard?', 'Your opinion is shit', 'Ding dong your opinion is wrong', 'Fucking kill yourself', 'Listen here you clueless shit where the fuckdoyouliveiwillcometoyourfuckinghouserightnowa-',\
                  'Go fuck yourself', 'You were adopted', 'Nobody loves you', 'You will die alone', 'Stop breathing']
Time = 2
while True:
    x = input ('Who in the SSBM cast is most DOPE?').lower()
    if Time == 0:
      print ('You are helpless. Goodbye')
      break
    Time -=1
    if x == "":
        break
    if x == 'bowser':
        print ('MY MAN!')
        break
    elif x == 'falco':
        print ('You aight')
        break
    elif x == 'ice climbers':
        print ('This isnt even funny at this point like seriously just go dive off of a cliff you filthy fucking degenerate')
        break
    else:
        print (random.choice(Bowser_is_best))
