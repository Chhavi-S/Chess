class Piece:
    def __init__(self,board,currentPos,isWhite=True,bottomWhite=True):
        self.isWhite=isWhite
        self.taken=False
        self.board=board
        self.currentPos=currentPos
        #direction
        self.d=-1 if self.isWhite and bottomWhite else 1
    def allowedMoves(self):
        #return list of positons which are allowed
        output=list()
        return Board.isInsidefilter(Board.filterTeammates(self,output))
    def __canMove(self,targetPos):
        return targetPos in self.__allowedMoves()
    def move(self,targetPos):
        #check for enemy capture
        if self.canMove(targetPos):
            self.currentPos=targetPos

class Pawn(Piece):
    def __init__(self,isWhite,board):
        super().__init__(isWhite,board)
        self.moved=False
        self.promoted=False

    def allowedMoves(self):
        #check if allowed moves are inside board
        output=list()
        oneStep=Board.addVertical(self.currentPos,self.d*1)
        twoStep=Board.addVertical(self.currentPos,self.d*2)
        leftCapture=Board.addCoords(self.currentPos,-1,self.d*1)
        rightCapture=Board.addCoords(self.currentPos,1,self.d*1)

        if not self.board.pieceAt(oneStep):
            output.append(oneStep)

        if not self.moved and not self.board.pieceAt(twoStep):
            output.append(twoStep)

        if self.board.enemyPresentAt(self,leftCapture):
            output.append(leftCapture)
        if self.board.enemyPresentAt(self,rightCapture):
            output.append(rightCapture)

        return Board.isInsidefilter(Board.filterTeammates(self,output))

    def __canMove(self,targetPos):
        return targetPos in self.__allowedMoves()

    def checkPromotion(self):
        pass

    def move(self,targetPos):
        #check for enemy capture
        if self.canMove(targetPos):
            self.currentPos=targetPos
            self.moved=True

class King(Piece):
    def __init__(self,isWhite,board):
        super().__init__(isWhite,board)
        self.moved=False
        self.castled=False

    def allowedMoves(self):
        #return list of positons which are allowed
        #add castling conditon
        #also move that rook
        output=list()
        return Board.isInsidefilter(Board.filterTeammates(self,output))

    def __canMove(self,targetPos):
        return targetPos in self.__allowedMoves()

    def move(self,targetPos):
        #check for enemy capture
        if self.canMove(targetPos):
            self.currentPos=targetPos
            self.moved=True

class Queen(Piece):
    def __init__(self,isWhite,board):
        super().__init__(isWhite,board)

    def allowedMoves(self):
        #return list of positons which are allowed
        output=list()

        x=1
        while True:
            coord=Board.addHorizontal(self.currentPos,x)
            if self.board.teammatePresentAt(self,coord):
                break
            if not Board.isInside(coord):
                break
            if self.board.enemyPresentAt(self,coord):
                output.append(coord)
                break
            output.append(coord)
            x+=1

        x=-1
        while True:
            coord=Board.addHorizontal(self.currentPos,x)
            if self.board.teammatePresentAt(self,coord):
                break
            if not Board.isInside(coord):
                break
            if self.board.enemyPresentAt(self,coord):
                output.append(coord)
                break
            output.append(coord)
            x-=1

        y=1
        while True:
            coord=Board.addVertical(self.currentPos,x)
            if self.board.teammatePresentAt(self,coord):
                break
            if not Board.isInside(coord):
                break
            if self.board.enemyPresentAt(self,coord):
                output.append(coord)
                break
            output.append(coord)
            y+=1

        y=-1
        while True:
            coord=Board.addVertical(self.currentPos,x)
            if self.board.teammatePresentAt(self,coord):
                break
            if not Board.isInside(coord):
                break
            if self.board.enemyPresentAt(self,coord):
                output.append(coord)
                break
            output.append(coord)
            y-=1

        for x in [1,-1]:
            for y in [1,-1]:
                while True:
                    coord=Board.addCoords(self.currentPos,x,y)
                    if self.board.teammatePresentAt(self,coord):
                        break
                    if not Board.isInside(coord):
                        break
                    if self.board.enemyPresentAt(self,coord):
                        output.append(coord)
                        break
                    output.append(coord)
                    x+=1


        return Board.isInsidefilter(Board.filterTeammates(self,output))

    def __canMove(self,targetPos):
        return targetPos in self.__allowedMoves()

    def move(self,targetPos):
        #check for enemy capture
        if self.canMove(targetPos):
            self.currentPos=targetPos

class Bishop(Piece):
    def __init__(self,isWhite,board):
        super().__init__(isWhite,board)

    def allowedMoves(self):
        #return list of positons which are allowed
        output=list()

        for x in [1,-1]:
            for y in [1,-1]:
                while True:
                    coord=Board.addCoords(self.currentPos,x,y)
                    if self.board.teammatePresentAt(self,coord):
                        break
                    if not Board.isInside(coord):
                        break
                    if self.board.enemyPresentAt(self,coord):
                        output.append(coord)
                        break
                    output.append(coord)
                    x+=1


        return Board.isInsidefilter(Board.filterTeammates(self,output))

    def __canMove(self,targetPos):
        return targetPos in self.__allowedMoves()

    def move(self,targetPos):
        #check for enemy capture
        if self.canMove(targetPos):
            self.currentPos=targetPos

class Knight(Piece):
    def __init__(self,isWhite,board):
        super().__init__(isWhite,board)

    def allowedMoves(self):
        #return list of positons which are allowed
        output=list()

        for y in [2,-2]:
            for x in [1,-1]:
                output.append(Board.addCoords(self.currentPos,x,y))
                output.append(Board.addCoords(self.currentPos,y,x))

        return Board.isInsidefilter(Board.filterTeammates(self,output))

    def __canMove(self,targetPos):
        return targetPos in self.__allowedMoves()

    def move(self,targetPos):
        #check for enemy capture
        if self.canMove(targetPos):
            self.currentPos=targetPos

class Rook(Piece):
    def __init__(self,isWhite,board):
        super().__init__(isWhite,board)

    def allowedMoves(self):
        #return list of positons which are allowed
        output=list()

        x=1
        while True:
            coord=Board.addHorizontal(self.currentPos,x)
            if self.board.teammatePresentAt(self,coord):
                break
            if not Board.isInside(coord):
                break
            if self.board.enemyPresentAt(self,coord):
                output.append(coord)
                break
            output.append(coord)
            x+=1

        x=-1
        while True:
            coord=Board.addHorizontal(self.currentPos,x)
            if self.board.teammatePresentAt(self,coord):
                break
            if not Board.isInside(coord):
                break
            if self.board.enemyPresentAt(self,coord):
                output.append(coord)
                break
            output.append(coord)
            x-=1

        y=1
        while True:
            coord=Board.addVertical(self.currentPos,x)
            if self.board.teammatePresentAt(self,coord):
                break
            if not Board.isInside(coord):
                break
            if self.board.enemyPresentAt(self,coord):
                output.append(coord)
                break
            output.append(coord)
            y+=1

        y=-1
        while True:
            coord=Board.addVertical(self.currentPos,x)
            if self.board.teammatePresentAt(self,coord):
                break
            if not Board.isInside(coord):
                break
            if self.board.enemyPresentAt(self,coord):
                output.append(coord)
                break
            output.append(coord)
            y-=1


        return Board.isInsidefilter(Board.filterTeammates(self,output))

    def __canMove(self,targetPos):
        return targetPos in self.__allowedMoves()

    def move(self,targetPos):
        #check for enemy capture
        if self.canMove(targetPos):
            self.currentPos=targetPos
