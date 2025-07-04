board=[[None for i in range(0,9)] for j in range(0,9)]


def srows():
    rows=[]
    for i in range(0,9):
        row=[board[i][j] for j in range (9)]
        rows.append(row)
    return(rows)
def scolumns():
    columns=[]
    for j in range(0,9):
        column=[board[i][j] for i in range(9)]
        columns.append(column)
    return(columns)
def sboxes():
    boxes=[]
    for m in range (0,9,3):
        for k in range(0,9,3):
            box=[board[i][j] for j in range(k,k+3) for i in range (m,m+3)]
            boxes.append(box)
    return(boxes)
def end():
    ideal=set([1,2,3,4,5,6,7,8,9])
    rows=srows()
    columns=scolumns()
    boxes=sboxes()
    for i in range(0,9):
        if set(rows[i])!=ideal:
            return(False)
        if set(columns[i])!=ideal:
            return(False)
        if set(boxes[i])!=ideal:
            return(False)
    return True
def dis():
    for i in range(0,9):
        for j in range(0,9):
            var=board[i][j]
            print(f"| {var if var is not None else ' '} ",end="")
            if (j+1)%3==0 :
                print("|",end="")
        print()
        if (i+1)%3==0 and i!=8:
            print("_"*40)
            print()


def filter(a):
    filtered = []
    for i in range(9):
        temp = [x for x in a[i] if x is not None]
        filtered.append(temp)
    return filtered

def checkinput():
    for group in srows() + scolumns() + sboxes():
        values = [x for x in group if x is not None]
        if len(values) != len(set(values)):
            return False
        if not all(1 <= x <= 9 for x in values):
            return False
    return True


def solve():
    if any(None in row for row in board):
        print("empty")
        i,j=empty()
        for k in range (1,10):
                        board[i][j]=k
                        print("*")
                        if checkinput()==False:
                            board[i][j]=None
                            continue
                        if solve():
                            return True
                        board[i][j]=None
    else:
        if end():
              print("solved suduko!!!")
              dis()
              return True
        return False

def empty():
    for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==None:
                    return i,j

dis()
known_cells = [
    (1, 1, 5), (1, 2, 3), (1, 5, 7),
    (2, 1, 6), (2, 4, 1), (2, 5, 9), (2, 6, 5),
    (3, 2, 9), (3, 3, 8), (3, 8, 6),
    (4, 1, 8), (4, 5, 6), (4, 9, 3),
    (5, 1, 4), (5, 4, 8), (5, 6, 3), (5, 9, 1),
    (6, 1, 7), (6, 5, 2), (6, 9, 6),
    (7, 2, 6), (7, 7, 2), (7, 8, 8),
    (8, 4, 4), (8, 5, 1), (8, 6, 9), (8, 9, 5),
    (9, 5, 8), (9, 8, 7), (9, 9, 9)
]


# Populate the board
for r, c, val in known_cells:
    board[r - 1][c - 1] = val

dis()
print("start solver")
solve()
print("solver ended")
