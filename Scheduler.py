import MySQLdb
#from MySQLdb.cursors import SSCursor

#import mysql.connector

from ConsoleIO import ConsoleIO
from DB_Manager import DatabaseManager
from ConstraintsChecker import ConstraintsChecker

from Database_Classes import Activity

# for testing
import sys

import datetime
import time

# TODO: Testing module
# TODO: Impliment 'finally' closing these connections

# TODO: Solve connection problem, probably with library, hopefully will go away when I use SQLAlchemy
#           Make this a static method / class, that way there's only one connection manager active per program
# NOTE: So open_close_everything works, but need a better solution (but good, it means problem actually is with connections not updating)


class Scheduler:

    # TODO: Make Activities, Events, etc. into classes

    def __init__(self, QtMainWindow):

    	#set the qtMainWindow to interact with for output/input
        self.qtMainWindow = QtMainWindow

        #create consoleIO to manager input/output with the console window
        self.console = ConsoleIO(QtMainWindow)

        self.database = DatabaseManager(self.qtMainWindow)
        self.constraints = ConstraintsChecker(self.qtMainWindow)

    def addActivity(self, activity):

        self.console.display("Attempting to add activity: " + activity.pretty_string())

        if(self.constraints.checkActivity(activity)):

            self.console.display("Activity passed all constraints")
            self.console.display("Adding activity: " + activity.pretty_string() + " to the database")

            self.database.addActivity(activity)

            return True

        else:

            self.console.display("Activity violated contraints. Please correct errors and try again")

            return False

    #def retrievePlan(self):

    	#constraint check every activity again
    	#maybe constraint check entire plan

# Return true for cleared, false for not cleared
def prompt_to_clear_activities():

    # Prompt the user if they are sure they would like to clear the activities
    # table for testing
    print "Scheduler will now clear all entries in the activities table to start testing."
    print "Are you sure you want to clear all entries from the activities table? (yes/no)"

    prompt = raw_input(">")

    if(prompt == "yes"):

        print "Do you really wish to delete all entries from the activities table? (yes/no)"

        prompt = raw_input(">")

        if(prompt == "yes"):

            print "Deleting all entries in the activities table"

            delete_activities_table_entries_SQL = """TRUNCATE TABLE Activities;"""

            host = 'localhost'
            user = 'Bronson Schoen'
            user_identifier = 'bschoen'
            database_name = 'scheduler_database'
            connection = MySQLdb.connect(host, user, user_identifier, database_name)

            cursor = connection.cursor()

            cursor.execute(delete_activities_table_entries_SQL)

            print "Successfully deleted all entries in the activities table"

            return True

    print "Aborted deleting all activities entries"
    print "The activities table is unchanged"

    return False


if __name__ == "__main__":

	#TODO: Impliment testing without QtMainWindow (can take in null?)

    scheduler = Scheduler()

    testing = True

    if(testing):

        # clearing activities table for testing
        # as an empty activities table will always behave the same way for testing
        # TODO: Make prompt a generalized funciton
        if(prompt_to_clear_activities()):

            # assuming the activity table is empty

            # these two should add without error
            new_activity = Activity(50.55, 60.45, 'dummy params')
            scheduler.addActivity(new_activity)

            new_activity = Activity(57.55, 97.44, 'more dummy params')
            scheduler.addActivity(new_activity)

            # this activity should fail, as it violates the constraint that
            # start time < end time
            new_activity = Activity(60.2, 50.1, 'even more dummy params')
            scheduler.addActivity(new_activity)

            # this activity should fail, as it starts at the same time as
            # another activity
            new_activity = Activity(50.55, 60.45, 'still more dummy params')
            scheduler.addActivity(new_activity)
