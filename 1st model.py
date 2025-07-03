board=[[" " for i in range(0,9)] for j in range(0,9)]


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
            print(f"| {board[i][j]} ",end="")
            if (j+1)%3==0 :
                print("|",end="")
        print()
        if (i+1)%3==0 and i!=8:
            print("_"*40)
            print()


def filter(a):
    filtered = []
    for i in range(9):
        temp = [x for x in a[i] if x != " "]
        filtered.append(temp)
    return filtered



dis()
n=int(input("enter number of known places"))
for i in range (n):
    irow=int(input("Enter the row :  "))
    icol=int(input("enter the column :"))
    value=int(input("Enter the index and value : "))
    board[irow-1][icol-1]=value

dis()
p=filter(sboxes())
print(p)





def checkinput():
    cideal={1,2,3,4,5,6,7,8,9}
    rows=srows()
    columns=scolumns()
    boxes=sboxes()
    for i in range(0,9): 
        if not rows[i] <= cideal:
            return(False)
        if not columns[i] <= cideal:
            return(False)
        if not boxes[i] <= cideal:
            return(False)
    return True

