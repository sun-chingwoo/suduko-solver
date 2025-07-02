board=[[" " for i in range(0,9)] for j in range(0,9)]


def srows():
    rows=[]
    for i in range(0,9):
        row=[board[i][j] for j in range (9)]
        rows.append(row)
    print(rows)

def scolumns():
    columns=[]
    for j in range(0,9):
        column=[board[i][j] for i in range(9)]
        columns.append(column)
    print(columns)

def sbox():
    boxes=[]
    for m in range (0,9,3):
        for k in range(0,9,3):
            box=[board[i][j] for j in range(k,k+3) for i in range (m,m+3)]
            boxes.append(box)
    print(boxes)


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

dis()
n=int(input("enter number of known places"))
for i in range (n):
    irow=int(input("Enter the row :  "))
    icol=int(input("enter the column :"))
    value=int(input("Enter the index and value : "))
    board[irow-1][icol-1]=value

dis()
sbox()



