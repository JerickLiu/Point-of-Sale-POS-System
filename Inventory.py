from Functions import Functions
from FindProduct import FindProduct
from Menu import Menu
from Outputs import Outputs

class Inventory:
	# Inventory Class is a class for products to obtain their respective attributes
	#  > Attributes are: sku, name, category, quantity, minQuantity, vendorPrice, markUpPercent, salePercent, profit, warning, regPrice, and currentPrice

	def __init__(self, sku, name, category, quantity, minQuantity, vendorPrice, markUpPercent, salePercent):

		self.sku = sku
		self.name = name
		self.category = category
		self.quantity = int(quantity)
		self.minQuantity = int(minQuantity)
		self.vendorPrice = float(vendorPrice)
		self.markUpPercent = int(markUpPercent)
		self.salePercent = int(salePercent)

		return
	# end __init__ method

	def __str__(self):
		# Prints a formatted view of product displaying name, sku, price, profit, quantity, and min. qty.

		price = f'{(self.vendorPrice * (1 + (self.markUpPercent / 100)) * (1 - self.salePercent / 100)):.2f}'
		profit = f'{float(price) - self.vendorPrice:.2f}'
		
		return (f"\n\n{'Product:':>15}\t{self.name} ({self.sku})\n\n{'Price:':>15}\t${(price):>5}\n{'Profit:':>15}\t${profit:>5}\n{'Quantity:':>15}\t{self.quantity:>5}\n{'Min Quantity:':>15}\t{self.minQuantity:>5}\n")
	# end __str__ method

	# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #
	# Attributes profit, warning, regPrice, currentPrice use the property decorater as values change and rely on calculations
	# Parameters: self (instance)
	# Returns: accurate product attributes

	@property
	def profit(self):
		# Profit determined by subtracting currentPrice by vendorPrice
		return abs(self.currentPrice - self.vendorPrice)
	# end profit
	
	@property
	def warning(self):
		# Warning is a flag to identify if a product is low on quantity
		return True if self.quantity <= self.minQuantity else False
	# end warning 
	
	@property
	def regPrice(self):
		# RegPrice determined by multiplying vendorPrice by the markUpPercent
		return round(self.vendorPrice * (1 + (self.markUpPercent / 100)), 2)
	# end regPrice

	@property
	def currentPrice(self):
		# CurrentPrice determined by multiplying the regPrice by the salePercent
		return round(self.regPrice * (1 - (self.salePercent / 100)), 2)
	# end currentPrice

	# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #
	
	# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #
	# These methods individually update either the name, min.Qty, vendorPrive, markUp, or salePercent attribute after confirming that the values are appropiate

	def updateName(self, newName):
		# Upon modifying product name, this method saves it to that particular class object
		# Parameters: self (Instance), newName (str)
		# Returns: Null

		self.name = newName
		return
	# end updateName method

	def updateMinQuantity(self, newMinQty):
		# Upon modifying product min.Qty, this method saves it to that particular class object
		# Parameters: self (Instance), newMinQty (int)
		# Returns: Null

		self.minQuantity = int(newMinQty)
		return
	# end updateMinQuantity meethod

	def updateVendorPrice(self, newVP):
		# Upon modifying product vendorPrice, this method saves it to that particular class object
		# Parameters: self (Instance), newMinQty (float)
		# Returns: Null

		self.vendorPrice = float(newVP)
		return
	# end updateVendorPrice method
	
	def updateMarkUpPercent(self, newMP):
		# Upon modifying product markUp Percent, this method saves it to that particular class object
		# Parameters: self (Instance), newMP (int)
		# Returns: Null

		self.markUpPercent = int(newMP)
		return
	# end updateMarkUpPercent method
	
	def updateSalePercent(self, newSP):
		# Upon modifying product salePercent, this method saves it to that particular class object
		# Parameters: self (Instance), newSP (int)
		# Returns: Null

		self.salePercent = int(newSP)
		return
	# end updateSalePercent method
	
	# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #
# end Inventory Class


