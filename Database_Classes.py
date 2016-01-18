#classes corresponding to the tables in DB_Manager

class Activity:

	#TODO: Can remove save functionality
	#TODO: Thing functionality

	#NOTE: Assuming a default of thing 1 for now

	#Can do elaborate time based manipulations easily with the based off start of display method
	#	Get start time from display, then time since then, etc

	def __init__(self, startTime, stopTime, parameters, thing=0):

		self.startTime = float(startTime)
		self.stopTime = float(stopTime)
		self.parameters = str(parameters)

		#optional parameter
		if(thing != 0):

			self.thing=thing

	#save the current state in the save_'name' variables
	def save_state(self):

		self.saved_startTime = self.startTime
		self.saved_stopTime = self.stopTime
		self.saved_parameters = self.parameters

	#reset all parameters to last saved parameters
	def reset_parameters_from_save(self):

		self.startTime = self.saved_startTime
		self.stopTime = self.saved_stopTime
		self.parameters = self.saved_parameters

	def get_duration(self):

		#NOTE: Must be in some kind of "seconds from X" format
		#	otherwise things like start: 11:57pm stop: next day at 11:30pm would get rejected

		self.duration = self.stopTime - self.startTime

		return self.duration

	#return a pretty printed verison of the class for display
	def pretty_string(self):

		pretty_text = "(" + str(self.startTime) + "," + str(self.stopTime) + "," + str(self.parameters) + ")"

		return pretty_text


