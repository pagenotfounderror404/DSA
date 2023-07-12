def jospehous(number,interval,start=0):



    if number==1:
        return 0


    return ((jospehous(number-1,interval)+interval)%number)+start

n=int(input("Enter n: "))
print(jospehous(5,3))