import os
from collections import Counter



#path =r"C:\Users\Administrator\Documents\des"

path = input("Please enter the path \n")
print(path)   
#we shall store all the file names in this list
filelist = []
filext=""
countfile=0
counts =Counter()

for root, dirs, files in os.walk(path):
    print(root)
    
    for file in files:
        
        before_ext,extension = os.path.splitext(file)
        counts[extension] +=1
    for extension,count in counts.items():
         countfile=count
         filext=extension
         
         
        
         filelist.append(os.path.join(f"{extension:8}{count}"))
         print(f"{extension:8}{count}")
         
         
     
        
             
              

f = open("file.html","w")
f.write(str(filelist))
f.close()
        
            
            
           


