import json
import socket
import sys
import os

sk = socket.socket()  
sk.bind(('',int(sys.argv[1])))
sk.listen(3)

def server():
    i=1
    while i<=3:
        c, addr=sk.accept()
        child_pid=os.fork()
        i=i+1
        if child_pid==0:
                handle_client(c, addr, i)
                return
       
    
def handle_client(s, addr, i):
    while True:
        string1 = s.recv(102400)
        if string1=="0\n":
         break
        d=dict()
        d=json.loads(string1)
        output = {}
        count = 0
        squares_traversedc = {}
        squares_traversed = {}
        player_count=d['player_count'] 
        board_dimension=d['board_dimension'] 
        ladders=d['ladders']
        snakes=d['snakes']
        switcher = ladders.copy()
        switcher.update(snakes)
        die_tosses=d['die_tosses']
        die_tosses={int(key):value for key,value in die_tosses.items()}
        rounds=len(die_tosses) 
        score = []
        score = [0] * player_count
        for x in die_tosses.values():
        	die_toss = []
        	die_toss = x 
        	die_toss={int(key):value for key,value in die_toss.items()}
        	key =[] 
        	value = []
        	key = list(die_toss.keys())
        	value = list(die_toss.values())
        	l=len(x)
        	for i in range(0,l):
        	 if score[i]+value[i]>(board_dimension**2):
        	 	continue
        	 score[i]+=value[i]
        	 squares_traversed.setdefault((i+1), []).append(score[i])
        	 while str(score[i]) in switcher.keys():
        	 	score[i] = switcher.get(str(score[i]))
        	 	squares_traversed.setdefault((i+1), []).append(score[i])
        	 squares_traversedc[i+1]=score[i]
        listOfItems = squares_traversedc.items()
        for item  in listOfItems:
         if item[1] == (board_dimension**2):
          count = count + 1
        for item  in listOfItems:
         if item[1] ==(board_dimension**2):
          output['winner'] = (item[0])
        if count==0:
         output['winner']= None
        if count >= 1:
         output['game_state'] = 'finished'
        else:
         output['game_state'] = 'progress'
        output['final_positions']=squares_traversedc
        output['squares_traversed']=squares_traversed
        s.sendall(json.dumps(output)+"\n") 
server()
sk.close()
	 
