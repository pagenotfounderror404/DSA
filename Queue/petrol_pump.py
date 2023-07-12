def petrol_pump(p,d):
    for i in range(len(p)):
        pc=0
        if p[i]>=d[i]:
            for j in range(i,len(p)):
                pc+=p[j]
                pc-=d[j]
                if pc<=0:
                    break
            if pc>0:
                for j in range(i):
                    pc += p[j]
                    pc -= d[j]
                    if pc <= 0:
                        break
                if pc > 0:
                    print(i+1)
                    return
    print("-1")
    return
def petrol_pump_efficient(p,d):
    start=0
    curr=0
    prev=0
    for i in  range(len(p)):
        curr+=p[i]-d[i]
        if curr<0:
            start=i+1
            prev+=curr
            curr=0
    if curr+prev>=0:
        print(start+1)
    else:
        print(-1)
l=[50,10,60,100]
p=[30,20,100,10]
petrol_pump_efficient(l,p)


