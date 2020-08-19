import socket
import json
import sys

sk = socket.socket()               
sk.connect((sys.argv[1],int(sys.argv[2]))) 
string1=sk.recv(10240)         
while string1!="0\n":
 def calc_win(arguement):
	max = 0
	winners = []
	for x in range(len(arguement)):
		if max < arguement[x]:
			if len(winners) != 0:
				del winners[:]
			max = arguement[x]
			winners.append(x+1)
		elif max == arguement[x]:
			winners.append(x+1)
	if len(winners) == 1:
		return winners[0]
	else:
		return winners
 switcher = { 
		'0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'S': 20,
        'T': 20,
        'R': 20,
        'W': 50,
        'F': 50 
	} 	
 string = string1.split('||')

 round_winner = dict()
 players_list=[]
 no_of_players=string[0]
 np=int(no_of_players)
 player_score = [0] * np
 for i in range(1,np+1):
  players_list.append(str(i))
 no_of_rounds=string[1]
 del string[0]
 del string[0]

 l =(len(string)) #length of string (l= 9)            ['1', '1:2,0,S,W', '3:0,1,S']
 rounddata = []
 zerolist = []
 for i in range(0,l):
  if string[i]=='0':
   zerolist.append(i)

 for j in range(len(zerolist)): #for appending the list by rounds into rounddata
  if j==0:
	rounddata.append(string[:zerolist[j]])
  else:
	rounddata.append(string[zerolist[j-1]+1 : zerolist[j]])
 #print "rr",rounddata,"rr"  #[['1', '1:2,0,S,W', '3:0,1,S'], ['2', '2:F,6', '3:4,5,W,3,0']]
 rounddata={i+1:e for i, e in enumerate(rounddata)}  
 player_of_round = []
 winners = []
 for x in rounddata.values():
  l=len(x) #length of roundata
  score = 0
  if len(player_of_round) != 0:
   del player_of_round[:]
  for i in range (1,l):
   player_of_round_with_cards = (x[i])
   #print player_of_round_with_cards #eg 1:2,0,S,W and 3:0,1,S
   prc = player_of_round_with_cards.split(':') #eg ['1', '2,0,S,W'] and ['3', '0,1,S']
   player_of_round.append(prc[0])
   for s in prc[1]:
    if s in switcher.keys():
	 score = score + switcher[s]
  for p in player_of_round:
   if p in players_list:
	 players_list.remove(p)
	
  if	len(players_list)==1:
   round_winner[x[0]] = int(players_list[0])
   player_score[int(players_list[0]) - 1] = player_score[int(players_list[0]) - 1] + score
  del players_list[:]
  for i in range(1,np+1):
   players_list.append(str(i))

 overall_winner = calc_win(player_score)
		  				
 p_s = dict()
 for x in range(len(player_score)):
  p_s[str(x+1)] = player_score[x]
 result = {
        "round_winners" : round_winner,
        "overall_winner" : overall_winner,
        "scores" : p_s,
    }

 #r = json.dumps({"round_winners": round_winner, "overall_winner": overall_winner, "scores": p_s})
 sk.send(json.dumps(result)+"\n")
 string1=sk.recv(10240) 
sk.close()
