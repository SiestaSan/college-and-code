#code for investmant calculator
#T-Level Sample Assessmnet Material (Task 2)
#Non working code


#define a function to ask for basic inputs    
def opening ():
    print('#####################################')
    print('Welcome to the investment quote system')
    print('')
    print('Please enter your name') #ask for the users name
    opening.name = input()
    
    print('Please enter your Address') #ask for the users address
    opening.address = input()
    
    print ('Please eneter your telephone number') #ask for the users telephone number
    opening.phone = input()
    
    print ('How much would you like to invest per month (£)?') #ask for the users investment amount
    opening.investSum = float(input()) #initialise the investment in a float variable under opening.investSum
    
#define a function named options
def options ():
    print('#####################################')
    print('There are two types of investment available:')
    print('Option 1 - Savings plan')
    print('Option 2 - Managed stock investment')
    print('Please select an option (press 1 or 2 followed by enter)')
    print('#####################################')
    
    option = input() #ask the user to decide how they're going to manage their savings
          
    #force the user to input either 1 or 2
    while option != '1' and option != '2':
        print('Please select an option (press 1 or 2 followed by enter)')
        
        option = input()
        
    #if the user chose to run the savings calc, run the savings calc, else run the stocks calc
    if option == '1':
        savingsMain()
    else:
        stocksMain()
        
#define a function that runs the savings calc
def savingsMain():
    savingsMain.monthlyInvest = opening.investSum 
    savingsMain.yearlyInvest = savingsMain.monthlyInvest * 12 #convert the monthly investments to an annual investment
    
    #force the user to give an investment between 0 and 20,000
    while savingsMain.yearlyInvest > 20000:
        print('The the initial monthly amount is too high for this type of plan' )
        print ('How much would you like to invest per month (£)?')
        savingsMain.monthlyInvest = float(input())
        savingsMain.yearlyInvest = savingsMain.monthlyInvest * 12
        
        
    while savingsMain.yearlyInvest < 0:
        print('The the initial monthly amount has to be greater than 0' )
        print ('How much would you like to invest per month (£)?')
        savingsMain.monthlyInvest = float(input())
        savingsMain.yearlyInvest = savingsMain.monthlyInvest * 12
    savingsPrint()
    
    

def savingsMin():
    predictReturns = 0.012 #minimal predicted returns through the savings plan
    yearlyFees = 0.0025 * 12 #overall yearly fee by multiplying the monthly fee by 12
    savingsMin.total = savingsMain.yearlyInvest
    print('#####################################')   
    print('Forecasted perfromance of this plan at the lowest rate of return:')
    
    for i in range(10):
        savingsMin.total = (savingsMin.total + (savingsMin.total * predictReturns)) - yearlyFees #calculates the overall amount made that year
        
        #displays the profit at each significant year with suitable messages
        if i == 0 or i == 4 or i == 9:
            print('At the end of year', str(i+1))
            print('Your investment will be worth:')
            print('£', round(savingsMin.total, 2), sep = '')
            print('')
            print('Total fees paid in this period: £', round(yearlyFees * (i+1), 2), sep = '')
            print('')
            print('Total profit in this period: £', round(savingsMin.total - (yearlyFees * (i+1)), 2), sep = '')
            print('')
    print('#####################################')
    print('')

def savingsMax():
    predictReturns = 0.024 #maximal predicted returns through the savings plan
    yearlyFees = 0.0025 * 12 #overall yearly fee by multiplying the monthly fee by 12
    savingsMax.total = savingsMain.yearlyInvest
    print('#####################################')
    print('Forecasted perfromance of this plan at the highest rate of return::')
    
    for i in range(10):
        savingsMax.total = (savingsMax.total + (savingsMax.total * predictReturns)) - yearlyFees #calculates the overall profit made that year
        
        #displays important info for each significant year
        if i == 0 or i == 4 or i == 9:
            print('At the end of year', str(i+1))
            print('Your investment will be worth:')
            print('£', round(savingsMax.total,2), sep = '')
            print('')
            print('Total fees paid in this period: £', round(yearlyFees * (i+1), 2), sep = '')
            print('')
            print('Total profit in this period: £', round(savingsMax.total - (yearlyFees * (i+1)), 2), sep = '')
            print('')
    print('#####################################')  
    print('')

