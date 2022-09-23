


# function 1: divide players into teams  - done
def group_together(players,teams): 
	#creating a deep copy of players and clearing players so I can create groups
    players_copy = []
    for i in range (len(players)):
        players_copy.append(players[i])
    players.clear()
    newteam = []
    counter = 0
    for element in players_copy:
    	#creating group sizes by adding element until counter is = to the number of players in each team
        newteam.append(element)
        counter += 1
        #once count is = the number of players, the group is added to players and then cleared so it can start again 
        if counter % teams == 0 or counter == len(players_copy):
            players.append(newteam)
            newteam = []


#example 1
#players = [456, 218, 67, 1, 101, 199]
##group_together(players, 3)
#print(players)

#example 2:
#players = [456, 218, 67, 1, 101, 199]
##print(players)

#example 3:
##group_together(players, 4)
#print(players)

#example 4:
#players = [456, 218, 67, 1, 101, 199]
#group_together(players, 5)
#print(players)

#example 5:
#players = [456, 218, 67, 1, 101, 199]
#group_together(players, 6) 
#print(players)
           

           


#function 2 , player and bets placed
def monitor_bets(playersInfo, bets):
    playersInfo_copy = []
    for i in range(len(playersInfo)):
        playersInfo_copy.append(playersInfo[i])
    playersInfo.clear()
    for i in playersInfo_copy:
        player = False 
        found = 0
        bet_total = 0
        for j in bets:
            if i[1] == j[0]:
                found += 1
                bet_total += j[1]
                player = True
        if player == True:
            playersInfo.append([i[0], i[1], round(bet_total, 2)])
        else:
            playersInfo.append([i[0], i[1]])
    #if found == 0:
        #playersInfo.append([i[0], i[1]])
        

#playerInfo = [["Seong Gi-hun", 456], ["Cho Sang-woo", 218], ["Kang Sae-byeok", 67], ["Abdul Ali", 199], ["Byeong-gi", 111]]
#bets = [[199, 100000], [111, 10000], [218, 10000], [111, 50], [67, 100000.00], [199, 50000.00]]
#monitor_bets(playerInfo, bets)
#print(playerInfo)                
#playersInfo = [['Seong Gi-hun', 456], ['Cho Sang-woo', 218], ['Kang Say-Buook', 67]]
#bets = [[67, 1000000.00], [67, 2000000.00], [218, 300000.00], [456, 450000.20]]
#moniter_bets(playersInfo, bets)
#print(playersInfo)
#example `
#playersInfo = [['Seong Gi-hun', 456], ['Cho Sang-woo', 218], ['Kang Say-Buook', 67]]
#bets = [[67, 1000000.00], [67, 2000000.00], [218, 100000.00], [456, 450000.20]]
##print(playersInfo)

#example 2
#playerInfo = [["Seong Gi-hun", 456], ["Cho Sang-woo", 218],["Kang Sae-byeok", 67], ["Abdul Ali", 199], ["Byeong-gi", 111]]
#bets = [[199, 100000], [111, 10000], [218, 10000], [111, 50], [67, 100000.00],[199, 50000.00]]
#moniter_bets(playersInfo, bets)
#print(playersInfo)

#example 3 
#playerInfo = [["Seong Gi-hun", 456], ["Cho Sang-woo", 218], ["Kang Sae-byeok", 67],	["Oh Il-nam", 1], ["Jang Deok-su", 101], ["Abdul Ali", 199], ["Kim Joo-ryoung", 212], ["Byeong-gi", 111]]
#bets = [[67, 1000000], [101, 2000000], [199, 3000000], [199, 2], [456, 10]]
#moniter_bets(playersInfo, bets)
#print(playersInfo)




#function 3 - new 
def compress_info(playerTrack):
	#creating a copy of playerTrack and clearing it
    copy_playerTrack = []
    for i in range(len(playerTrack)):
        copy_playerTrack.append(playerTrack[i])
    playerTrack.clear()
    #checking to see if the team player is the same for the bets 
    for i in copy_playerTrack:
        count = 0
        for j in playerTrack:
            if i[0] == j[0]:
            	# if the bet is the same for the team player, the bet value is updated
                j[1] = round((j[1] + (i[1])), 2)
                count += 1
        if count == 0:
            playerTrack.append([i[0], i[1]])

# example 
#playerTrack = [[456, 3000000], [10, 10], [67, 10000], [199, 400000], [10, 20]]
#compress_info(playerTrack) 
#print(playerTrack)
# instead of adding the bet values for the same player, it is duplicating it?   





#function 4 - games and players that won - done 
def set_of_games(games, searchNum):
	set_of_games = set()
	#checking to see if element in list is greater than the searchNum value 
	for element in games.values():
		# if the value is larger, it is added to the set 
		if element[1] >= searchNum:
			set_of_games.add(element[0])
	return set_of_games

# example 
#games = {'game 1' : ['RLGL, 201'], 'game 2' : ["PPOPGI", 80],'game 3' : ["Tug of War", 44],'game 4' : ["Marbles", 1] , 'game 5' : ["Bridge", 3],'game 6' : ["Squid", 1]}
#set_of_games(games, 10)
#set_of_games(games, 70)
#set_of_games(games, 44)
#set_of_games(games, 1)




















