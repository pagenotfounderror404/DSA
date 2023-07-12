def merge_overlapping_intervals(l):
    global ub, lb
    l.sort()
    for i in range(1,len(l)):
        if l[i][0]<=l[i-1][1]:
            lb=l[i-1][0]
            ub=l[i][1]
            if i==len(l)-1:
                print(f"[{lb},{ub}]")
        else:
            print(f"[{lb},{ub}]", end=" ")


l=[[1,3],[6,8],[2,4],[5,7]]
merge_overlapping_intervals(l)
