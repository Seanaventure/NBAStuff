playByPlay="Play by Play Data Sample"
eventCodes="Event Codes"
lineUp="Game Lineup Data Sample"
playByPlayList=[]
eventList=[]
lineUpList=[]



# reads files and stores to according lists
def read(name,lst):
    file = open(name)
    line = file.readline()
    line = file.readline().strip()
    while line != "":
        splitLine = line.split("\t")
        lst.append(splitLine)
        line = file.readline().strip()
    file.close()


def main():
    read(playByPlay,playByPlayList)
    read(eventCodes,eventList)
    read(lineUp,lineUpList)
    print(eventList)
    # intializing the dict of players with their team id and plus/minus
    players=dict()
    for player in lineUpList[2]:
        players[player]=[lineUpList[3],0]
    for event in playByPlayList[2]:
        if(event==1):
    # do plus/minus


main()