def issafe(i,j,s):
    return i<len(s)-1 and j<len(s)-1 and s[i][j]==1

def rat_in_maze(s,i,j):
    sol=[[0]*len(s)]*len(s)
    if i==len(s)-1 and j==len(s)-1:
        sol[i][j]=1
        return True
    if issafe(i,j,s):
        sol[i][j]=1
        if rat_in_maze(s,i+1,j)==True:
            return True
        elif rat_in_maze(s,i,j+1)==True:
            return True
        sol[i][j]=0
    return False



