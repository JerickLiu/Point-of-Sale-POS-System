from Inventory import Inventory
from datetime import datetime
from pytz import timezone

class FileManager:
	# Allows the ability to read and write files for the POS System
	
	def obtainProducts():
		# Reads and converts info into Inventory Object from inventory.txt
		# Parameters: None
		# Return: productList (list)

		# Initiates empty productList
		productList = []
		
		# Opens inventory.txt for reading
		with open('inventory.txt', 'r') as invFile:

			for line in invFile:

					# Splits and Unpacks info from inventory.txt into variables
					# Info: self, sku, name, category, quantity, minQuantity, vendorPrice, markUpPercent, salePercent
					sku, name, category, quantity, minQuantity, vendorPrice, markUpPercent, regPrice, salePercent, currentPrice = line.replace('\n', '').split(',')

				
					# Creates an Inventory object
					inventoryEntry = Inventory(sku, name, category, quantity, minQuantity, vendorPrice, markUpPercent, salePercent)

					# Appends the Inventory object into productList
					productList.append(inventoryEntry)
			# end for

		# end with

		return productList
	# end obtainProducts method
	
	

	def txtFormat(product):
		# Converts Inventory object into proper format for txt
		# Parameters: product (Inventory object)
		# Return: formatted string (str)

		return f'{product.sku},{product.name},{product.category},{product.quantity},{product.minQuantity},{product.vendorPrice},{product.markUpPercent},{round(product.regPrice, 2)},{product.salePercent},{round(product.currentPrice, 2)}\n'
	# end txtFormat method


	def updateFiles(productList):
		# Copies current inventory.txt to a new file and writes the updated inventory to inventory.txt
		# Parameters: productList (list)
		# Return: Null

		# Opens inventory.txt for reading and writing
		with open(f'inventory.txt', 'r+') as newInv:

			# Creates file "inventory.<date>.txt" for writing
			with open(f'inventory.{datetime.now(timezone("US/Eastern")).strftime("%d-%m-%y")}.txt', 'w') as oldInv:

				# Copies everything from inventory.txt to inventory.<date>.txt
				for line in newInv:
					
					oldInv.write(line)
				# End for

				# Streams the position of inventory.txt to the beginning of the file and erase all contents
				newInv.seek(0)
				newInv.truncate()

				# Formats and tranfers productList to inventory.txt
				for product in productList:

					newInv.write(FileManager.txtFormat(product))
				# end for
			# end with
		# end with
	# end updateFiles method
# end FileManger class