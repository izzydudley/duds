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
    def __init__(self, Car, Orientation, Row, Column, Board):
        self.Car = Car
        self.Orientation = Orientation
        self.Row = Row
        self.Column = Column

        SetCars(Board, Row, Column, Car)

    def MoveCar(self, Board, Car):
        if self.Orientation == "H":
            Column2 = int(input("Enter moving Column: "))
            while Column2 < 0 or Column2 > 5:
               Column2 = int(input("Enter moving Column: "))
            else:
                Column = Column2
                #Column = Column2 - 1
                #if Car== "PURPLE":
                 #   Column -= 1
                Row = self.Row
        else:
            Row2 = int(input("Enter moving Row: "))
            while Row2 < 0 or Row2 > 5:
                Row2 = int(input("Enter moving Row: "))
            Row = Row2
            #Row = Row2 - 1
            #if Car == "YELLOW" or Car == "BLUE":
                #Row -= 1
            Column = self.Column

        Set = ValidateCars(self ,Board, Row, Column)
        if Set == True:
            RemoveCars(Board,self.Row,self.Column,self.Car)
            self.Row = Row
            self.Column = Column
            SetCars(Board, Row, Column, self.Car)
            
        


def RemoveCars(Board,Row,Column,Car):
    if Car == "RED":
            Board[Row][Column] = "_"
            Board[Row][Column+1] = "_"

    elif Car =="PURPLE":
            Board[Row][Column] = "_"
            Board[Row][Column+1] = "_"
            Board[Row][Column+2] = "_"


    elif Car== "YELLOW":
            Board[Row][Column] = "_"
            Board[Row+1][Column] = "_"
            Board[Row+2][Column] = "_"
            

    elif Car == "GREEN":
            Board[Row][Column] = "_"
            Board[Row][Column+1] = "_"
            

    elif Car == "BLUE":
        Board[Row][Column] = "_"
        Board[Row+1][Column] = "_"
        Board[Row+2][Column] = "_"
                       
    else:
        print("Invalid car")

    

def SetCars(Board, Row, Column, Car):
    if Car == "RED":
                if Column+1 > 5:
                    Column = 4
                Board[Row][Column] = "R"
                Board[Row][Column+1] = "R"

    elif Car =="PURPLE":
            if Column+1 > 5 or Column+2 > 5:
                Column = 3
            Board[Row][Column] = "P"
            Board[Row][Column+1] = "P"
            Board[Row][Column+2] = "P"


    elif Car== "YELLOW":
            if Row+1 > 5 or Row+2 > 5:
                Row = 3
            Board[Row][Column] = "Y"
            Board[Row+1][Column] = "Y"
            Board[Row+2][Column] = "Y"
            

    elif Car == "GREEN":
            if Column+1 > 5:
                Column = 4
            Board[Row][Column] = "G"
            Board[Row][Column+1] = "G"
            

    elif Car == "BLUE":
        if Row+1 > 5 or Row+2 > 5:
            Row = 3
        Board[Row][Column] = "B"
        Board[Row+1][Column] = "B"
        Board[Row+2][Column] = "B"
                       
    else:
        print("Invalid car")

        
def ValidateCars(Car, Board, Row, Column):
    
    if Board[Row][Column] in ["Y","B","P","G","R"]:
        print("Invalid Coords")
        Car.MoveCar(Board, Car)
    

        return False
    return True
        
        
        
    
           
Board = SetBoard()       

Red = Cars("RED", "H", 2,0, Board)
Purple = Cars("PURPLE", "H", 3,0, Board)
Yellow = Cars("YELLOW", "V", 0,2, Board)
Green = Cars("GREEN", "H", 0,4, Board)
Blue = Cars("BLUE", "V", 3,5, Board)

while Board[2][5] != ["R"]:

    PrintBoard(Board)
    car = input("Enter a car u want to move: ").upper()
    while car not in ["RED","PURPLE", "YELLOW","GREEN","BLUE"]:
        car = input("Enter a car u want to move: ").upper()
    Car = car
        
    if car == "RED":
        Red.MoveCar(Board, Car)
    elif car == "PURPLE":
        Purple.MoveCar(Board, Car)
    elif car == "YELLOW":
        Yellow.MoveCar(Board, Car)
    elif car == "GREEN":
        Green.MoveCar(Board, Car)
    elif car == "BLUE":
        Blue.MoveCar(Board, Car)
    else:
        print("shouldnt get here")

PrintBoard(Board)

    


