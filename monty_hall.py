#you are given the opportunity to select one closed door of three, behind one of which there is a prize. The other two doors hide “goats” (or some other such “non-prize”), or nothing at all. Once you have made your selection, Monty Hall will open one of the remaining doors, revealing that it does not contain the prize 2. He then asks you if you would like to switch your selection to the other unopened door, or stay with your original choice. Here is the problem:

#Disclaimer I am trying to do this without reading any solution 


#so if we repetedly do this experiment randomly then after sufficient number of iterations theoritical probablity should approach actual probablity.

#so after randomly arranging the boxes and selecting one and removing one wrong answer we can find the probablity of random answer being correct


import random


box=[1,2,1]           #1 is goat and 2 is car
iterr=int(input("Enter the number of iterations- "))
winner=0
lost=0


for i in range(iterr):
    k=box[:]
    random.shuffle(k)
    choice=random.randint(0,2)
    for p in range(3):
        if choice != p:
            if k[p] == 1:
                k[p] = 0
                break
#    print(k)
    if k[choice]==2:
        winner+=1
    if k[choice]==1:
        lost+=1

#print(lost)
#print(winner)
winner_ratio=winner/iterr
losing_ratio=lost/iterr
print("winning ratio",winner_ratio)
print("Losing ratio",losing_ratio)
