from Menu import Menu
from Functions import Functions
from FindProduct import FindProduct

TAXRATE = 0.13

class Item:
	# Holds information representing an item in the store

	def __init__(self, sku, name, quantity, price):
		self.sku = sku
		self.name = name
		self.quantity = quantity 
		self.price = price

		return
	# end __init__ method
	
	def __str__(self):
		# Prints a formatted view of an Item object. Shows name, sku, price, and quantity.

		price = f'{self.price:.2f}'

		return (f"\n\n{f'Product {self.sku}:':>20}\t{self.name}\n\n{'Price:':>20}\t${price:>5}\n{'Quantity:':>20}\t{self.quantity}")
	# end __str__ method
# end Item class

 
class Shopping(Item):
	# Holds methods allowing user to shop products

	def __init__(self, listOfItems):
		self.listOfItems = listOfItems
		self.cart = {}

		return
	# end __init__ method

	def cashRegisterMenu(self):
		# Central Cash Register
		# Parameters: self (instance)
		# Return: checkedOut (dict)
		
		# Boolean variable tracking if user wants to keep shopping and cart (dictionary) tracking what user has added to cart
		doneShopping, checkedOut = False, {}

		while not doneShopping:

			# User chooses between add to cart, checkout, and back to menu
			userChoice = Menu('Cash Register', 'Add to Cart', 'Checkout','Back to Main Menu').menu()

			# User chooses add to cart
			if userChoice == '1':

				# Calls getUserProduct method to obtain requested product
				SKU = self.getUserProduct()

				# Calls shop method to get requested stock 
				self.shop(SKU)

			# User chooses checkout
			elif userChoice == '2':
				
				# Creates Transaction object and calls takePayment method
				Transaction(self.listOfItems, self.cart).takePayment()
				
				# Variable equates to cart when transaction is completed to confirm quantity has been taken
				checkedOut = self.cart

				# Boolean controling while loop turns True
				doneShopping = True
			
			# User chooses back to menu
			elif userChoice == '3':

				doneShopping = Functions.confirmSelection('\n\nBack to Main Menu (You will lose your cart if you proceed)\n', 'Cash Register')
			# end if

		return checkedOut
	# end cashRegisterMenu method
	

	def getUserProduct(self):
		# Obtains the user requested product to purchase
		# Parameters: self (instance)
		# Return: SKU (str)

		# Calls loopTillValid method to obtain user inputted SKU
		SKU = Functions.loopTillValid('\nEnter the SKU or Name of the item:\t', 'any', 'Adding to Cart')

		# Variable tracking if user confirmed is False
		confirmed = False

		# While statement loops until user confirms product
		while not confirmed:
			
			# If statement calls checkIfProductExists method to check if user input is in productList
			if FindProduct.checkIfProductExists(self.listOfItems, SKU): 

				# User reviews requested product and can confirm or deny
				confirmed = Functions.confirmSelection(self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)], 'Adding to Cart')

				if not confirmed:
					# User inputs another SKU is denied

					SKU = Functions.loopTillValid('\nEnter the SKU or Name of the item:\t', 'any', 'Adding to Cart')
				# end if

			else:
				# Else occurs if user input is not a product in productList
				FindProduct.searchError()

				SKU = Functions.loopTillValid('\nEnter the SKU or Name of the item:\t', 'any', 'Adding to Cart')
			# end if
			
		# Variable equates to the SKU of the item requested
		SKU = self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].sku
		
		return SKU
	# end getUserProduct method

	
	def stockAvailable(self, stockPurchase, SKU):
	# Determines if there is enough stock relative to user inputted stock purchase
	# Parameters: self (instance), stockPurchase (int), SKU (str)
	# Returns: True if stock is available / False if isnt (Boolean)

		available = True

		# If statement checks if user already has product stock in cart
		if SKU in self.cart:

			# If statement checks if stock in cart + stock requested > product stock
			if self.cart[SKU] + stockPurchase > self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].quantity:

				# Boolean turns false
				available = False
			# End if

		else:
			
			# If statement checks if stock requested > product stock
			if stockPurchase > self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].quantity:

				# Boolean turns false
				available = False
			# End if
		# End if

		return available
	# End stockAvailable function

	def shop(self, SKU):
		# Allows user to add input requested quantity
		# Parameters: self (self), SKU (str)
		# Return: Null

		# Boolean variable tracking if user confirmed the amount of stock they want to buy
		stockConfirm = False

		# While statement loops until user confirms 
		while not stockConfirm:

				# Calls loopTillValid function to obtain user inputted stock
				stockPurchase = int(Functions.loopTillValid(f'How many {self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].name} do you want to add to cart:\t', 'integer', f'{"Cash Register":^50}\n{self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)]}'))

				# If statement calls stockAvailable function to check if the stock is available
				if self.stockAvailable(stockPurchase, SKU):
					
						# Boolean variable exits while loop if user confirms the stock
						stockConfirm = Functions.confirmSelection(stockPurchase, 'Cash Register')

				else:
						# Else calls errorStockMessage
						self.errorStockMessage(SKU)

						Functions.enterToContinue()
				# End if
		# End while
		
		# Calls addToCart function to add the stock to the cart
		self.addToCart(SKU, stockPurchase)

		# Calls cartReview for user visability
		self.cartReview(stockPurchase, SKU)

		return
	# End shopping method


	def addToCart(self, SKU, stockPurchase):
		# Adds the product and the stock to the cart
		# Parameters: self (instance), SKU (str), stockPurchase(int)
		# Returns: Null

		# Try statement tries to increment the stock in cart if it already exists, else it creates an entry
		try:

				self.cart[SKU] += stockPurchase

		except:

				if stockPurchase != 0:

						self.cart[SKU] = stockPurchase
		# End try

		return 
	# End addToCart method


	def errorStockMessage(self, SKU):
			# Prints an error message if the stock user entered exceeds the stock available
			# Parameters: self (instance), SKU (int)
			# Return: Null

			# Try statement tries to print how much stock of the item is already in cart
			try:
					print(f'\nUh oh, there isn\'t enough stock for that! You already have {self.cart[SKU]} in your cart!')

			except KeyError:
					print('\nUh oh, there isn\'t enough stock for that!')
			
			return
	# End errorStockMessage method


	def cartReview(self, stockPurchase, SKU):
			# Prints the formatted cart and successful stock purchase message
			# Parameters: self (instance), stockPurchase (int), SKU (str)
			# Return: Null

			Functions.clearScreen('YOUR CART\n')

			# For statement goes through productCodes list
			for SKU, productQty in self.cart.items():

					# Prints formatted product for viewer visability
					print(f'\t{productQty:>3} x {self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].name:<10}')
			# End for

			# Prints successful stock purchase message
			print(f'\n\n{stockPurchase} {self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].name} have been added to your cart.')

			Functions.enterToContinue()

			return
	# End cartReview method
