from Functions import Functions

class Menu:

	# Creates a menu and obtains an input in correlation

	def __init__(self, titleText, *option):
		self.titleText = titleText
		self.option = option

		return
	
	# End __init__ method

	
	def menu(self):
		# Prints a menu
		# Parameters: self (instance)
		# Return: userInput (str)

		Functions.clearScreen(self.titleText)

		# For loop cycles through tuple
		for num, choice in enumerate(self.option):

			# Prints each element in the tuple enumerated by one
			print(f'{num + 1}: {choice}')
		# End for

		print('\nPlease select an option:', end=' ')

		userInput = self.getOption()

		return userInput
	# End menuOptions function
	
	def getOption(self):
		# Optains a user input in relation to the menu options
		# Parameters:  self (instance)
		# Return: userInput (str)

		# User inputs a value
		userInput = input()

		# While statement loops until userInput is in validInput
		while userInput not in [str(i + 1) for i in range(len(self.option))]:

			userInput = input('Invalid input. Please try again: ')
		# End while

		return userInput
	# End getOption function
# End Menu class