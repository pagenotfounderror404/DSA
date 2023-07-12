def trap_rain(l):
    water_height = 0
    max_left_wall = l[0]
    max_right_wall=max(l[1:])

    for i in range(1,len(l)-1):
        if max_left_wall>l[i]:
            water_height+=min(max_left_wall,max_right_wall)-l[i]
        else:
            max_left_wall=l[i]
            max_right_wall=max(l[i:])
    return water_height


def trap_rain2(l):
    water_height=0
    for i in range(1,len(l)-1):
        water_height=water_height+min(max(l[0:i]),max(l[i:]))-l[i]
    return water_height

l=[3,0,1,2,5]
print(trap_rain2(l))

