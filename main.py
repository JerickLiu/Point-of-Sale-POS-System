# POS Assignment w/ Classes
# Operates a POS system with cash register and inventory functionalities with python classes
# Jerick Liu
# 01/25/2021

from Menu import Menu
from FindProduct import FindProduct
from Inventory import InventoryMenu as Inv
from Item import Item, Shopping
from FileManager import FileManager as File
from Functions import Functions

# Constants
STORE_NAME = 'Jerick\'s Store'


class Main:

	# Holds everything required to begin the program

	def __init__(self):
		# Initializes everything, first thing executed when program starts
		# Parameters: self (instance)
		# Return: Null

		# Creates a ListUpdater object containing the master productList from info in inventory.txt
		self.allLists = ListUpdater(File.obtainProducts())

		# Boolean variable controling if user wants to exit the program
		# Calls ListUpdater method isProducts to check if there are products in the list
		self.exit = self.allLists.isProducts()

		while not self.exit:

			# User chooses to go to cash register, inventory control, or exit the program
			self.userChoice = Menu(f'Welcome to {STORE_NAME} POS System!', 'Cash Register', 'Inventory Control', 'Exit').menu()

			# User chooses to go to cash register
			if self.userChoice == '1':

				# Calls method cashRegisterMenu then calls method applyQuantityChanges after finished in cashRegisterMenu
				self.allLists.applyQuantityChanges(Shopping(self.allLists.listOfItems).cashRegisterMenu())
			
			# User chooses to go to inventory
			elif self.userChoice == '2':
				
				# Calls method inventoryMenu then calls method updateProductList after finished in inventoryMenu
				self.allLists.updateProductList(Inv(self.allLists.productList).inventoryMenu())
				
			# User chooses to exit program
			elif self.userChoice == '3':

				# Boolean evaluates to True
				self.exit = True

				# Calls method updateFiles to transfer productList to inventory.txt and make old inventories
				File.updateFiles(self.allLists.productList)

				Functions.clearScreen('Successfully saved inventory to inventory.txt')

				Main.goodbyeMessage()
			# end if
		# end while

		return
	# end __init__ method

	def goodbyeMessage():
    # Prints a goodbye message upon exiting the program
    # Parameters: self (instance)
    # Return: Null

    # Prints center justified goodbye message
		print(f'Thank you for using {STORE_NAME} POS System, goodbye!')
		
		return
	# end goodbyeMessage method
# end Main class



class ListUpdater:

	# Holds the productList with all products and it's respective attributes
	# Also holds listOfItems (productList with less attributes for cash register)

	def __init__(self, productList):
		self.productList = productList

		return
	# end __init__ method
	

	@property
	def listOfItems(self):
		# Property Decorater used as listOfItems is dependent on productList
		# Parameters: self (instance)
		# Return: listOfItems (list)

		listOfItems = []
		
		for product in self.productList:
			listOfItems.append(Item(product.sku, product.name, product.quantity, product.regPrice))
		# end for
		
		return listOfItems
	# end listOfItems method


	def updateProductList(self, productList):
		# Updates the productList after returning from Inventory
		# Parameters: self (instance), productList (list)
		# Return: Null
		self.productList = productList

		return
	# end updateProductList method
	
	def applyQuantityChanges(self, cart):
		# Updates the productList quantities after returning from cash register
		# Parameters: self (instance), cart (dict)
		# Return: Null

		for product, productQty in cart.items():
			self.productList[FindProduct.productIndex(self.productList, product)].quantity -= productQty
		# end for
		
		return 
	# end applyQuantityChanges method

	
	def isProducts(self):
		# Determines if products were extracted from inventory.txt
		# Parameters: self (instance)
		# Return: True if no products extracted / False upon successful extraction (boolean) 

		exit = False

		if not self.productList:
			Functions.clearScreen(f'{f"! Warning !":^50}\n\nReason: inventory.txt is empty. This may be intentional or the file may be missing / named incorrectly.\n\nPlease try again later.')

			Main.goodbyeMessage()

			exit = True
		# end if
		
		return exit
	# end isProducts method
# end ListUpdater class


# Main program

Main()