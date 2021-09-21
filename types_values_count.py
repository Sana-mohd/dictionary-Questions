# for the dictionary containing differenet types of values
dict={"sana":[1,3],"ali":[2,4],"reena":4}
count=0
total_values=0
for i in dict.values():
    if type(i)==list:
        j=0
        while j<len(i):
            count=count+1
            j=j+1
    else:
        total_values=total_values+1
print(count)
print(total_values)

for k in dict:
    print(dict[k])
