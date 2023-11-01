def calculate(principle,rate,time):
    total_amount=principle*(pow((1+rate/100),time))
    interest=total_amount-principle
    print(interest)
calculate(10000,2,3)    
