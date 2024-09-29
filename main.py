with open('files.txt') as the_file:
    i=1
    for lines in the_file:
        print('{} {}'.format(i,lines))
        i=i+1
    print(i,lines)
    print(i,lines)
import time
print(time.asctime())
print(time.timezone)

from time import asctime
print(asctime())

from time import asctime, sleep
print(asctime())
sleep(5)
print(asctime())

import sys
for path in sys.path:
    print(path)

def cat_say(text):
    text_length = len(text)
    print(' {}'.format('_' * text_length))
    print(' < {} >'.format(text))
    print(' {}'.format('-' * text_length))
    print(' /')
    print(' /\_/\ /')
    print('( o.o )')
    print(' > ^ <')

def main():
    text=('what say')
    cat_say(text)
if __name__=='__main__':
    main()

cph=0.51
cpd=24*cph
cpm=30*cpd
print('amount is{:.2f}'.format(cpd))
print('amount {:.2f}'.format(cpm))

distance=input('how far will u go')
distance=int(distance)
if distance < 3:
    modeoftransport= 'walking'
elif distance < 300:
    modeoftransport= 'driving'
else :
    modeoftransport='flying'
print('i sugest {} to your destination'.format(modeoftransport))
 

airport=[("O’Hare International Airport" ,'ORD') ,
         ('Los Angeles International Airport',' LAX'),
         ('Dallas/Fort Worth International Airport','DFW'), 
         ('Denver International Airport', 'DEN')
          ]
for (airport, code) in airport:
    print('this {} is {}'.format(airport,code))