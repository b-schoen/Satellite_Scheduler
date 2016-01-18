#Compiles all necessary files and starts QT Application

#Compile all ui files into their python counterparts
pyuic4 ELFIN_Proto.ui > ELFIN_Proto.py

pyuic4 Help_Dialog.ui > Help_Dialog.py

pyuic4 Add_Activity_Dialog.ui > Add_Activity_Dialog.py

pyuic4 Override_Dialog.ui > Override_Dialog.py

#run the main python file, starting QT application
ipython runELFIN_Proto.py