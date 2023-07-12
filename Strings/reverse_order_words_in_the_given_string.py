def reverse_order_of_words(s):
    l=s.split(" ")
    a=""
    for i in range(len(l)-1,-1,-1):
       a+=l[i]+" "
    print(a)
a="He loves his crush"
reverse_order_of_words(a)