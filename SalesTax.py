#Darrius Singleton SDEV 140
# Excersice 6
purchaseAmt = float(input('What is the purchase amount? '))

# State sales Tax
stateSalesTax = .0500*(purchaseAmt)

# County tax
countySalesTax =.025*(purchaseAmt)

# Total Cost
totalSales = float(purchaseAmt
                  +stateSalesTax
                  +countySalesTax)

def total_cost():
      stateSalesTax=.05*(purchaseAmt)
      countySalesTax =.025*(purchaseAmt)
      total_cost= float(purchaseAmt-countySalesTax-stateSalesTax)
      print('Cost',purchaseAmt)
      print('County tax', countySalesTax)
      print('State tax', stateSalesTax)
      print('totalSales', totalSales)
total_cost()

print ('Darrius Singleton')
total_cost()