# end Shopping class


class Transaction(Shopping):
	# Holds a list of item objects and methods to complete purchase

	def __init__(self, listOfItems, cart):
		
		super().__init__(listOfItems)
		self.cart = cart

		return
	# end __init__ method


	def computeSubtotal(self):
		# Computes subtotal of cart by multiplying price of object by quantity
		# Parameters: self (instance)
		# Return: subtotal (float)
		subtotal = 0

		for SKU, productQty in self.cart.items():
		
			subtotal += self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].price * productQty
		
		return subtotal
	# end computeSubtotal method
	

	def computeTax(self, subtotal):
		# Computes tax on subtotal
		# Parameters: subtotal (float)
		# Return: tax on purchase (float)

		return float(subtotal) * TAXRATE
	# end computeTax method

	
	def computeTotal(self, subtotal, tax):
		# Computes Total by adding subtotal and tax
		# Parameters: subtotal (float), tax (float)
		# Return: total on purchase (float)

		return float(subtotal) + float(tax)
	# end computeTotal method
		
	
	def takePayment(self):
		# Continuously takes payment method from user until all of total is paid
		# Parameters: self (instance)
		# Return: Null

		# Calls computeTax method to determine tax
		tax = self.computeTax(self.computeSubtotal())

		# Calls computeTotal method to determine total
		total = round(self.computeTotal(self.computeSubtotal(), tax), 2)

		# Initializes paid to track total amount user paid
		paid = 0

		# Initializes listOfPayments to track all methods of payment
		listOfPayments = []

		# While statement continuously loops until paid exceeds or is equal to total
		while total > paid:

			# User picks from cash, debit, or credit and subsequently enters amount to pay with specified method
			paymentType = Payment(Menu('Method of Payment:', 'Cash', 'Debit', 'Credit').menu(), Functions.loopTillConfirmed(f'Enter the amount to pay with chosen payment method:\t', 'float', f'{f"Paid / Total":^50}\n{f"${paid:.2f} / ${total:.2f}":^50}'))

			# If statement checks if user didn't overpay bill with credit
			if not (paymentType.paymentType == 'Credit Card' and paymentType.amount + paid > total): 
				
				# Method and amound gets appended into listOfPayments
				listOfPayments.append([paymentType.paymentType, paymentType.amount])

				# paid variable increments by amount
				paid += paymentType.amount
			
			else:
				# Else occurs if user overpaid bill with credit (illegal)
				#   > Payment not recorded and user prompted to re-enter payment 

				Functions.clearScreen(f'{f"! Payment Failed !":^75}\n\nReason: You cannot overpay the bill with a credit card. Please try again.')

				Functions.enterToContinue()
			# end if
		# end while

		# Calls needsChange method
		self.needsChange(listOfPayments, paid, total)

		return
	# end takePayment method

	def needsChange(self, listOfPayments, paid, total):
		# Determines if the Transaction features change and prints Receipt accordingly
		# Parameters: self (instance), listOfPayments (list), paid (float), total (float)
		# Return: Null

		# If statement checks if change is required for the transaction
		if paid > total:
			
			# Change calculated by subtracting total from paid, formatted to 2 decimals
			change = f'{paid - total:.2f}'

			# Calls and prints getReceiptString method (with change)
			print(Receipt.getReceiptString(self, listOfPayments, change))

			Functions.enterToContinue()
		
		else:

			# Calls and prints getReceiptString method (without change)
			print(Receipt.getReceiptString(self, listOfPayments))

			Functions.enterToContinue()
		# end if

		return
	# end needsChange method
