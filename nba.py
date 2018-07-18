playByPlay="Play by Play Data Sample"
eventCodes="Event Codes"
lineUp="Game Lineup Data Sample"
playByPlayList=[]
eventList=[]
lineUpList=[]



# reads files and stores to according lists
def read(name,lst):
    file = open(name)
    line = file.readline().strip()
    line = file.readline().strip()
    while line != "":
        splitLine = line.split("\t")
        # print(splitLine)
        # print("")
        lst.append(splitLine)
        line = file.readline().strip()
    file.close()

# def readplay():
#     with open(playByPlay) as f:
#         for line in f:
#             playByPlayList.append(line.split())






def main():
    read(playByPlay,playByPlayList)
    print(playByPlayList)
    # read(eventCodes,eventList)
    # read(lineUp,lineUpList)
    # print(eventList)
    # # intializing the dict of players with their team id and plus/minus
    # players=dict()
    # for player in lineUpList[2]:
    #     players[player]=[lineUpList[3],0]
    # # player Plus/Minus
    # scoringTeam = playByPlayList[10]  # scoring team id
    # for event in playByPlayList:
    #     print(event)
    #     print("here")
    #     if event[2] == '1':
            # if there is a goal
            # print("true")
            # find team id

#       if(event==1):
#           for player,list in players:
#
#                print(player)
#                print("WEIOFFFFFFFFFFFFIEWOFIJEI")
#                print(list[0])
#                print(scoringTeam)
#                if list[0] == scoringTeam:
#                    print(list)
#                    list[1] += 1
#                    print(list)
#                    print("wut")
#            pass

main()