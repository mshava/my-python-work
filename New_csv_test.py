import csv

f = open('sales.csv')

csv_f = csv.reader(f)

def itemMap():
	my_max_val = 0
	products = {}

	for row in csv_f:
		currentItem = row[2]
		numberSold = row[3]

		if not products.has_key(currentItem):
			products[currentItem] = 0
		products[currentItem] += int(numberSold)
	
	return products

def mostPopularProduct(products):
	
	my_max_val = 0
	
	for product,amount in products.items():
	 
	 if amount > my_max_val:
	     
	     my_max_val = amount
	     
	     my_max_key = product

	 mostPopularProduct = {
	     
	     "product":my_max_key,
	     
	     "amount":my_max_val    

}

	return mostPopularProduct
	
results = itemMap()

print mostPopularProduct(results)

"""

def leastPopularProducts(products):
	
	my_min_val = 172
	
	for product,amount in products.items():
		
		if amount < my_min_val:
			
			my_min_val = amount
			
			my_min_key = product
	
	leastPopularProducts = {

		 	  "product":my_min_key,
		
		      "amount":my_min_val
	
}	

	return leastPopularProducts

results = itemMap()

print leastPopularProducts(results)		

"""