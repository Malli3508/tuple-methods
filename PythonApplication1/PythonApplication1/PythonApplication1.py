
#take an empty list,insert 5 elements from keyboard, ask user to enter an element from keyboard and delete that element from tuple,
#ask user to enter element from keyboard and print the postion of that element.


x=()
y=[]
for i in range(5):
    y.append(input('enetr an element'))
x=tuple(y)
print(x)
y=list(x)
element=input('enter an element to delete from tuple')
if element in y:
   y.remove(element)
   print(element,'removed successfully')
else:
     print('element not available in the tuple')
y=tuple(y)
print(x)
element=input('enter an element to find postion')
if element in x:
    postion=x.index(element)
    print(element,'found at postion',postion)
else:
    print('element not available in the tuple')
