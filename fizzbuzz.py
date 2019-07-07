##Solving FizzBuzz on numbers 0-10.



for i in range (101):
    if (i) %3 == 0 and (i) %5 == 0:
        i = "FizzBuzz"
        print (i)
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz') 
    else:
        print (i) 
    
 


  
