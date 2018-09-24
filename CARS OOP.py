def SetBoard():
    Board = []
    for i in range(6):
        Row = []
        for i in range(6):
            Row.append("_")
        Board.append(Row)
    return Board


def PrintBoard(Board):
    marker = 0
    for x in Board:
        if len(x)==6:
            row = x
        for i in row:
            print(i,"|",end=" ")
            marker += 1
            if marker == 6:
                print("\n")
                marker = 0


class Cars:
    def __init__(self, Colour, Size, Orientation, Row, Column, Board):
        self.Colour = Colour
        self.Size = Size
        self.Orientation = Orientation
        self.Row = Row
        self.Column = Column
        self.RunCars(Board)

    def RunCars(self,Board):
        if self.Orientation == "H":
            for i in range(self.Size):
                Board[self.Row][self.Column+i] = self.Colour
        else:
            for i in range(self.Size):
                Board[self.Row+i][self.Column] = self.Colour

    def MoveCar(self, Board, Colour):
        if self.Orientation == "H":
            Column2 = int(input("Enter moving Column: "))
            while Column2 < 0 or Column2 > 5:
               Column2 = int(input("Enter moving Column: "))
            else:
                self.Column = Column2
                Row = self.Row
        else:
            Row2 = int(input("Enter moving Row: "))
            while Row2 < 0 or Row2 > 5:
                Row2 = int(input("Enter moving Row: "))
            self.Row = Row2
            Column = self.Column


            
        CheckColumn(Colour,self.Column)
        CheckRow(Colour, self.Row)
        Set = ValidateCars(self ,Board, self.Row, self.Column)
        if Set == True:
            RemoveCars(Board,self.Colour)
            self.RunCars(Board)
            
            
def CheckColumn(Colour,Column):
    print("HELLOE")
    if Column+1 > 5 or Column+2 > 5:
        Column = 3


def CheckRow(Colour,Row):
    if Row+1 > 5 or Row+2 > 5:
        Row = 3

def RemoveCars(Board,Colour):
    for i in range(len(Board)):
        for ii in range(len(Board[i])):
            if Board[i][ii] == Colour[0]:
                Board[i][ii] = "_"
        
def ValidateCars(Colour, Board, Row, Column):
    
    if Board[Row][Column] in ["Y","B","P","G","R"]:
        print("Invalid Coords")
        Colour.MoveCar(Board, Colour)
    

        return False
    return True
        
        
        
    
           
Board = SetBoard()       

Red = Cars("R", 2, "H", 2,0, Board)
Purple = Cars("P", 3, "H", 3,0, Board)
Yellow = Cars("Y", 3, "V", 0,2, Board)
Green = Cars("G", 2, "H", 0,4, Board)
Blue = Cars("B", 3, "V", 3,5, Board)

while Board[2][5] != ["R"]:

    PrintBoard(Board)
    colour = input("Enter a colour u want to move: ").upper()
    while colour not in ["R","P", "Y","G","B"]:
        colour = input("Enter a colour u want to move: ").upper()
    Colour = colour
        
    if colour == "R":
        Red.MoveCar(Board, Colour)
    elif colour == "P":
        Purple.MoveCar(Board, Colour)
    elif colour == "Y":
        Yellow.MoveCar(Board, Colour)
    elif colour == "G":
        Green.MoveCar(Board, Colour)
    elif colour == "B":
        Blue.MoveCar(Board, Colour)
    else:
        print("shouldnt get here")

PrintBoard(Board)

    


