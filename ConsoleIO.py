##@file Console Input Output
# Module for handling everything to do with prompted user I/O (including override, output to console, etc.)

from PyQt4 import QtGui, QtCore

import datetime
import time

from Queue import Queue

from Override_Dialog import Ui_Override_Dialog

#TODO: Make into general IO_Manager
#TODO: Generalize redundancy in IO

#TODO: Override display to log to a text file (only append)

## Outputs log of all events (database manipulation, constraint violations, added activities, etc) and user input.
class ConsoleIO:

    def __init__(self, QtMainWindow):

        #TODO OPT: Can let this function take in Input/Output widgets and be a general QtIOManager

        self.qtMainWindow = QtMainWindow

        #setup qt text output to appropriate widget (QTextEdit)
        self.qtTextOutput = self.qtMainWindow.console_text_edit

        #setup qt text input to appropriate widget (QLineEdit)
        self.qtTextInput = self.qtMainWindow.console_line_edit

        #formatting variables -----------------------------------

        self.user_input_color = "Green"

        #background color of qtTextInput when expecting input
        self.input_expected_color = "rgb(237, 251, 255)"

    #Output ----------------------------------------------------------------------------------------------------------

    #all classes should have a display function instead of print, so can be easily changed in one place and separated

#    #this display is plaintext with no HTML markup
#    def display(self, output_string):
#
#        output_string = self.add_timestamp(output_string)
#
#        self.qtTextOutput.insertPlainText(output_string)

    def display(self, output_string, color="Black"):

        #NOTE: This could effect text storage, as resulting strings will include this added HTML

        output_string = self.add_timestamp(output_string)

        formatted_output_string = self.add_html_color(output_string,color)

        self.qtTextOutput.insertHtml(formatted_output_string)

        #scroll to bottom like a normal console
        self.scroll_to_bottom()

    def scroll_to_bottom(self):

        self.qtTextOutput.moveCursor(QtGui.QTextCursor.End)

    #Input ---------------------------------------------------------------------------------------------------------

    def prompt_input(self):

        #change the color of the qlineedit to indicate that input is expected
        self.qtTextInput.setStyleSheet("background-color: %s;" % (self.input_expected_color))

        #        #NOTE: This connect/disconnect pattern for dealing with repeated connections in classes in QT
        #       For example, without this connect/disconnect, every class with a ConsoleIO member would 
        #       call received_input when qtTextInput.returnPressed signal was emitted
        #       the solution is thus to connect when waiting for input, then disconnect when finished

        #connect function to handle received console input
        self.qtTextInput.returnPressed.connect(self.received_input)

    def received_input(self):

    	#get the input text
    	text_input = self.qtTextInput.text()

        formatted_text_input = self.add_user_input_format(text_input)

        self.display(formatted_text_input, self.user_input_color)

        #clear the line edit that was used for input
        self.qtTextInput.clear()

        #change color of qlineedit back to default to indicate that input is no longer expected
        self.qtTextInput.setStyleSheet("")

        #now disconnect this function, as we have received our desired input
        #see self.prompt_input NOTE for more details
        self.qtTextInput.returnPressed.disconnect(self.received_input)

    def test_input(self):

        self.prompt_input()

    def prompt_override(self, message):

        #create and show Override_Dialog
        override_window = Override_Dialog(message, parent=self.qtMainWindow)

        #NOTE: Exec makes it block input (to parent widget)
        #the exit code of .exec_() is persistent after execution, so it can still be accessed
        self.user_input_code=override_window.exec_()

        if(self.user_input_code == 1):

            self.user_input = "yes"

        else:

            self.user_input = "no"

        #display user input
        formatted_user_input = self.add_user_input_format(self.user_input)
        self.display(formatted_user_input, self.user_input_color)

        return self.user_input

    #Formatting -----------------------------------------------------------------------------------------------------------

    def add_timestamp(self, output_string):

        timestamp = datetime.datetime.now()

        timestamp_format = "%Y-%m-%d %H:%M:%S"

        formatted_timestamp_string = timestamp.strftime(timestamp_format)

        timestamp_string = str(formatted_timestamp_string)+": "

        formatted_output_string = timestamp_string + output_string

        return formatted_output_string

    def add_html_color(self, output_string, color):

        #set beginning and ending of html format, with the appropriate color (must be HTML color)
        #ex: Lime
        self.begin_done_HTML_format = "<font color=\"%s\">" % (color) 
        self.end_done_HTML_format = "</font><br>"

        formatted_output_string = self.begin_done_HTML_format + output_string + self.end_done_HTML_format

        return formatted_output_string

    def add_user_input_format(self, output_string):

        #format for user input
        user_input_header = "User input: "
        user_text_input_string = user_input_header+output_string

        return user_text_input_string
        

    #Use this function any time you are repeatedly checking a loop until something occures
    #otherwise python will burn through CPU checking conditional
    def wait_a_moment(self):

        #TODO: Something besides sleep because I think this blocks the main event loop (=> Qt doesn't handle asynchronously)
        #       QTimers are the solution to this

    	time.sleep(0.1)

## Requests and handles user input when a constraint violation can be overridden
class Override_Dialog(QtGui.QDialog, Ui_Override_Dialog):

    def __init__(self, message, parent=None):

        #Qt window initialization
        super(Override_Dialog, self).__init__(parent)
        self.setupUi(self)

        self.override_constraint_message_label.setText(message)

        #connect either override button to close
        self.override_yes_button.clicked.connect(self.yes_input)
        self.override_no_button.clicked.connect(self.no_input)

    #each button input returns a different exit code, which are persistent after execution
    def yes_input(self):

        self.override_done_code = 1
        self.close()

    def no_input(self):

        self.override_done_code = 0
        self.close()

    def close(self):

        self.done(self.override_done_code)