#end Transaction class

				
class PaymentType:

	# Holds types of payment

	def __init__(self, paymentType):
		if paymentType == '1':
			self.paymentType = 'Cash'
		elif paymentType == '2':
			self.paymentType = 'Debit Card'
		elif paymentType == '3':
			self.paymentType = 'Credit Card'
		
		return
	# end __init__ method
# end PaymentType Class


class Payment:

	# Holds payment type and amount

	def __init__(self, paymentType, amount):
		self.paymentType = PaymentType(paymentType).paymentType
		self.amount = float(amount)

		return
	# end __init__ method
# end Payment Class


class Receipt(Transaction, Shopping):

	STORE_NAME = 'Store Name'
	CASHIER = 'Name'

	def getReceiptString(self, listOfPayments, change = None):
    # Obtains a string containing an itemized reciept of all items in cart
    # Parameters: self (instance), listOfPayments (list), change (float)
    # Returns: Null

		Functions.clearScreen()

		line = '–' * 60

		# Output initiated as top of receipt
		output = (f'{Receipt.STORE_NAME:^65}\n{f"Cashier: {Receipt.CASHIER}":^65}\n{"ITEMIZED RECIEPT":^65}\n\n\t{"QTY":>2}\t\t{"PRODUCT"}\t\t\t\t\t\t\t\t\t{"PRICE"}\n\t{line}\n')
	
		# For statement iterates through unpacked user cart
		# Each iteration represents a unique product in cart
		for SKU, productQty in self.cart.items():

			# Price of product determined by multiplying product price by quantity
			price = f'{self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].price * productQty:.2f}'

			# Receipt price spacing determined by multiplying a space by 36 subtracted by the length of the price string and product name string
			spacing = ' ' * (36 - len(f'{self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].price:.2f}') - len(str(self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].name[:20])))

			# Output concatenates a formatted product
			output += f'\n\n\t{productQty:>3}\t\t{self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].name[:20]} (${self.listOfItems[FindProduct.productIndex(self.listOfItems, SKU)].price:.2f}){spacing}${price:>8}\n\t\t\t   SKU: {SKU}'
		# end for
		
		# Formats subtotal, tax, grandtotal to 2 decimals
		subtotal = f'{self.computeSubtotal():.2f}'
		tax = f'{self.computeTax(float(subtotal)):.2f}'
		grandTotal = f'{self.computeTotal(float(subtotal), float(tax)):.2f}'

		# Output concatenates subtotal, HST, grand total portion of reciept
		output += (f'\n\t{line}\n\n\tSubtotal:{Receipt.totalsReceiptSpacing(49, "Subtotal: ")}${subtotal:>8}\n\n\tHST 13%:{Receipt.totalsReceiptSpacing(49, "HST 13%: ")}${tax:>8}\n\t{line}\n\n\tGrand Total:{Receipt.totalsReceiptSpacing(49, "Grand Total: ")}${grandTotal:>8}\n\t{line}\n{"PAYMENT":^65}')
		
		# For statement iterates through listOfPayments
		# Each iteration represents a method of payment
		for payment in listOfPayments:
			# Money formatted to 2 decimals
			money = f'{payment[1]:.2f}'
			# Output concatenates formatted payment method
			output += f'\n\n\t{payment[0]}: {Receipt.totalsReceiptSpacing(45, str(payment[0]))}(${money:>8})'
		#end for 
		
		# If statement checks if change is present
		if change:
			# Output concatenates formatted change
			output += f'\n\n\tChange:{Receipt.totalsReceiptSpacing(49, "Change: ")}${change:>8}'

		# Output concatenates footer of receipt
		output += f'\n\n{f"Thank you for shopping at {Receipt.STORE_NAME}!":^70}\n\n'

		return output
	# End getReceiptString method
	
	def totalsReceiptSpacing(spacing, text):
		# Determines receipt spacing
		# Parameters: spacing (int), text (str)
		# Return: proper spacing (str)

		return ' ' * (spacing - len(text))
	# end totalsReceiptSpacing method
# end Reciept class