from os import system

class Functions:
	# Contains re-useable functions useful for POS System

	def getInput(*validInput):
		# Optains a user input with ONLY the passed parameters as valid inputs
		# Parameters: validInput *arg (tuple)
		# Return: userInput (str)

		# User inputs a value
		userInput = input()

		# While statement loops until userInput is in validInput
		while userInput not in validInput:

			userInput = input('Invalid input. Please try again: ')
		# End while

		return userInput
	# End getOption function

	def clearScreen(titleText=''):
		# Prints a title at the top of the screen for user visability
		# Parameters: titleText (str)
		# Returns: Null
		system('clear')

		print(f'{f"{titleText}":^50}\n')

		return
	# End title function

	def loopTillValid(text, inputType, titleText=''):
		# User input continuously loops until the input matches the indicated inputType
		# Parameters: text (str), inputType (str), titleText (str)
		# Return: userInput (str)

		Functions.clearScreen(titleText)

		# User inputs a value
		userinput = input(text)

		# If statement checks input type requested
		if inputType == 'alphabetic':

			# While statement loops till isAlphabetic function returns True   
			while not Functions.isAlphabetic(userinput) or not userinput:

				userinput = input(
					f'\nInput can only be alphabetic. No special characters or numbers.\n\n{text}')

		elif inputType == 'integer':

			# While statement loops till isInteger function returns True   
			while not Functions.isInteger(userinput) or not userinput:

				userinput = input(f'\nInput must be a positive whole number.\n\n{text}')

		elif inputType == 'float':
			
			# While statement loops till isFloat function returns True   
			while not Functions.isFloat(userinput) or not userinput:

				userinput = input(f'\nInput must be a number greater than 0.\n\n{text}')
		

		elif inputType == 'any':
			
			while not userinput:

				userinput = input(f'\n{text}')
		# End if

		return userinput
	# End loopTillValid function

	def confirmSelection(userInput, titleText=''):
		# Allows user to review the input and confirm or deny their input
		# Parameters: userInput (str), titleText (str)
		# Returns: True if user confirms / False if user denies (Boolean)

		confirmed = True

		Functions.clearScreen(titleText)

		print(f"\nYou've selected: {userInput}\n\nIs this correct (Y/N):\t", end='')

		# Calls getOption function to get user input
		userConfirmation = Functions.getInput('Y', 'y', 'N', 'n')

		# If statement checks if user denies: Boolean turns False
		if userConfirmation in 'Nn':
			confirmed = False
		# End if

		Functions.clearScreen(titleText)

		return confirmed
	# End confirmSelection function

	def loopTillConfirmed(text, inputType, titleText=''):
			# Continuously asks for user input until they confirm
			# Parameters: text (str), inputType (str), titleText (str)
			# Returns: userInput (str)

			# Boolean varible tracking if user confirmed
			confirmed = False

			Functions.clearScreen(titleText)

			# While statement loops until user confirms input
			while not confirmed:

					# Calls loopTillValid function to obtain user input
					userInput = Functions.loopTillValid(text, inputType, titleText)

					# If statement checks if the requested input is float -> formats with $ sign and 2 decimals
					if inputType == 'float':
							confirmed = Functions.confirmSelection(f'${float(userInput):.2f}', titleText)

					else:
							confirmed = Functions.confirmSelection(userInput, titleText)
					# End if

			return userInput
	# End loopTillConfirmed function

	def isAlphabetic(string):
			# Checks if a string has only alphabetic characters
			# Parameters: string (str)
			# Return: True if alphabetic / False if not (Boolean)

			valid = True

			for character in string:
					if not (character <= 'z' and character >= 'a') and not (character <= 'Z' and character >= 'A') and not character == ' ':
							valid = False
					# End if
			# End for

			return valid
	# End isAlphabetic function

	def isInteger(string):
			# Checks if string is a positive integer
			# Parameters: string (str)
			# Returns: True if string is a positive integer / False if isnt (Boolean)

			# Try statement tries to convert string into integer: Boolean turns True
			try:

					int(string)

					valid = True

			# Except occurs if string cannot be converted: Boolean turns False
			except:

					valid = False

			else:
				
				# Checks if integer is less than 0: Boolean turns False
				if int(string) < 0:

					valid = False
				# End if
			# End try

			return valid
	# End isInteger function

	def isFloat(string):
			# Checks if string can be converted to a float
			# Parameters: string (str)
			# Returns: True if can be converted / False if cannot (Boolean)

			# Try statement tries to convert string to float: Boolean turns True
			try:

					float(string)

					valid = True

			# Except occurs if string cannot be converted: Boolean turns False
			except:

					valid = False
					
			else:
				
				# Checks if integer is less than 0: Boolean turns False
				if float(string) <= 0:

					valid = False
				# End if
			# End try

			return valid
	# End isFloat function

	def enterToContinue():
		# Waits for user input before proceeding
		# Parameters: None
		# Returns: Null

		input('\nEnter anything to continue.\n')

		return
	# End enterToContinue function