def Nmaxelements(dict, N):
    final_dict = {}
    i=0
    while i<N:
        maxi=0
        j=0
        while j<len(dict.keys()):
            if dict.values[j]>maxi:
                maxi=dict.values[j]
            j=j+1
                  
        dict.pop(maxi)
        print(maxi)
        #final_list.append(maxi)
        i=i+1
        
    #print(final_list)
  
# Driver code
dict= {2:6, 41:85, 0:3, 7:6}
N = 2
  
# Calling the function
Nmaxelements(dict, N)