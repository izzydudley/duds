def SetBoard():
    print(" ____ ____ ____ ____ ____")
    for i in range(2):
        print("|____|____|____|____|____|")
    print("|____|____|____|____|____")
    for i in range(2):
        print("|____|____|____|____|____|")


SetBoard()

def Board():
    Board = []
    for i in range(5):
        Row = []
        for i in range(5):
            Row.append("_")
        Board.append(Row)
    print(Board)
    return Board

Board()
