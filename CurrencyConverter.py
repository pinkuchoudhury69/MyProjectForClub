read=open('Data.txt')

lines=read.readlines()

dict={}

for i in lines:
    data=i.split("\t")
    dict[data[0]]=data[1]

amount=int(input("Enter the amount:\n"))

print("Enter the name of currency you to convert this amount to: ")

[print(k) for k in dict.keys()]

currency=input("Enter one of these values: ")

print(f"{amount} INR is equal to {amount *float(dict[currency])} {currency}")