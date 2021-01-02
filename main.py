from Menu import Menu
from FindProduct import FindProduct
from Inventory import InventoryMenu as Inv
from Item import Item, Shopping
from FileHelper import FileManager as File
from Functions import Functions

STORE_NAME = 'Jerick\'s Store'

class Main:

	# Holds everything required to begin the program

	@staticmethod
	def main():
		# Initializes everything, first thing executed when program starts
		# Parameters: None
		# Return: Null

		# Creates a ListUpdater object containing the master productList from info in inventory.txt
		allLists = ListUpdater(File.obtainProducts())

		# Boolean variable controling if user wants to exit the program
		# Calls ListUpdater method isProducts to check if there are products in the list
		exit = allLists.isProducts()

		while not exit:

			# User chooses to go to cash register, inventory control, or exit the program
			userChoice = Menu(f'Welcome to {STORE_NAME} POS System!', 'Cash Register', 'Inventory Control', 'Exit').menu()

			# User chooses to go to cash register
			if userChoice == '1':

				# Calls method cashRegisterMenu then calls method applyQuantityChanges after finished in cashRegisterMenu
				allLists.applyQuantityChanges(Shopping(allLists.listOfItems).cashRegisterMenu())
			
			# User chooses to go to inventory
			elif userChoice == '2':
				
				# Calls method inventoryMenu then calls method updateProductList after finished in inventoryMenu
				allLists.updateProductList(Inv(allLists.productList).inventoryMenu())
				
			# User chooses to exit program
			elif userChoice == '3':

				# Boolean evaluates to True
				exit = True

				# Calls method updateFiles to transfer productList to inventory.txt and make old inventories
				File.updateFiles(allLists.productList)

				Functions.clearScreen('Successfully saved inventory to inventory.txt')

				Main.goodbyeMessage()

	
	def goodbyeMessage():
    # Prints a goodbye message upon exiting the program
    # Parameters: None
    # Return: Null

    # Prints center justified goodbye message
		print(f'Thank you for using {STORE_NAME} POS System, goodbye!')
		
		return
# End goodbyeMessage function


class ListUpdater:

	# Holds the productList with all products and it's respective attributes
	# Also holds listOfItems (productList with less attributes for cash register)

	def __init__(self, productList):
		self.productList = productList

		return

	# end __init__
	

	@property
	def listOfItems(self):
		# Property Decorater used as listOfItems is dependent on productList
		# Parameters: self (instance)
		# Return: listOfItems (list)

		listOfItems = []
		
		for product in self.productList:

			listOfItems.append(Item(product.sku, product.name, product.quantity, product.regPrice))
		
		return listOfItems
	# end listOfItems


	def updateProductList(self, productList):
		# Updates the productList after returning from Inventory
		# Parameters: self (instance), productList (list)
		# Return: Null
		self.productList = productList

		return
	# end updateProductList
	
	def applyQuantityChanges(self, cart):
		# Updates the productList quantities after returning from cash register
		# Parameters: self (instance), cart (dict)
		# Return: Null

		for product, productQty in cart.items():
			self.productList[FindProduct.productIndex(self.productList, product)].quantity -= productQty
		
		return 
	# end applyQuantityChanges 

	
	def isProducts(self):
		# Determines if products were extracted from inventory.txt
		# Parameters: self (instance)
		# Return: True if no products extracted / False upon successful extraction (boolean) 

		exit = False

		if not self.productList:
			Functions.clearScreen(f'{f"! Warning !":^50}\n\nReason: inventory.txt is empty. This may be intentional or the file may be missing / named incorrectly.\n\nContinue using POS system regardless? (Y/N): ')

			continueProgram = Functions.getInput('Y', 'y', 'N', 'n')

			if continueProgram in 'Nn':
				Main.goodbyeMessage()

				exit = True
		
		return exit
	# end isProducts 
# end ListUpdater 


Main.main()