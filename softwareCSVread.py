import csv
jsonObject = {}
with open('softwear.csv', newline = '') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for index, row in enumerate(reader):
		if index == 0:
			for index, elem in enumerate(row):
				if elem == 'product_title':
					prodTitle = index
				elif elem == 'product_type':
					prodType = index
				elif elem == 'variant_title':
					variantTitle = index
				elif elem == 'net_quantity':
					quantityTitle = index
		else:
			if row[prodType] in jsonObject:
				prods = jsonObject[row[prodType]]
				if row[prodTitle] in prods:
					jsonObject[row[prodType]][row[prodTitle]][row[variantTitle]] = int(row[quantityTitle])
				else:
					jsonObject[row[prodType]][row[prodTitle]] = {}
					jsonObject[row[prodType]][row[prodTitle]][row[variantTitle]] = int(row[quantityTitle])				
			else:
				jsonObject[row[prodType]] = {}
				jsonObject[row[prodType]][row[prodTitle]] = {}
				jsonObject[row[prodType]][row[prodTitle]][row[variantTitle]] = int(row[quantityTitle])
				


	for elem in jsonObject:
		products = jsonObject[elem]
		for product in products:
			sizes = products[product]
			totalCount = 0
			for size in sizes:
				quantity = sizes[size]
				totalCount += quantity
			sizes['Total Quantity'] = totalCount
	print(jsonObject)

		