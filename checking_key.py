dict={"name":"Raju", "marks":56}
key=input("enter your key: ")
if key in dict.keys():
    print("exist")
else:
    print("not exist")



def checkKey(dict, key):
      
    if key in dict.keys():
        print("exist")
    else:
        print("not exist")
dict = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dict, key)
  