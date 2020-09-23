list=[]
a=int(input("HOW MANY ELEMENT YOU WANT TO PRINT IN THIS LIST\n"))
for i in range(a):
    b=int(input(f"Enter your element you want to add in this list{i}\n"))
    list.append(b)
print(list)
print("Enter your choice  1.list comprehension 2.set comprehension 3.dictionary comprehension")
ch=int(input(" "))
if ch==1:
    l1=[x for x in list]
    print(l1)
elif ch==2:
    l2={y for y in list}
    print(l2)
elif ch==3:
    l3={z:f"item {z+1}"for z in list}
    print(l3)

print("Enter choice q quit and c continue\n")
ch1=" "
while(ch1!="q" and ch1!="c"):
 ch1==input( )
 if ch1=="q":
     quit()
 elif ch1=="c":
    continue




