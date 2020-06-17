import numpy as np

#find a way to handle pawn moves two in the start and gets killed thingy
#find a way to handle pawn moves two in the start and gets killed thingy
#find a way to handle pawn moves two in the start and gets killed thingy
class Board():
    def __init__(self):
        self.board=np.zeros((8,8),'int8')

    def __repr__(self):
        return str(self.board)

    @staticmethod
    def addVertical(pos,amount):
        return (pos[0]+amount,pos[1])

    @staticmethod
    def addHorizontal(pos,amount):
        return (pos[0],pos[1]+amount)

    @staticmethod
    def addCoords(pos,h,v):
        return (pos[0]+v,pos[1]+h)

    @staticmethod
    def isInside(piece,pos):
        try:
            #SELF DOESNT WORK HERE
            #SELF DOESNT WORK HERE
            #SELF DOESNT WORK HERE
            self.board[pos]
            return True
        except:
            return False

    @staticmethod
    def isInsidefilter(arr):
        return list(filter(Board.isInside,arr))

    @staticmethod
    def filterTeammates(piece,arr):
        for element in arr:
            if piece.board.teammatePresentAt(piece,element):
                arr.remove(element)
        return arr

    def enemyAvailableMoves(self,piece):
        pass
        #check all possible enemy moves. use it to prevent putting self_king in check

    def enemyPresentAt(self,piece,pos):
        if pieceAt(pos).isWhite and piece.isWhite:
            return False
        if not pieceAt(pos).isWhite and not piece.isWhite:
            return False
        if not pieceAt(pos).isWhite and piece.isWhite:
            return True
        if pieceAt(pos).isWhite and not piece.isWhite:
            return True

    def teammatePresentAt(self,piece,pos):
        if pieceAt(pos).isWhite and piece.isWhite:
            return True
        if not pieceAt(pos).isWhite and not piece.isWhite:
            return True
        if not pieceAt(pos).isWhite and piece.isWhite:
            return False
        if pieceAt(pos).isWhite and not piece.isWhite:
            return False

    def pieceAt(self,pos):
        #return refernce to piece
        #return False if no piece is present
        pass

    def capturePiece(self,piece):
        piece.taken=True

    def whiteKingInCheck(self):
        pass

    def blackKingInCheck(self):
        pass

    def checkPromotion(self):
        pass
