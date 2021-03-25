i=1
new_dict={}
while i<=10:
    user_name=input("enter your name: ")
    user_marks=int(input("enter your marks: "))
    new_dict[user_name]=user_marks
    i=i+1
print(new_dict)