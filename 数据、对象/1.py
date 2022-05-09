matrix=[[1,2,3],[4,5,6],[7,8,9]]
index=[]

n, m = len(matrix), len(matrix[0])
top, bottom, left, right = 0, n-1, 0, m-1
while True:
    for i in range(left:right+1):
        index.append(top,i])
    for i in range(top:bottom+1):
        index.append([i,right])
    for i in range(left:right+1):
        index.append(bottom,right-i])    
    for i in range(top+1:bottom+1):
        index.append([bottom-i,left])
    top, bottom, left, right = top+1, bottom-1, left+1,right-1