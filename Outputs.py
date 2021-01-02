class Outputs:

	# Manages outputs to screen to improve user visability

	maxOutput = 24
	linePerPrint = 1
	message = '\nEnter anything to see next.\n'

	def __init__(self, lineCounter):
		self.lineCounter = lineCounter

		return
	# end __intit__
	
	def updateCounter(self):
		# Increments lineCounter attribute by linePerPrint 
		# Parameters: self (instance)
		# Return: Null

		self.lineCounter += self.linePerPrint

		# If statement checms if lineCounter meets maxOutput
		if self.lineCounter % self.maxOutput == 0:

			input(self.message)

		return
	# end updateCounter method
# end Outputs Class