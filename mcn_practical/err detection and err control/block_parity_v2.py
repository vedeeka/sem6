
n=input("Enter data bits: ")
c=int(input("Enter columns: "))
rows=[]
for i  in range(0,len(n),c):
    row = list(n[i:i+c])
    while len(row) < c:
        row.append('0')
    rows.append(row)
    
for row in rows:
    s=0
    for r in row:
        if r=="1":
            s+=1
    if s%2==1:
        row.append('1')
    else :
        row.append('0')

col=[]
for j in range(c+1):
    s=0
    for row in rows:
        if row[j]=="1":
            s+=1
    
    if s%2==1:
        col.append('1')
    else:
        col.append('0')

data=[]
for row in rows:
    data+=row

data+=col
for row in rows:
    print(row)

print("full")
print(data)
