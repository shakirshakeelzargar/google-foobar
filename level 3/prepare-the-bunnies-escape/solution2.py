

class Board(list):

    traversable_value    = 0
    nontraversable_value = 1
    unvisited_value      = None
    unreachable_value    = None

    def __getitem__(self, tup):
        r, c = tup
        return super(self.__class__, self).__getitem__(r).__getitem__(c)

    def __setitem__(self, tup, val):
        r, c = tup
        super(self.__class__, self).__getitem__(r).__setitem__(c, val)

from collections import deque

class Cell(tuple):

    def __init__(self, minDistTo = None):
        self.minDistTo = minDistTo

    def getNeighbors(self):

        r, c = self

        yield self.__class__( (r-1, c) ) # up
        yield self.__class__( (r+1, c) ) # down
        yield self.__class__( (r, c-1) ) # left
        yield self.__class__( (r, c+1) ) # right

    def isInside(self, board):
        r, c = self
        num_rows, num_cols = len(board), len(list(board)[0])

        return 0 <= r < num_rows and 0 <= c < num_cols

    def isTraversableIn(self, board):
        return board[self] == board.__class__.traversable_value

    def isAWallIn(self, board):
        return board[self] == board.__class__.nontraversable_value

    def hasNotBeenVisitedIn(self, board):
        return board[self] == board.__class__.unvisited_value

    def isUnreachableFrom(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.minDistTo[self] == other.minDistTo.__class__.unreachable_value # hard to understand

    # O(h*w) time complexity
    def genMinDistTo(self, m):
       
        if self.isAWallIn(board = m):
            return None

        h = len(m)
        w = len(list(m)[0])

        minDistTo = Board( [ [Board.unvisited_value]*w for _ in range(h) ] )

        minDistTo[self] = 1
        cells = deque([self]) 

        while cells:

            cell          = cells.popleft()
            minDistToCell = minDistTo[cell]

            for neighbor in cell.getNeighbors(): 

                if neighbor.isInside(board = m) and \
                   neighbor.isTraversableIn(board = m) and \
                   neighbor.hasNotBeenVisitedIn(board = minDistTo):

                    minDistToNeighbor   = minDistToCell + 1
                    minDistTo[neighbor] = minDistToNeighbor

                    cells.append(neighbor) 

        self.minDistTo = minDistTo

def solution(m):

    num_rows = h = len(m)   
    num_cols = w = len(m[0])

    m = Board(m)

    bestConceivableResult = h + w - 1

    start = Cell( (  0,   0) )
    end   = Cell( (h-1, w-1) )

    start.genMinDistTo(m) # O(h*w) time

    if end.isUnreachableFrom(start):

        bestResult_soFar = 2**31 - 1
    else:
        bestResult_soFar = start.minDistTo[end]

    if bestResult_soFar == bestConceivableResult:
        return bestConceivableResult

    end.genMinDistTo(m) 

    for r in range(num_rows):
        for c in range(num_cols):

            cell = Cell( (r, c) )

            if cell.isAWallIn(board = m):

                wall = cell


                potentiallyBetterResult = whatIfIRemovedThis(wall, m, start, end) # O(1) time

                bestResult_soFar = min(bestResult_soFar, potentiallyBetterResult)

    bestResult = bestResult_soFar

    return bestResult

def whatIfIRemovedThis(wall, m, start, end):
   


    bestResult_soFar = 2**31 - 1

    for incoming in wall.getNeighbors():
        for outgoing in wall.getNeighbors():
            if incoming == outgoing:
                continue

            if not incoming.isInside(board  = m)     or not outgoing.isInside(board  = m)    or \
                   incoming.isAWallIn(board = m)     or     outgoing.isAWallIn(board = m)    or \
                   incoming.isUnreachableFrom(start) or     outgoing.isUnreachableFrom(end):
                continue

            minDistFromStartToIncoming = start.minDistTo[incoming]
            minDistFromOutgointToEnd   = end.minDistTo[outgoing]

            potentiallyBetterResult = minDistFromStartToIncoming + 1 + minDistFromOutgointToEnd

            bestResult_soFar = min(bestResult_soFar, potentiallyBetterResult)

    bestResult = bestResult_soFar

    return bestResult



ls=[
    [0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0]
]

solution(ls)