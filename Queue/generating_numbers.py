def generate_numbers(n):
    a=[]
    a.append("5")
    a.append("6")
    for i in range(n):
        p = []
        s=len(a)
        for j in range(s):
            if len(a[j])==len(a[-1]):
                p.append(a[j]+"5")
                p.append(a[j]+"6")
        for k in p:
            a.append(k)
    print(a)
generate_numbers(4)
