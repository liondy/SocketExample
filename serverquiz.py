import numpy as np
from numpy.random import shuffle
from random import randint
import socket
import time
import select

#LIST OF QUESTIONS AND ANSWERS
question2 = ["What is the capital of France?","In which continent is Argentina?","Where is Big Ben?","What is the most densely populated country?","What language do they speak in Brazil?"]
answer2 = [["Paris","London","Berlin","Madrid"],
        ["South America","Africa","Europe","Asia"],
        ["London","New York","Mexico","Jakarta"],
        ["China","India","USA","Indonesia"],
        ["Portuguese","Spanish","French","English"]]
question_done=[0]*(len(question2))


#SCORE, stored as a list score[0]--> score of the player 1
score=[0]


#SHOW THE POSSIBLE ANSWERS
def displayA(question,answer,i):
    a = answer[i]
    order = np.arange(4)
    shuffle(order) #create list from 1 to 4 in different order --> to print the answers in random order
    a_display = [[a[order[0]],a[order[1]]],[a[order[2]],a[order[3]]]]
    print(a_display)


#CHOOSE RANDOMLY A QUESTION IN THE LIST
def chooseQuestion(question,answer):
    k = randint(0,len(question)-1)
    if (question_done[k]!=0):
        while(question_done[k]!=0):
            k = randint(0,len(question)-1)
        question_done[k]=1
    else :
        question_done[k]=1
    print(question[k])
    #displayA(question,answer,k)
    return k


#CHECK IF GOOD ANSWER OR NOT
def checkAnswer(answer,agiven,qnb):
    #print("CHECK")
    test = False
    if(answer[qnb][0] in agiven):
        test = True
        score[0]=score[0]+1
    #print("ANSWER")
    return test



#END OF GAME, DISPLAY OF SCORES
def final_score(score):
    print("The scores are {}".format(score))

    maxi = max(score)
    if(score.count(maxi)==1):
        print("The winner is Player {}".format(score.index(max(score))+1))
    else :
        winners = []
        for i in range(len(score)):
            if(score[i]==maxi):
                winners.append(i+1)
        print("The winners are players {}".format(winners))


"""
#Number of choosen questions, random order : GIVE THE QUESTION TO THE PLAYER
nb = 3

for k in range(nb):
nbq = chooseQuestion(question2,answer2)
agiven = raw_input("What is your answer?  ")
result = checkAnswer(answer2,agiven,nbq)
print("Your answer is {}".format(result))

#Say who the winner is
final_score(score)
"""
#START THE NETWORK CODE
#host = '192.168.26.86'
host = '127.0.0.1'

port = 4042

#list for all the players
players = []

#creation of socket object UDP and bind
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
#socket non blocking --> will always try to grab datas from the stream
#not block it

print("Server Started.")

#INITIAL SETUP PERIOD
secs = 20
max_players = 5

# WAIT FOR PLAYERS TO JOIN
while ((secs > 0) and (len(players) < max_players)):
    ready = select.select([s], [], [], 1)
    if ready[0]:
        data, addr = s.recvfrom(1024)
        print("FIRST RECV {}".format(data))
        if addr not in players:
            players.append(addr)
            print("liste players {}".format(players))
            s.sendto("Wait for game to start... ",players[len(players)-1])
        print(time.ctime(time.time()) +  ":" + str(data))
    secs = secs - 1

#START GAME
print("Game starting")
for i in range(len(players)):
    try:
        s.sendto("Game starting", players[i])
    except:
        pass

#ASK QUESTIONS
nb = 3
for k in range(nb):
    print("question nb {}".format(k))
    nbq = chooseQuestion(question2,answer2)
    #print("ENTER FOR")
    for i in range(len(players)):
        try:
            s.sendto(str(question2[nbq]), players[i])
            #print("BEFORE GET ANSWER")
            agiven = ""
            ready = select.select([s], [], [], 10)
            if ready[0]:
                agiven, addr = s.recvfrom(1024)
                #print("GOT ANSWER")
            print("agiven is : {}".format(agiven))
            checkAnswer(answer2,agiven,nbq)
        except:
            pass

for i in range(len(players)):
    try:
        s.sendto("The game is finished", players[i])
    except:
        pass

final_score(score)
s.close()