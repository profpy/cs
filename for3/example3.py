hours = int(input("Hours: "))                          
speed = int(input("Speed: "))                            
print("Hours\tDistance")                                          
print("-----------------")                               
for x in range(1,hours+1):                              
   print(x,"\t",speed*x)  
