from Functions import Functions


class FindProduct:

	# Contains methods to find object in list 

	def checkIfProductExists(productList, productSearch):
		# Obtains the index of the requested object in productList( Only ran if checkIfProductExists method validates parameter prior)
		# Parameters: self (instance), productSearch (str)
		# Returns: productIndex (int)

		productExists = False

		# For statment iterates through an enumerated productList
		for product in productList:

			# If statement checks if current iteration name or sku attribute is equal to the search term (not case-sensitive)
			if product.name.upper() == productSearch.upper() or product.sku == productSearch.upper():
				productExists = True
			# end if

		# end for
		
		return productExists
	# end checkIfProductExists method

	def productIndex(productList, productSearch):
		# Obtains the index of the requested object in productList( Only ran if checkIfProductExists method validates parameter prior)
		# Parameters: self (instance), productSearch (str)
		# Returns: productIndex (int)

		# For statment iterates through an enumerated productList
		for index, product in enumerate(productList):

			# If statement checks if current iteration name or sku attribute is equal to the search term (not case-sensitive)
			if product.name.upper() == productSearch.upper() or product.sku == productSearch.upper():
				productIndex = index
			# end if

		# end for
		
		return productIndex
	# end productIndex method

	
	def searchError():
		# Prints if requested product doesn't exist
		# Parameters: None
		# Return: Null

		print(f'That code or name doesn\'t exist.')

		Functions.enterToContinue()

		return
	# end searchError method