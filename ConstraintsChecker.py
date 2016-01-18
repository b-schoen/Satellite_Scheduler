import MySQLdb

from ConsoleIO import ConsoleIO

from Database_Classes import Activity

import datetime
import time

# Has access to the database in order to check for conflicts, but no write capability

# TODO: ConstraintsChecker as modules for each table then a master ConstraintsChecker

class ConstraintsChecker:

    def __init__(self, QtMainWindow):

        #set the qtMainWindow to interact with for output/input
        self.qtMainWindow = QtMainWindow

        #create consoleIO to manager input/output with the console window
        self.console = ConsoleIO(QtMainWindow)
        #HTML color for messages displayed in console
        self.constraint_console_display_color = "Maroon"
        self.override_prompt_console_display_color = "Red"

        #create a MySQL connection to the database
        #TODO: These parameters as constructor argument (currently hardcoded for ease of testing)
        self.host = 'localhost'
        self.user = 'Bronson Schoen'
        self.user_identifier = 'bschoen'
        self.database_name = 'scheduler_database'
        self.connection = MySQLdb.connect(self.host,self.user,self.user_identifier,self.database_name)

        #create a cursor to execute commands
        self.cursor = self.connection.cursor()

    #return true if activity violates no contraints, otherwise return false
    def checkActivity(self, activity):

        #TODO: Return exception so caller is aware what went wrong

        #TODO: Make these (constraints) functions for the ConstraintsChecker_Activities module

        #assert that it starts before it stops
        if(not activity.startTime < activity.stopTime):

            constraint_message = "Constraint violation: An activity cannot end before it begins."

            self.console.display(constraint_message, self.constraint_console_display_color)

            return False

        #assert that there are no other events which start at the same time
        #(simply for testing purposes)
        elif(self.exists("Activities","startTime",activity.startTime)):

            constraint_message = "Constraint violation: Two activities cannot start at the same time"

            self.console.display(constraint_message, self.constraint_console_display_color)

            return self.prompt_override(constraint_message)

        else:

            return True

    def prompt_override(self, constraint_message):

        self.console.display("Overridable conflict: \"" + constraint_message + "\" occured", self.constraint_console_display_color)

        self.console.display("Would you like to override? (yes/no)", self.override_prompt_console_display_color)

        prompt = self.console.prompt_override(constraint_message)

        if(prompt == "yes"):

            self.console.display("Overriding \"" + constraint_message + "\"", self.override_prompt_console_display_color)

            return True

        else:

            self.console.display("Override declined", self.override_prompt_console_display_color)

            return False

    def exists(self, tableName, identifierName, identifier):

        self.open_close_everything()

        #TODO: Make work for more than floats (generalize %f formatting with identifier)

        #TODO: float comparison causes issues, can sql check for tolerance bounds? Should these be truncated before going in?
        self.checkIfExists = """SELECT EXISTS(SELECT 1 FROM %s WHERE %s=%f LIMIT 1)""" % (tableName,identifierName,identifier)

        result = self.retrieveSingleResult(self.checkIfExists)

        doesExist = result[0][0]

        return doesExist

    #return the result of a SQL query that returns a single row
    def retrieveSingleResult(self, query):

        self.cursor.execute(query)

        result = self.cursor.fetchall()

        return result

    #Print all entries in activities table (for debugging purposes)
    def printAll(self):

        sql_command = """SELECT * FROM Activities"""

        self.cursor.execute(sql_command)

        result = self.cursor.fetchall()

        #print result

    def open_close_everything(self):

        self.cursor.close()

        self.connection.close()

        self.connection = MySQLdb.connect(self.host,self.user,self.user_identifier,self.database_name)

        self.cursor = self.connection.cursor()
