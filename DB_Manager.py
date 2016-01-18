##Contains all classes and functions involved in manipulating the database
import MySQLdb
#from MySQLdb.cursors import SSCursor

#import mysql.connector

from ConsoleIO import ConsoleIO

import datetime
import time

## Responsible for adding and removing items from the database
class DatabaseManager:

    #TODO: Create log table that gets logged for every executeAndSave()

    def __init__(self, QtMainWindow):

        #set the qtMainWindow to interact with for output/input
        self.qtMainWindow = QtMainWindow

        #create consoleIO to manager input/output with the console window
        self.console = ConsoleIO(QtMainWindow)

        #create a MySQL connection to the database
        #TODO: These parameters as constructor argument (currently hardcoded for ease of testing)
        self.host = 'localhost'
        self.user = 'Bronson Schoen'
        self.user_identifier = 'bschoen'
        self.database_name = 'scheduler_database'
        self.connection = MySQLdb.connect(self.host,self.user,self.user_identifier,self.database_name)
        #self.connection = mysql.connector.connect(host=self.host,user="root",database=self.database_name,password="elemosmysqladmin")

        #create a cursor to execute commands
        self.cursor = self.connection.cursor()

        #TODO: Find out why return None has to be explicit classSQL runs these same two lines without giving this error
        return None

    # create the SQL commands to create data tables
    # according to specifications given in the 
    # "Mission Planning System Specification" document
    # the 'External Element' table is specified according to the 
    # "ELFIN Operations Database Table Definitions" document (in OPS/DOCS)
    #
    # To easily browse the created tables, use "sqlitebrowser" application
    #
    # NOTE: Only ever needs to be executed once per database, will throw an error otherwise
    def createTables(self):

        table_creation_commands = []

        createMissionsTable = """CREATE TABLE Missions (id BIGINT NOT NULL AUTO_INCREMENT, name VARCHAR(255),PRIMARY KEY (id));"""
        #	 TABLE Missions
        # 	 id BIGINT NOT NULL AUTO_INCREMENT
        # 	 name VARCHAR(255)
        #    PRIMARY KEY (id)

        table_creation_commands.append(createMissionsTable)

        createTimelinesTable = """CREATE TABLE Timelines (id BIGINT NOT NULL AUTO_INCREMENT, name VARCHAR(255), mission_id INTEGER, sequence INTEGER,PRIMARY KEY (id));"""
        #    TABLE Timelines
        #    id BIGINT NOT NULL AUTO_INCREMENT,
        #    name VARCHAR(255),
        #    mission_id INTEGER,
        #    sequence INTEGER
        #    PRIMARY KEY (id)

        table_creation_commands.append(createTimelinesTable)

        createActivityTypesTable = """CREATE TABLE ActivityTypes (id BIGINT NOT NULL AUTO_INCREMENT,name VARCHAR(255),mission_id INTEGER,timeline_id INTEGER,color INTEGER,symbol INTEGER,priority INTEGER,duration DOUBLE,PRIMARY KEY (id));"""
        #    CREATE TABLE ActivityTypes
        #    id BIGINT NOT NULL AUTO_INCREMENT,
        #    name VARCHAR(255),
        #    mission_id INTEGER,
        #    timeline_id INTEGER
        #    color INTEGER,
        #    symbol INTEGER,
        #    priority INTEGER,
        #    duration DOUBLE
        #    PRIMARY KEY (id)

        table_creation_commands.append(createActivityTypesTable)

        createParametersTable = """CREATE TABLE Parameters(id BIGINT NOT NULL AUTO_INCREMENT,name VARCHAR(255),type VARCHAR(255),typeID INTEGER,format VARCHAR(255),PRIMARY KEY (id));"""
        #    CREATE TABLE Parameters
        #    id BIGINT NOT NULL AUTO_INCREMENT,
        #    name VARCHAR(255),
        #    type VARCHAR(255),
        #    typeID INTEGER,
        #    format VARCHAR(255)
        #    PRIMARY KEY (id)

        table_creation_commands.append(createParametersTable)

        createActivitiesTable = """CREATE TABLE Activities (id BIGINT NOT NULL AUTO_INCREMENT,startTime DOUBLE,stopTime DOUBLE,parameter VARCHAR(255),PRIMARY KEY (id));"""
        #	 CREATE TABLE Activities
        #	 id BIGINT NOT NULL AUTO_INCREMENT,
        #    startTime DOUBLE,
        #    stopTime DOUBLE,
        #    parameter VARCHAR(255)
        #    PRIMARY KEY (id)

        table_creation_commands.append(createActivitiesTable)

        createEventTypesTable = """CREATE TABLE EventTypes (id BIGINT NOT NULL AUTO_INCREMENT,name VARCHAR(255),mission_id INTEGER,timeline_id INTEGER,color INTEGER,symbol INTEGER,PRIMARY KEY (id));"""
        #	 CREATE TABLE EventTypes
        #	 id BIGINT NOT NULL AUTO_INCREMENT,
        #    name VARCHAR(255),
        #    mission_id INTEGER,
        #    timeline_id INTEGER,
        #    color INTEGER,
        #    symbol INTEGER
        #    PRIMARY KEY (id)

        table_creation_commands.append(createEventTypesTable)

        createEventsTable = """CREATE TABLE Events (id BIGINT NOT NULL AUTO_INCREMENT, startTime DOUBLE, stopTime DOUBLE,PRIMARY KEY (id));"""
        #	 CREATE TABLE Events
        #	 id BIGINT NOT NULL AUTO_INCREMENT,
        #    startTime DOUBLE,
        #    stopTime DOUBLE
        #    PRIMARY KEY (id)

        table_creation_commands.append(createEventsTable)

        createTiggersTable = """CREATE TABLE Triggers (id BIGINT NOT NULL AUTO_INCREMENT, activityTypeID INTEGER, triggerType VARCHAR(255), triggerTypeID INTEGER, priority INTEGER, frequency INTEGER,PRIMARY KEY (id));"""
        #	 CREATE TABLE Triggers
        #	 id BIGINT NOT NULL AUTO_INCREMENT,
        #    activityTypeID INTEGER,
        #    triggerType VARCHAR(255),
        #    triggerTypeID INTEGER,
        #    priority INTEGER,
        #    frequency INTEGER
        #    PRIMARY KEY (id)

        table_creation_commands.append(createTiggersTable)

        createCommandsTable = """CREATE TABLE Commands (id BIGINT NOT NULL AUTO_INCREMENT, name VARCHAR(255), activityTypeID INTEGER, opCode VARCHAR(255),PRIMARY KEY (id));"""
        #	 CREATE TABLE Commands
        #	 id BIGINT NOT NULL AUTO_INCREMENT,
        #    name VARCHAR(255),
        #    activityTypeID INTEGER,
        #    opCode VARCHAR(255)
        #    PRIMARY KEY (id)

        table_creation_commands.append(createCommandsTable)

        createTelemetryDefinitionsTable = """CREATE TABLE TelemetryDefintions (id BIGINT NOT NULL AUTO_INCREMENT, name VARCHAR(255), mission_id INTEGER, ap_id INTEGER, offset INTEGER, length INTEGER,PRIMARY KEY (id));"""
        #	 CREATE TABLE TelemetryDefintions
        #	 id BIGINT NOT NULL AUTO_INCREMENT,
        #    name VARCHAR(255),
        #    mission_id INTEGER,
        #    ap_id INTEGER,
        #    offset INTEGER,
        #    length INTEGER
        #    PRIMARY KEY (id)

        table_creation_commands.append(createTelemetryDefinitionsTable)

        createLimitsTable = """CREATE TABLE Limits (id BIGINT NOT NULL AUTO_INCREMENT,telemetryID INTEGER,redHigh FLOAT,redLow FLOAT,yellowHigh FLOAT,yellowLow FLOAT,activityTypeID INTEGER,opCode VARCHAR(255),PRIMARY KEY (id));"""
        #	 CREATE TABLE Limits
        #	 id BIGINT NOT NULL AUTO_INCREMENT,
        #    telemetryID INTEGER,
        #    redHigh FLOAT,
        #    redLow FLOAT,
        #    yellowHigh FLOAT,
        #    yellowLow FLOAT,
        #    activityTypeID INTEGER,
        #    opCode VARCHAR(255)
        #    PRIMARY KEY (id)

        table_creation_commands.append(createLimitsTable)

        createCalibrationsTable = """CREATE TABLE Calibrations (telemetryID BIGINT NOT NULL AUTO_INCREMENT,coeff1 DOUBLE,coeff2 DOUBLE,coeff3 DOUBLE,coeff4 DOUBLE,coeff5 DOUBLE,PRIMARY KEY (telemetryID));"""
        #	 CREATE TABLE Calibrations
        #	 telemetryID BIGINT NOT NULL AUTO_INCREMENT,
        #    coeff1 DOUBLE,
        #    coeff2 DOUBLE,
        #    coeff3 DOUBLE,
        #    coeff4 DOUBLE,
        #    coeff5 DOUBLE
        #    PRIMARY KEY (telemetryID)

        table_creation_commands.append(createCalibrationsTable)

        createExternalElementsTable = """CREATE TABLE ExternalElements (id BIGINT NOT NULL AUTO_INCREMENT, missionID BIGINT, APID INTEGER, PRIMARY KEY (id));"""
        #   CREATE TABLE ExternalElements
        #   id BIGINT NOT NULL AUTO_INCREMENT,
        #   missionID BIGINT,
        #   APID INTEGER    
        #   PRIMARY KEY (id)

        table_creation_commands.append(createExternalElementsTable)

        #create all 

        for command in table_creation_commands:

            self.executeAndSave(command)


    #The approach of using a table class seems natural, but since createTables is only called once
    #in the lifetime of every database, it cannot be used to initialize or manipulate any proposed table
    #class for a particular instance
    #
    #def createTable(self, tableName,formattingString):
    #
    #	self.createTableCommand = """CREATE TABLE "%s" "%s" ;""" % (tableName, formattingString)

    def addActivity(self, activity):

        # Will I want to access this id at a later date?

        #create sql command corresponding to insert
        #unique id is automatically generated by database

        insert_command = """INSERT INTO Activities (startTime,stopTime,parameter) VALUES ("%f","%f","%s");""" % (activity.startTime,activity.stopTime,activity.parameters)

        self.executeAndSave(insert_command)

    def removeActivity(self, id):

        #cast into appropriate variable type

        id=int(id)

        #create sql command corresponding to remove

        remove_command="""DELETE FROM Activities WHERE id="%i" """ % (id)

        self.executeAndSave(remove_command)

    #return the result of a SQL query that returns a single row
    def retrieveSingleResult(self, query):

        self.cursor.execute(query)

        result = self.cursor.fetchall()

        return result

    #execute a SQL query and commit that change to the database
    def executeAndSave(self, sql_command):

        #print "Executing: "+sql_command

        self.cursor.execute(sql_command)

        self.connection.commit()

        self.printAll()

    #Print all entries in activities table (for debugging purposes)
    def printAll(self):

        sql_command = """SELECT * FROM Activities"""

        self.cursor.execute(sql_command)

        result = self.cursor.fetchall()

        #print result

#class DatabaseTable:
#
#	def __init__(self, tableName, formattingString):
#
#		self.tableName = tableName
#		self.formattingString = formattingString

if __name__ == "__main__":

    database = DatabaseManager()

    #TODO: Make a simple conditional check for if tables don't exist, create them
    #NOTE: DO NOT comment out this command unless tables need to be created on a new database
    #database.createTables()






