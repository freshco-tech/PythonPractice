#Darrius Singleton
#Pyramid- inverted trangle and Triangle
#V1.0 Exercise 5.19 Page 161


#Triangle
rows = int(input("Enter number of rows from 1 to 15: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')

    print(" ")

#inverted Triangle
for i in range(rows + 2, 1, -1):
    for j in range(1, i - 1):
        print(j, end=' ')

    print(" ")