class InventoryMenu(Inventory):

	# Class InventoryMenu contains a list of all products as objects of the Inventory class and methods for inventory control

	def __init__(self, productList):
		self.productList = productList

		return
	# end __init__ method

	
	def inventoryMenu(self):
		# inventoryMenu Method navigates through all inventory methods
		# Parameters: self (instance)
		# Returns: an updated productList (list)
		
		# Boolean variable tracking if user wants to go back to Main Menu
		exit = False

		while not exit:

			userChoice = Menu('Inventory Control', 'Print a Report', 'Restock Product Quantities', 'Add an Item', 'Remove an Item', 'Modify an Item', 'Apply a Sale', 'Back to Main Menu').menu()

			if userChoice == '1':
				# User chooses to view product reports
				self.productReportMenu()
			
			elif userChoice == '2':
				# User chooses to restock product quantities
				self.reOrderStockMenu()
			
			elif userChoice == '3':
				# User chooses to add a product
				self.addProduct()
			
			elif userChoice == '4':
				# User chooses to remove a product
				self.removeProduct()
			
			elif userChoice == '5':
				# User chooses to modify a product
				self.modifyProductMenu()
			
			elif userChoice == '6':
				# User chooses to apply sales
				self.applySaleMenu()
			
			elif userChoice == '7':
				# User chooses to return to main menu (Boolean evaluates to True)
				exit = Functions.confirmSelection('\n\nBack to Main Menu', 'Inventory Control')
			# end if
		# end while

		# Changes are updated and returned to the productList in main
		return self.productList
	# end inventoryMenu method


	def productReportMenu(self):
		# Obtains User choice and navigates through Reports Class
		# Parameters: self (instance)
		# Return: Null

		# Boolean variable tracking if user wants to keep reporting
		doneReporting = False

		while not doneReporting:

			# Creates Outputs Class to control printing of abundance of outputs
			outputManager = Outputs(0)

			# User chooses to report based on individual product, category, max qty, warning indicator, or quit menu
			userChoice = Menu('Based on what Criteria?', 'SKU / Product Name', 'Category', 'Products under inputted Quantity', 'Products under Minimum Quantity (Warning Indicator)', 'All Items', 'Back').menu()

			# User chooses to report based on individual product
			if userChoice == '1':

				self.getReportProduct(outputManager)

			# User chooses to report based on category
			elif userChoice == '2':

				self.getReportCategory(outputManager)
			
			# User chooses to report based on max qty
			elif userChoice == '3':

				# Calls Reports method criteriaQuantity
				Reports.criteriaQuantity(self.productList, outputManager)
			
			# User chooses to report based on warning indicator
			elif userChoice == '4':

				# Calls Reports method criteriaMinQty
				Reports.criteriaMinQty(self.productList, outputManager)
			
			# User chooses to report based on all items
			elif userChoice == '5':

				# Calls Reports method criteriaAll
				Reports.criteriaAll(self.productList, outputManager)
			
			# User chooses to return to Inventory Menu
			elif userChoice == '6':

				# Boolean evaluates to True
				doneReporting = True
			# end if
	
		return
	# end productReportMenu


	def reOrderStockMenu(self):
		# Obtains User choice and navigates code in order to restock products
		# Parameters: self (instance)
		# Return: Null

		# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #
		# Restocking must result in new quantity to exceed min. qty per product.
		# If fails, no changes will be made to product quantity
		# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––– #
		
		# User chooses to restock by individual product, minimum qty., products with a warning flag, or return to menu
		userChoice = Menu('Add Product Quantity by', 'Individual Product', 'Minimum Quantity', 'Warning Indicator (all less than r. qty)', 'Quit').menu()

		# User chooses to restock an individual product
		if userChoice == '1':

			self.getIndividualRestockAmt()

		# User chooses to restock by min. qty.
		elif userChoice == '2':

			# Calls reOrderStockUnderQty method
			self.reOrderStockUnderQty()

		# User chooses to restock by warning indicator
		elif userChoice == '3':

			# Calls reOrderWarningQty method
			self.reOrderWarningQty()
		# end if
		
		return
	# end reOrderStockMenu method


	def addProduct(self):
		# Allows for the adding of a product 
		# Parameters: self (instance)
		# Returns: Null

		# Calls getProductSpecifications method to obtain all the properties of the new product
		addName, addCategory, addSKU, addQuantity, addMinQty, addVendorPrice, addMarkUp, addSalePercent = self.getProductSpecifications()

		# If statement checks if the new name already exists > No changes made
		if FindProduct.checkIfProductExists(self.productList, addName):

			Functions.clearScreen(f'{addName} already exists as a product.\nNo product has been added.')

		else:
			# Else occurs if it's an available name

			# If statement calls confirmSelection method to print a formatted view of the new product and asks if user confirms
			if Functions.confirmSelection(self.formattedAddProduct(addSKU, addName, addQuantity, addMinQty, addVendorPrice, addMarkUp, addSalePercent)):
			
				# Creates a new Inventory object
				newProduct = Inventory(addSKU, addName, addCategory, addQuantity, addMinQty, addVendorPrice, addMarkUp, addSalePercent)

				# Calls appendCorrectly method to append it to the right spot in productList
				self.appendCorrectly(addCategory, addSKU, newProduct)

				Functions.clearScreen(f'\n\nProduct {addName} has been added.')
			
			else:
				# Else occurs if user doesn't confirm product > No changes made
				Functions.clearScreen('\n\nNo product has been added.')
			# end if
		# end if

		Functions.enterToContinue()

		return
	# end addProduct method


	def removeProduct(self):
		# Allows for the deletion of a product in the productList
		# Parameters: self (instance)
		# Returns: Null

		# User chooses between removing a product by search (individual), batch (category), or returning to menu
		userChoice = Menu('Remove a Product by:', 'Name / SKU', 'Category', 'Quit').menu()

		# User chooses remove by search
		if userChoice == '1':

			self.removeIndividualProduct()
		
		# User chooses to remove products by category
		elif userChoice == '2':

			self.getCategoryToRemove()
		# end if

		return
	# end removeProduct method


	def modifyProductMenu(self):
		# Allows for modification of select individual attributes (name, vendor price, markup, sale, min. qty)
		# Parameters: self (instance)
		# Returns: Null

		# Calls loopTillValid method and obtains user requested product 
		userProduct = Functions.loopTillValid('Enter the product name or SKU to modify:\t', 'any', 'Modify a Product')

		# If statement calls checkIfProductExists method and checks if the product is in the productList
		if FindProduct.checkIfProductExists(self.productList, userProduct):

			# User decides to modify one of name, vendor price, markup, sale percent, min. qty.
			userChoice = Menu(f'{self.productList[FindProduct.productIndex(self.productList, userProduct)]}\n\tAttribute to Adjust?', 'Product Name', 'Vendor Price', 'Mark Up Percent', 'On Sale Percent', 'Minimum Quantity', 'Quit').menu()

			# User chooses to modify name
			if userChoice == '1':
				
				self.modifyProductName(userProduct)

			# User chooses to modify vendor price
			elif userChoice == '2':

				self.modifyProductVendor(userProduct)

			# User chooses to modify markup percent
			elif userChoice == '3':

				self.modifyProductMarkup(userProduct)

			# User chooses to modify sale percent
			elif userChoice == '4':

				self.modifyProductSale(userProduct)
		
			# User chooses to modify min. qty.
			elif userChoice == '5':

				self.modifyProductMinQty(userProduct)
			# end if

		else:
			# Else occurs if user requested product doesn't exits
			FindProduct.searchError()
		# end if
		
		return
	# end modifyProductMenu method


	def applySaleMenu(self):
		# Menu to allow user to apply sales to products
		# Parameters: self (instance)
		# Returns: Null

		# User decides to discount items by search (individual), or by batch (category)
		userChoice = Menu('Apply sale to:', 'Individual Product', 'Category', 'Quit').menu()

		# User decides individual
		if userChoice == '1':

			# Calls applyIndividualSale method
			self.applyIndividualSale()
				
		# User decides batch discount
		elif userChoice == '2':

			# Calls applyBatchDiscount method
			self.applyBatchDiscount()
		# end if

		return
	# end applySaleMenu method


	def getProductSpecifications(self):
		# Obtains the specifications for a product the user wants to add
		# Parameters: self (instance)
		# Returns: addName (str), addCategory(str), addSKU(str), addQuantity(int), addMinQty(int), addVendorPrice(float), addMarkUp(int), addSalePercent (int)

		# Calls loopTillValid method to obtain new name
		addName = Functions.loopTillValid('Enter the new product name:\t', 'alphabetic', 'Adding a Product')

		# User chooses between categories Fruit, Vegetables, Meat, or Other for the new product
		addCategory = Menu(f'What category is {addName} in?', 'Fruit', 'Vegetables', 'Meat', 'Other').menu()

		addCategory = self.convertCategory(addCategory)

		# Calls makeSKU method to determine appropiate SKU (in correlation to category)
		addSKU = self.makeSKU(addCategory)

		# Calls getQuantity method to get proper quantity values
		addQuantity, addMinQty = self.getQuantity(addName)

		# Calls getPrice method to get proper price values
		addVendorPrice, addMarkUp, addSalePercent = self.getPrice(addName)

		return addName, addCategory, addSKU, addQuantity, addMinQty, addVendorPrice, addMarkUp, addSalePercent
	# end getProductSpecifications method


	def getPrice(self, addName):
		# Obtains a vendor price, mark up percentage, and sale percentage from the user that satisfies price >= vendor price
		# Parameters: self (instance), addName (str)
		# Returns: addVendorPrice (float), addMarkUp (int), addSalePercent (int)

		# Boolean varaible will continuously loop until the user inputs percentages that make the price higher than vendor price
		discountTest = False

		while not discountTest:

			addVendorPrice = float(Functions.loopTillValid(f'Enter the vendor price of {addName}:\t$ ', 'float', 'Adding a Product'))

			addMarkUp = int(Functions.loopTillValid(f'Enter the markup percentage of {addName}:\t% ', 'integer', 'Adding a Product'))

			addSalePercent = int(Functions.loopTillValid(f'Note: Discount price cannot be lower than vendor price.\nEnter the discount percentage of {addName} (0 for none):\t% ', 'integer', 'Adding a Product'))

			#  Calls priceHigherThanVendor method to determine if values are valid
			discountTest = self.priceHigherThanVendor(addVendorPrice, addMarkUp, addSalePercent)

			if not discountTest:
				Functions.clearScreen(f'{f"! Discount Failed !":^75}\n\nReason: A discount percentage of {addSalePercent}% will make the price (${(addVendorPrice * (1 + (addMarkUp / 100)) * (1 - addSalePercent / 100)):.2f}) lower than the vendor price (${addVendorPrice:.2f}).\nPlease adjust the vendor price, markup percentage, and discount percentage.')

				Functions.enterToContinue()
			# end if
		# end while

		return addVendorPrice, addMarkUp, addSalePercent
	# end getPrice method


	def getQuantity(self, addName):
		# Obtains a quantity and minimum quantity from the user that satisfies qty > min. qty
		# Parameters: self (instance), addName (str)
		# Returns: addQuantity (int), addMinQty (int)

		# Boolean variable will continuously loop until the user inputs a quantity amount higher than the min. qty.
		goodQuantity = False

		while not goodQuantity:
			addQuantity = int(Functions.loopTillValid(f'Enter the quantity of {addName}:\t', 'integer', 'Adding a Product'))

			addMinQty = int(Functions.loopTillValid(f'Enter the minimum quantity {addName} should be over:\t', 'integer', 'Adding a Product'))
			
			if addQuantity > addMinQty:
				goodQuantity = True
			# end if

			if not goodQuantity:
				Functions.clearScreen(f'{f"! Quantity Failed !":^75}\n\nReason: Ensure the quantity of the item is greater than the minimum quantity. Please try again.')

				Functions.enterToContinue()
			# end if
		# end while

		return addQuantity, addMinQty
	# end getQuantity method

	
	def applyIndividualSale(self):
		# Allows the user to apply a sale percentage to a select product
		# Parameters: self (instance)
		# Return: Null

		# Calls loopTillValid method to obtain user requested product
		userProduct = Functions.loopTillValid('Enter the product name or SKU to modify:\t', 'any', 'Modify a Product')

		# If statement calls checkIfProductExists method to see if product exists
		if FindProduct.checkIfProductExists(self.productList, userProduct):
			
			# Calls loopTillConfirmed method to obtain user requested sale percent
			userSale = int(Functions.loopTillConfirmed('Enter the discount percent to apply:\t% ', 'integer', f'Current Sale % of {self.productList[FindProduct.productIndex(self.productList, userProduct)].name}: {self.productList[FindProduct.productIndex(self.productList, userProduct)].salePercent}%'))

			# While statement calls priceHigherThanVendor method and loops until the price is higher than the vendor
			while not self.priceHigherThanVendor(float(self.productList[FindProduct.productIndex(self.productList, userProduct)].vendorPrice), int(self.productList[FindProduct.productIndex(self.productList, userProduct)].markUpPercent), int(userSale)):
				
				# Prints error message
				Functions.clearScreen(f'{f"! Discount Failed !":^75}\n\nReason: A sale percent of {userSale}% will make the price (${(float(self.productList[FindProduct.productIndex(self.productList, userProduct)].regPrice) * (1 - int(userSale) / 100)):.2f}) lower than the vendor price (${float(self.productList[FindProduct.productIndex(self.productList, userProduct)].vendorPrice):.2f}).\nPlease try again.')

				Functions.enterToContinue()
				
				# User continually inputs a sale percentage until the price is higher than the vendor price
				userSale = int(Functions.loopTillConfirmed('Enter the discount percent to apply:\t% ', 'integer', f'Current Sale % of {self.productList[FindProduct.productIndex(self.productList, userProduct)].name}: {self.productList[FindProduct.productIndex(self.productList, userProduct)].salePercent}%'))
			# end while
			
			# Object calls updateSalePercent method to update it's attribute
			self.productList[FindProduct.productIndex(self.productList, userProduct)].updateSalePercent(userSale)

			# Prints success message
			Functions.clearScreen(f'Sale percent has been changed successfully. New {self.productList[FindProduct.productIndex(self.productList, userProduct)].name} Sale Price: ${self.productList[FindProduct.productIndex(self.productList, userProduct)].currentPrice:.02f}')

			Functions.enterToContinue()

		else:
			# Else occurs when product doesn't exist
			FindProduct.searchError()
		# end if

		return
	# end applyIndividualSale method


	def applyBatchDiscount(self):
		# Allows the user to apply a sale percentage to a select category
		# Parameters: self (instance)
		# Return: Null

		# Variable obtains the category requested to discount
		userCtgy = Menu(f'What category would you like to discount?', 'Fruit', 'Vegetables', 'Meat', 'Other', 'Quit').menu()

		# If statement is true as long as user doesn't choose to exit
		if not userCtgy == '5':

			# Creates Outputs object to track maximum outputs to screen
			outputManager = Outputs(0)

			userCtgy = self.convertCategory(userCtgy)

			# Calls loopTillConfirmed method to obtain requested discount percentage
			userSale = Functions.loopTillConfirmed('Any products that will be priced lower than the vendor price due to the discount will be unchanged.\n\nEnter the discount percent to apply (0 to remove all discounts):\t% ', 'integer', f'Applying Sale to {userCtgy.title()}')
			
			# For statement iterates through every product on the productList
			for product in self.productList:

				# If statement checks if the current iteration is the same category as what was inputted prior
				if product.category == userCtgy:

					# Nested if statement checks if the updated sale percentage will keep the price above the vendor price
					if self.priceHigherThanVendor(float(product.vendorPrice), int(product.markUpPercent), int(userSale)):

						outputManager.updateCounter()

						# Calls updateSalePercent method to update the respective product's attribute
						product.updateSalePercent(userSale)

						print(f'{f"{product.name[:20]} has been discounted to ${product.currentPrice:.02f}.":^50}')
					
					else:
						# Else product doesn't update if the sale percentage will make individual item lower than vendor price
						outputManager.updateCounter()

						print(f'{f"No changes have been made to {product.name[:20]}.":^50}')
					# end if
				# end if
			# end for
			
			Functions.enterToContinue()
	
		return
	# end applyBatchDiscount method


	def modifyProductName(self, userProduct):
		# Allows user to input a potential name to rename the product
		# Parameters: self (instance), userProduct (str)
		# Return: Null

		# Calls loopTillConfirmed method to obtain requested new product name
		newName = Functions.loopTillConfirmed('Enter the new product name:\t', 'alphabetic', 'Change Product Name')

		# If statement calls checkIfProductExists method and checks if the name isn't taken (in the productList)
		if not FindProduct.checkIfProductExists(self.productList, newName):

			# Calls updateName method to update respective object's attribute
			self.productList[FindProduct.productIndex(self.productList, userProduct)].updateName(newName)

			Functions.clearScreen('Name successfully changed!')

			Functions.enterToContinue()
		
		else:
			# Else occurs if name already exists > No changes made.
			Functions.clearScreen(f'A product with name {newName} already exists.\nPlease try again later.')

			Functions.enterToContinue()
		# end if

		return
	# end modifyProductName method


	def modifyProductVendor(self, userProduct):
		# Allows user to input a potential vendor price for the product
		# Parameters: self (instance), userProduct (str)
		# Return: Null

		# Calls loopTillConfirmed method and obtains user requested vendor price
		newVP = float(Functions.loopTillConfirmed('Enter the new vendor price:\t$ ', 'float',f'Current {self.productList[FindProduct.productIndex(self.productList, userProduct)].name} Vendor Price: ${self.productList[FindProduct.productIndex(self.productList, userProduct)].vendorPrice:.2f}'))

		# Calls updateVendorPrice method to update respective object's attribute (no need to check if price is valid as all prices are adjusted in retrospect of the vendor price)
		self.productList[FindProduct.productIndex(self.productList, userProduct)].updateVendorPrice(round(newVP, 2))


		Functions.clearScreen(f'The vendor price for {self.productList[FindProduct.productIndex(self.productList, userProduct)].name} is now ${self.productList[FindProduct.productIndex(self.productList, userProduct)].vendorPrice:.2f}')

		Functions.enterToContinue()

		return
	# end modifyProductVendor method


	def modifyProductMarkup(self, userProduct):
		# Allows user to input a potential markup percentage for the product
		# Parameters: self (instance), userProduct (str)
		# Return: Null

		# Calls loopTillConfirmed method and obtains requested markup percent
		newMP = int(Functions.loopTillConfirmed('Enter the new markup percent:\t% ', 'integer',f'Current {self.productList[FindProduct.productIndex(self.productList, userProduct)].name} Markup %: {self.productList[FindProduct.productIndex(self.productList, userProduct)].markUpPercent}%'))

		# If statement calls priceHigherThanVendor method and checks if price will be higher than the vendor price
		if self.priceHigherThanVendor(self.productList[FindProduct.productIndex(self.productList, userProduct)].vendorPrice, newMP, self.productList[FindProduct.productIndex(self.productList, userProduct)].salePercent):
			
			# Calls updateMarkUpPercent method to update respective object's attribute
			self.productList[FindProduct.productIndex(self.productList, userProduct)].updateMarkUpPercent(newMP)

			Functions.clearScreen(f'The markup percent for {self.productList[FindProduct.productIndex(self.productList, userProduct)].name} is now {self.productList[FindProduct.productIndex(self.productList, userProduct)].markUpPercent}%')

			Functions.enterToContinue()

		else:
			# Else occurs if price will be lower than vendor price

			Functions.clearScreen(f'{f"! Modification Failed !":^75}\n\nReason: A markup percent of {newMP}% will make the price (${(float(self.productList[FindProduct.productIndex(self.productList, userProduct)].vendorPrice) * (1 + newMP / 100) * (1 - int(self.productList[FindProduct.productIndex(self.productList, userProduct)].salePercent) / 100)):.2f}) lower than the vendor price (${float(self.productList[FindProduct.productIndex(self.productList, userProduct)].vendorPrice):.2f}).\nPlease try again later.')

			Functions.enterToContinue()
		# end if

		return
	# end modifyProductMarkup method


	def modifyProductSale(self, userProduct):
		# Allows user to input a potential sale percentage for the product
		# Parameters: self (instance), userProduct (str)
		# Return: Null

		# Calls loopTillConfirmed method to obtain requested sale %
		newSP = int(Functions.loopTillConfirmed('Enter the new sale percent:\t% ', 'integer',f'Current {self.productList[FindProduct.productIndex(self.productList, userProduct)].name} Sale %: {self.productList[FindProduct.productIndex(self.productList, userProduct)].salePercent}%'))

		# If statement checks if updated price will be higher than vendor price
		if self.priceHigherThanVendor(float(self.productList[FindProduct.productIndex(self.productList, userProduct)].vendorPrice), int(self.productList[FindProduct.productIndex(self.productList, userProduct)].markUpPercent), newSP):

			# Calls updateSalePercent method to update respective object's attribute
			self.productList[FindProduct.productIndex(self.productList, userProduct)].updateSalePercent(newSP)

			Functions.clearScreen(f'The sale percent for {self.productList[FindProduct.productIndex(self.productList, userProduct)].name} is now {self.productList[FindProduct.productIndex(self.productList, userProduct)].salePercent}%')

			Functions.enterToContinue()

		else:
			# Else occurs when updated price will be lower than vendor price. No changes made.

			Functions.clearScreen(f'{f"! Modification Failed !":^75}\n\nReason: A sale percent of {newSP}% will make the price (${(float(self.productList[FindProduct.productIndex(self.productList, userProduct)].vendorPrice) * (1 + int(self.productList[FindProduct.productIndex(self.productList, userProduct)].markUpPercent) / 100) * (1 - newSP / 100)):.2f}) lower than the vendor price (${float(self.productList[FindProduct.productIndex(self.productList, userProduct)].vendorPrice):.2f}).\nPlease try again later.')

			Functions.enterToContinue()
		# end if

		return
	# end modifyProductSale


	def modifyProductMinQty(self, userProduct):
		# Allows user to input a potential min qty for the product
		# Parameters: self (instance), userProduct (str)
		# Return: Null

		# Calls loopTillConfirmed method to obtain requested min. qty.
		newMQty = int(Functions.loopTillConfirmed('Enter the new minimum quantity:\t', 'integer', f'Current {self.productList[FindProduct.productIndex(self.productList, userProduct)].name} Min. Qty.: {self.productList[FindProduct.productIndex(self.productList, userProduct)].minQuantity}'))

		# If statement checks if the product quantitly will be greater than the updated min. qty
		if not(self.productList[FindProduct.productIndex(self.productList, userProduct)].quantity <= newMQty):

			# Calls updateMinQuantity method and updates respective object's attribute
			self.productList[FindProduct.productIndex(self.productList, userProduct)].updateMinQuantity(newMQty)

			Functions.clearScreen(f'The minimum quantity for {self.productList[FindProduct.productIndex(self.productList, userProduct)].name} is now {self.productList[FindProduct.productIndex(self.productList, userProduct)].minQuantity}')

			Functions.enterToContinue()
		
		else:
			# Else occurs if new min. qty. is greater than the product quantity. No changes made.
			Functions.clearScreen(f'{f"! Modification Failed !":^75}\n\nReason: Ensure the quantity of the product is greater than the minimum quantity. Please try again later.')

			Functions.enterToContinue()
		# end if

		return
	# end modifyProductMinQty method


	def removeIndividualProduct(self):
		# Gets the product user wishes to delete and removes it
		# Parameters: self (instance)
		# Return: Null

		# Calls loopTillValid function to obtain requested product
		userProduct = Functions.loopTillValid('Enter the product name or SKU to delete:\t', 'any', 'Remove a Product')

		# If statement checks if product exists in productList
		if FindProduct.checkIfProductExists(self.productList, userProduct):

			# If statement calls confirmSelection method, asks if user confirms and prints a formatted view of the product for user visability. User doesn't confirm > No changes and kicked back to menu
			if Functions.confirmSelection(self.productList[FindProduct.productIndex(self.productList, userProduct)]):

				# Object is popped from the productList
				removed = self.productList.pop(FindProduct.productIndex(self.productList, userProduct))

				Functions.clearScreen(f'{removed.name} has been deleted.')

				Functions.enterToContinue()

		else:
			# Else occurs if product doesn't exist in productList
			FindProduct.searchError()
		# end if

		return
	# end removeIndividualProduct method


	def getCategoryToRemove(self):
		# Gets the category user wishes to delete
		# Parameters: self (instance)
		# Return: Null

		# User chooses between categories Fruit, Vegetables, Meat, Other, or return to menu
		userCtgy = Menu(f'What category would you like to empty?', 'Fruit', 'Vegetables', 'Meat', 'Other', 'Quit').menu()

		# If statement runs as long as user doesn't choose to return to menu
		if not userCtgy == '5':

			userCtgy = self.convertCategory(userCtgy)

			# Calls confirmSelection method to confirm once more before proceeding
			if Functions.confirmSelection(f'{userCtgy.title()}.\nThis will delete every product under this category.\nThere is no turning back after this.'):

				# Calls removeCategoryProducts method > all products in specified category deleted
				self.removeCategoryProducts(userCtgy)

			else:
				# Else occurs if user doesn't confirm > No changes made.
				Functions.clearScreen('No changes have been made.')

				Functions.enterToContinue()
			# end if

			return
	# end getCategoryToRemove method
	

	def removeCategoryProducts(self, ctgy):
		# Deletes every product in productList that falls in specified category
		# Parameters: self (instance), ctgy (str)
		# Returns: Null

		# Initiates an empty list that will hold every product pending deletion (Cannot delete immediately as modifying a list that is being iterated through causes indexing complexions)
		productsToDelete = []

		# For statement iterates through productList
		for product in self.productList:

			# If statement check if current iteration is in specified category
			if product.category == ctgy:

				# List appends current iteration
				productsToDelete.append(product)
			# end if
		# end for

		# For statement iterates through productsToDelete list
		for product in productsToDelete:

			# Product is popped through it's SKU
			self.productList.pop(FindProduct.productIndex(self.productList, product.sku))
		# end for

		Functions.clearScreen('Success!')

		Functions.enterToContinue()
		
		return
	# end removeCategoryProducts method
		
	
	def appendCorrectly(self, category, sku, newProduct):
		# Determines the accurate location of where the new product should be appended to (based on SKU)
		#   > For ex. SKU VEG-0043 should be between VEG-0042 and VEG-0044
		# Parameters: self (instance), category (str), sku (str), newProduct(Inventory object)
		# Returns: Null

		# Variable calls checkIfProductExists method to check if there is an sku that is one less than the newProduct SKU (effective 99% of the time)
		exists = FindProduct.checkIfProductExists(self.productList, f'{category[:3]}-{int(sku[4:]) - 1:04d}')

		if exists:
			# Calls productIndex to obtain the index of the product sku one less than newProduct
			index = FindProduct.productIndex(self.productList, f'{category[:3]}-{int(sku[4:]) - 1:04d}')

			# Appends newProduct at the index + 1
			self.productList[index + 1:index + 1] = [newProduct]

		else:
			# Else occurs if the newProduct SKU is the first one of it's category (for ex. MEA-0001)
			# This happens if user deletes the first item of the category then adds a new product in that category (newProduct takes the first available SKU of that category)
			# To rectify this situation, the program finds the next SKU above the newProduct SKU of the same category

			try:
				# Variable tracking if the next product's SKU has been found
				nextItem = False

				# For loop iterates over every product in productList
				for product in self.productList:

					# If statement checks if the current iteration is of the same category as the SKU
					if product.category == category and not nextItem:

						# The first item of the category would be the SKU that follows newProduct since we established that newProduct is the first of it's category. Obtains the index of that product
						index = FindProduct.productIndex(self.productList, product.sku)

						# Variable turns True (Stops the loop from overriding the index we need)
						nextItem = True

				# Appends newProduct at that index
				self.productList[index:index] = [newProduct]

			except UnboundLocalError:
				# Except occurs if program failed to find another product in the category (newProduct is the only one of it's category)

				# Appends newProduct at the very end of the productList
				self.productList.append(newProduct)

			# end try
		# end if
				
		return
	# end appendCorrectly method


	def makeSKU(self, category):
		# Determines the next available enumerated SKU of a specified category 
		#  > This method finds if there's a gap in the category's used SKU and will assign the SKU to that gap
		# Parameters: self (instance), category (str)
		# Returns: nextSKU (str)

		try:
			# Initiates usedSKU as an empty list
			usedSKU = []

			# For statement iterates through all products
			for product in self.productList:

				# If statement checks if current iteration is of the same category
				if product.category[:3] == category[:3]:
					
					# Appends just the integer portion of the sku
					usedSKU.append(product.sku[4:])
				# end if
			# end for
			
			# *The next available SKU is assumed to be the last usedSKU + 1
			nextSKU = int(usedSKU[-1]) + 1

			# Boolean variable preventing program from overriding if there's a gap in the usedSKUs
			gotSKU = False
			
			# For statement iterates through an enumerated usedSKU list
			for enum, SKU in enumerate(usedSKU):

				# In theory, the enumeration should always be equal to the usedSKU as they both get enumerated by 1
				# This if statement checks if the current iteration enumeration does not equal to the usedSKU
				#   > This means that the gap in the usedSKU is the next available SKU
				# If there is no gap found, the program uses the assumed nextSKU (*see above)
				if enum + 1 != int(SKU) and not gotSKU:

					# nextSKU becomes equal to the enumeration + 1 (bc enumerate starts at 0 while SKU starts at 1)
					# Boolean variable turns True to prevent overriding of SKU we need
					nextSKU, gotSKU = enum + 1, True
				

			# Formats newSKU into the proper SKU format
			newSKU = f'{category[:3]}-{nextSKU:04d}'

		except IndexError:
			# Exception occurs when there are no other SKU of that category (bc of category-wide deletion)

			# newSKU becomes the first product of that category
			newSKU = f'{category[:3]}-0001'
		# end try
		
		return newSKU
	# end makeSKU method


	def getIndividualRestockAmt(self):
		# Gets the product and the amount to order
		# Parameters: self (instance)
		# Return: Null

		# Calls loopTillValid to obtain requested product
		userSKU = Functions.loopTillValid('Enter the product name or SKU:\t', 'any', 'Search by SKU / Name')

		# If statement calls checkIfProductExists and checks if the product is in the productList
		if FindProduct.checkIfProductExists(self.productList, userSKU):

			productIndex = FindProduct.productIndex(self.productList, userSKU)

			# Calls loopTillConfirmed method to obtain amount of stock to order
			userQuantity = int(Functions.loopTillConfirmed('Enter amount of stock to order:\t', 'integer', f'{self.productList[(productIndex)]}\n'))

			# Calls reOrderSearchProduct method to update quantity
			self.reOrderSearchProduct(userQuantity, productIndex)
		
		else:
			# Else occurs if product doesn't exist in productList
			FindProduct.searchError()
		# end if

		return
	# end getIndividualRestockAmt method

	
	def reOrderSearchProduct(self, amount, index):
		# Reorders stock based on individual product (see reOrderStockMenu method)
		# Parameters: self (instance), amount (int), index (int)
		# Returns: Null

		# Calls checkReOrderAmt to determine if the amount will exceed the min. qty.
		# Method returns False if amount isn't enough
		amount = self.checkReOrderAmt(amount, index)

		# If statement runs if amount is enough to exceed min qty.
		if amount:

			# The product's quantity increments by the amount
			self.productList[index].quantity += amount
			
			Functions.clearScreen(f'{self.productList[index].name} has been restocked to {self.productList[index].quantity} quantity.')

			Functions.enterToContinue()
		# end if

		return
	# end reOrderSearchProduct method

	
	def reOrderWarningQty(self):
		# Reorders stock based on all products with an active warning indicator (see reOrderStockMenu method)
		# Parameters: self (instance)
		# Returns: Null

		# Calls loopTillConfirmed method to obtain amount of stock to order beyond the min. qty per product
		userAmount = int(Functions.loopTillConfirmed('Products with an active warning indicator will be restocked to their minimum quantity plus one.\nEnter amount of stock to order in addition per product (0 for none):\t', 'integer', 'Restock Products with Warning Indicator'))

		# Creates an Outputs object to control abundance of outputs
		outputManager = Outputs(0)

		# For loop iterates over every product in productList
		for product in self.productList:

			# If statement checks if the current iteration has an active Warning indicator
			if product.warning:

				outputManager.updateCounter()

				# Variable determines the amount of stock needed to exceed the min. qty. by one
				amtToMin = product.minQuantity - product.quantity + 1

				# Product quantity increments by amtToMin plus any additional stock if user specifies
				product.quantity += amtToMin + userAmount

				print(f'{f"{product.name} has restocked to {product.quantity}.":>40}')
			# end if
		# end for
		
		Functions.enterToContinue()
		
		return
	# end reOrderWarningQty method


	def reOrderStockUnderQty(self):
		# Reorders stock based on products with less stock than user specified (see reOrderStockMenu method)
		# Parameters: self (instance)
		# Returns: Null

		# Calls loopTillConfirmed method to obtain a maximum quantity
		userQuantity = int(Functions.loopTillConfirmed('Enter an amount of quantity:\t', 'integer', 'Restock Products under inputted Quantity'))

		# Calls loopTillConfirmed method to obtain amount of stock to order
		userAmount = int(Functions.loopTillConfirmed('Products that are under it\'s minimum quantity after the restock will remain unchanged and not be restocked.\nEnter amount of stock to order per product:\t', 'integer', f'Restock Products under {userQuantity} Quantity'))

		# Creates an Objects object to control abundance of outputs
		outputManager = Outputs(0)

		# For loop iterates over every product in productList
		for product in self.productList:

			# If statement checks if the product quantity is less than specified max stock and if product quantity + reorder amt exceeds product's min. qty.
			if product.quantity < userQuantity and product.quantity + userAmount > product.minQuantity:

				outputManager.updateCounter()

				# Product quantity increments by amount
				product.quantity += userAmount

				print(f'{f"{product.name[:20]} has restocked to {product.quantity}.":^50}')
			
			else:
				# Else occurs if the amount reordered doesn't exceed the min. qty per product
				print(f'{f"No changes have been made to {product.name[:20]}.":^50}')
			# end if
		# end for
		
		Functions.enterToContinue()
		
		return
	# end reOrderStockUnderQty method


	def checkReOrderAmt(self, amount, index):
		# Determines if the reorder quantity amount will exceed the min. qty. of a product (see reOrderSearchProduct)
		# Parameters: self (instance), amount (int), index (int)
		# Return: amount (int)
		
		
		if (self.productList[index].quantity) + amount <= (self.productList[index].minQuantity):

			Functions.clearScreen('Restock Failed.')

			print(f'Reason: You must add enough product to exceed the product\'s minimum quantity. Please try again later.')

			Functions.enterToContinue()

			# Amount equals to 0 (False) if qty amount not enough
			amount = 0
		# end if
		
		return amount
	# end checkReOrderAmt method


	def getReportProduct(self, outputManager):
		# Gets the select product the user wishes to see a report of
		# Parameters: self (instance), outputManager (object)
		# Return: Null

		# Calls loopTillConfirmed to obtain requested product
		userSKU = Functions.loopTillConfirmed('Enter the product name or SKU:\t', 'any', 'Search by SKU / Name')

		# If statement calls checkIfProductExists to check if the product exists in productList
		if FindProduct.checkIfProductExists(self.productList, userSKU):
			
			# Calls Reports method criteriaSKU
			Reports.criteriaSKU(self.productList, userSKU, outputManager)
		
		else:

			#Else occurs if requested product doesn't exist
			FindProduct.searchError()
		# end if

		return
	# end getReportProduct method


	def getReportCategory(self, outputManager):
		# Gets the select category the user wishes to see a report of
		# Parameters: self (instance), outputManager (object)
		# Return: Null

		# User chooses between Fruit, Vegetables, Meat, or Other category
		userCategory = Menu('What category do you want to sort by?', 'Fruit', 'Vegetables', 'Meat', 'Other').menu()

		userCategory = self.convertCategory(userCategory)

		# Calls Reports method criteriaCategory 
		Reports.criteriaCategory(self.productList, userCategory, outputManager)

		return
	# end getReportCategory method


	def formattedAddProduct(self, sku, name, quantity, minQty, vendPrice, markUp, salePercent):
    # Creates a formatted product string (FOR PRODUCTS NOT YET ADDED TO PRODUCT LIST) for user visability
    # Parameters: self (instance), sku (str), name (str), quantity (str), minQty (int), vendPrice (float), markUp (int), salePercent (int)
    # Returns: Formatted add product as (str)

    # Formats price and profit price to 2 decimals
		price = f'{(vendPrice * (1 + (markUp / 100)) * (1 - salePercent / 100)):.2f}'
		profit = f'{float(price) - vendPrice:.2f}'
		
		return (f"\n\n{'Product:':>15}\t{name} ({sku})\n\n{'Price:':>15}\t${(price):>5}\n{'Profit:':>15}\t${profit:>5}\n{'Quantity:':>15}\t{quantity:>5}\n{'Min Quantity:':>15}\t{minQty:>5}\n")
	# End formattedAddProduct function


	def priceHigherThanVendor(self, vendPrice, markUp, salePercent):
		# Checks if calculated current price will be lower than vendor price
		# Parameters: self (instance), vendPrice (float), markUp (int), salePercent (int)
		# Returns: True if price is higher than vendor / False if isnt (boolean)
		
		return False if vendPrice > round((vendPrice * (1 + markUp / 100)) * (1 - salePercent / 100), 2) else True
	# end priceHigherThanVendor method


	def convertCategory(self, userInput):
		# Converts the str user inputted into the corresponding category
		# Parameters: self (instance), userInput (str)
		# Return: category (str)

		if userInput == '1':
			category = 'FRUIT'
		elif userInput == '2':
			category = 'VEGETABLE'
		elif userInput == '3':
			category = 'MEAT'
		elif userInput == '4':
			category = 'OTHER'
		
		return category
	# end convertCategory
