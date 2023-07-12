def minimum_consective_flips(l):
    frag0=0
    frag1=0
    ele=l[0]
    for i in range(1,len(l)):
        if l[i]!=l[i-1] and l[i]==0:
            frag1+=1
        if l[i]!=l[i-1] and l[i]==1:
            frag0+=1

    if l[len(l)-1]==1:
        frag1+=1
    if l[len(l)-1]==0:
        frag0+=1
    if frag1+1==frag0 and frag1==0 or frag0+1==frag1 and frag0==0:
        print("Nothing to change here")
        return
    if frag0>frag1:
        ele=1
    if frag0<frag1:
        ele=0
    if frag0==frag1:
        frag(l,1)
        frag(l,0)
    else:
        frag(l,ele)

def frag(l,ele):
    s=0
    p=0
    print("\n",ele,"\n")
    for i in range(len(l)):
        if l[i]==ele and l[i-1]!=ele:
            s=i
            print(i,end=",")
        if l[i] != ele and l[i - 1] == ele:
            p=i-1
            if i-1<0 or s==p:
                pass
            else:
                print(i-1,end="|")
l=[1,0,0,1,0,1]
minimum_consective_flips(l)