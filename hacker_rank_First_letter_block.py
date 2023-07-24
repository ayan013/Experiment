name="ayan chak"
#print(name[3+1])
new_name=''
i=0
while i < len(name):
    
    if name[i] ==" ":
        
        new_name+=name[i]
        new_name+=name[i+1].upper()
        i=i+1
    else:
        if i == 0:
          new_name+=name[i].upper()
        else:
          new_name+=name[i]
    i=i+1


print(new_name)
    
    
