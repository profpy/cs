min = int(input("Min: "))                  
max = int(input("Max: "))                             
sum = 0                                                                 
divisible = int(input("Divisible: "))                   
for i in range(min,max+1):                               
    if i % divisible == 0:                               
        print(i)                                          
        sum = sum + 1                                     
 print(sum)
