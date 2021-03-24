 

res = {}
def list_to_dict(list1,list2):
    for key in list1:
        for value in list2:
            res[key] = value
            list2.remove(value)
            break
    return res
list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
print(list_to_dict(list1,list2))
