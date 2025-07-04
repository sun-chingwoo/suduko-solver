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
    ideal=[1,2,3,4,5,6,7,8,9]
    rows=srows()
    columns=scolumns()
    boxes=sboxes()
    for i in range(0,9):
        if rows[i]!=ideal:
            return(False)
        if columns[i]!=ideal:
            return(False)
        if boxes[i]!=ideal:
            return(False)
    return True
def dis():
    for i in range(0,9):
        for j in range(0,9):
            var=board[i][j]
            print(f"| {var if var is not None else " "} ",end="")
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
                            board[i][j]=None
                            return True
                        return False

    else:
        if end():
              print("solved suduko!!!")
              dis()
              return True
        else:
             return False


def empty():
    for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==None:
                    return i,j

dis()
n=int(input("enter number of known places"))
for i in range (n):
    irow=int(input("Enter the row :  "))
    icol=int(input("enter the column :"))
    value=int(input("Enter value : "))
    board[irow-1][icol-1]=value

dis()
print("start solver")
solve()
print("solver ended")