#defines a function that creates important features for the stocks calc
def stocksMain():
    stocksMain.monthlyInvest = opening.investSum
    stocksMain.yearlyInvest = stocksMain.monthlyInvest * 12 #turns monthly investment into yearly investments by multiplying by 12
    
    stocksPrint() #runs the stocksPrint function
    
    #defines a function that will run all the necessary procedures for the minimum stocks calc amount
def stocksMin():
    predictReturns = 0.04 #minimum stocks predicted profit
    yearlyFees = 0.13 * 12 
    
    stocksMin.total = stocksMain.yearlyInvest
    print('#####################################')   
    print('Forecasted perfromance of this plan at the lowest rate of return:')
    
    #calculates the overall profit for this year without tax added on
    for i in range(10):
        stocksMin.total = (stocksMin.total + (stocksMin.total * predictReturns)) - yearlyFees
        
        #decides how much tax if any should be added on
        if stocksMin.total >= 40000:
            taxRate = 0.2
        elif stocksMin.total >= 12000:
            taxRate = 0.1
        else:
            taxRate = 0
        
        #adds effects of tax
        taxPayable = stocksMin.total * taxRate
        postTax = stocksMin.total - taxPayable
        
        #displays the profit at each significant year with suitable messages
        if i == 0 or i == 4 or i == 9:
            print('At the end of year', str(i+1))
            print('Your investment will be worth:')
            print('£', round(postTax, 2), sep = '')
            print('')
            print('Total fees paid in this period: £', round(yearlyFees * (i+1), 2), sep = '')
            print('')
            print('Total profit in this period: £', round(postTax - (yearlyFees * (i+1)), 2), sep = '')
            print('')
            print('Total tax due in this period: £', round(taxPayable, 2), sep = '')
            print('')
    print('#####################################')
    print('') 

#defines a function that will run all the necessary procedures for the maximum stocks calc amount
def stocksMax():
    predictReturns = 0.23 #maximum stocks predicted profit
    yearlyFees = 0.13 * 12
    stocksMax.total = stocksMain.yearlyInvest
    print('#####################################')   
    print('Forecasted perfromance of this plan at the higher rate of return:')
    
    #calculates the overall profit for this year without tax added on
    for i in range(10):
        stocksMax.total = (stocksMax.total + (stocksMax.total * predictReturns)) - yearlyFees
        
        #decides how much tax if any should be added on
        if stocksMax.total >= 40000:
            taxRate = 0.2
        elif stocksMax.total >= 12000:
            taxRate = 0.1
        else:
            taxRate = 0
        
        #adds effects of tax
        taxPayable = stocksMin.total * taxRate
        postTax = stocksMin.total - taxPayable
        
        #displays the profit at each significant year with suitable messages      
        if i == 0 or i == 4 or i == 9:
            print('At the end of year', str(i+1))
            print('Your investment will be worth:')
            print('£', round(postTax, 2), sep = '')
            print('')
            print('Total fees paid in this period: £', round(yearlyFees * (i+1), 2), sep = '')
            print('')
            print('Total profit in this period: £', round(postTax - (yearlyFees * (i+1)), 2), sep = '')
            print('')
            print('Total tax due in this period: £', round(taxPayable,2), sep = '')
            print('')
    print('#####################################')
    print('') 

#prints the given info at the beginning
def savingsPrint ():
    print('--------------------------------------------------------')
    print('Personal Investment Quote for:')
    print('Name: ', opening.name)
    print('')
    print('Telephone Number: ', opening.phone)
    print('--------------------------------------------------------')
    print('')
    print('You selected a savings plan')
    savingsMin() #runs the savingsMin function
    savingsMax() #runs the savingsMax function

#prints the given info at the beginning
def stocksPrint ():
    print('--------------------------------------------------------')
    print('Personal Investment Quote for:')
    print('Name: ', opening.name)
    print('')
    print('Telephone Number: ', opening.phone)
    print('--------------------------------------------------------')
    print('')
    print('You chose a Managed Stock Investment plan')
    stocksMin() #runs the stocksMin function
    stocksMax() #runs the stocksMax function


opening()
options()