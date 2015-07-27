import csv

f = open('sales.csv')

csv_f = csv.reader(f)

products = {}

for row in csv_f:
	currentItem = row[2]
	numberSold = row[3]

	if not products.has_key(currentItem):
		products[currentItem] = 0
	products[currentItem] += int(numberSold)
	
print products
PopularProduct = [(value,key)for key,value in products.items()]
print max(PopularProduct)[1]
print min(PopularProduct)[1]