# end InventoryMenu Class
			


class Reports:

	# Contains general functions regarding generating a report (see InventoryMenu method productReportMenu)

	def printReportHeader(criteria):
		# Prints the report header
		# Parameters: criteria (str)
		# Return: Null

		Functions.clearScreen(f'Report ({criteria})')

		print(f"{'Item': <10}{'Name': <21}{'Category': <10}{'Qty': <10}{'R. Qty' : <10}{'Price': <11}{'Sale': <10}{'Profit':<10} Warning\n{'_' * 100}\n")

		return
	# end printReportHeader method

	def printItemInfo(product):
		# Prints the current product's attributes in correlation to the report header
		# Parameters: product (Inventory Object)
		# Return: Null
		regPrice, currentPrice, profit = f'{product.regPrice:.02f}', f'{product.currentPrice:.02f}', f'{product.profit:.02f}'

		print(f"{product.sku: <10}{product.name[:20]: <21}{product.category: <10}{product.quantity: <10}{product.minQuantity: <10}${regPrice: <10}${currentPrice: <10}${profit: <10} {product.warning:}")

		return
	# end printItemInfo method
	

	def criteriaSKU(productList, userSKU, outputManager):
		# Prints the individual product info
		# Parameters: productList (List), userSKU (str), outputManager (Outputs object)
		# Return: Null

		# Calls printReportHeader method
		Reports.printReportHeader(f'{userSKU.upper()}')

		# For loop iterates over all products in productList (Due to items having duplicate names in original inventory.txt)
		for product in productList:

			# If statement checks if current iteration matches the name or sku of the requested product
			if product.name.upper() == userSKU.upper() or product.sku == userSKU.upper():

				# Calls printItemInfo method
				Reports.printItemInfo(product)
			# end if

		# end for
			
		Functions.enterToContinue()

		return
	# end criteriaSKU method
		

	def criteriaCategory(productList, category, outputManager):
		# Prints all products under specified category
		# Parameters: productList (List), category (str), outputManager (Outputs object)
		# Return: Null

		# Calls printReportHeader method
		Reports.printReportHeader(category.title())

		# For loop iterates over all products in productList
		for product in productList:

			# If statement checks if current iteration matches the category of the specified.
			if product.category == category:

				outputManager.updateCounter()

				# Calls printItemInfo method
				Reports.printItemInfo(product)
			# end if
		# end for
			
		Functions.enterToContinue()

		return
	# end criteriaCategory method
	

	def criteriaQuantity(productList, outputManager):
		# Prints all products under specified quantity
		# Parameters: productList (List), outputManager (Outputs object)
		# Return: Null

		# Calls loopTillConfirmed to obtain max qty
		userQuantity = Functions.loopTillConfirmed('Enter an amount of quantity:\t', 'integer', 'Products under inputted Quantity')

		# Calls printReportHeader method
		Reports.printReportHeader(f'Products under {userQuantity} Quantity')

		# For loop iterates over all products in productList
		for product in productList:

			# If statement checks if current iteration has a lower quantity than the inputted.
			if product.quantity < int(userQuantity):

				outputManager.updateCounter()

				# Calls printItemInfo method
				Reports.printItemInfo(product)
			# end if
		# end for
			
		Functions.enterToContinue()

		return
	# end criteriaQuantity method
	

	def criteriaMinQty(productList, outputManager):
		# Prints all products with an active warning indicator
		# Parameters: productList (List), outputManager (Outputs object)
		# Return: Null

		# Calls printReportHeader method
		Reports.printReportHeader(f'Products under Minimum Quantity')

		# For loop iterates over all products in productList
		for product in productList:

			# If statement checks if current iteration has an active warning indicator
			if product.warning:

				outputManager.updateCounter()

				# Calls printItemInfo method
				Reports.printItemInfo(product)
			# end if
		# end for
			
		Functions.enterToContinue()

		return
	# end criteriaMinQty method


	def criteriaAll(productList, outputManager):
		# Prints all products
		# Parameters: productList (List), outputManager (Outputs object)
		# Return: Null

		# Calls printReportHeader method
		Reports.printReportHeader(f'All Products')

		# For loop iterates over all products in productList
		for product in productList:

			outputManager.updateCounter()
			
			# Calls printItemInfo method
			Reports.printItemInfo(product)

		# end for
		
		Functions.enterToContinue()

		return
	# end criteriaAll method
# end Reports Class
