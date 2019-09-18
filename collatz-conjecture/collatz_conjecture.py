
def steps(number):
    step = 0
    while number != 1:
        
        if number % 2 == 1: 
            number = number*3 +1
            step = step + 1
        else:
            number = number/2
            step = step+1
    return step
    
