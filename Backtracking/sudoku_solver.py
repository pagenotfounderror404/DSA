global grid
def isSafe(i,j,n):
    for k in range(len(grid)):
        if grid[k][j]==n or grid[i][k]==n:
            return False
    s=int(len(grid)**0.5)
    rs=i-i%s
    cs=j-j%s
    for i in range(s):
        for j in range(s):
            if grid[i+rs][j+cs]==n:
                return False
    return True



def solve():
    i=0
    j=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==0:
                break
    if i==len(grid) and j==len(grid[i]):
        return True
    for n in range(len(grid)):
        if isSafe(i,j,n):
            grid[i][j]=n
            if solve():
                return True
            grid[i][j]=0
    return False

