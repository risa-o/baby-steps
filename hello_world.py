print("Welcome to your ToDos!")
#----------------------
#create menu that allows user to select one of 4 choices, one of which is to quit
def menu_choice():
	print ("""1. Display All ToDos
2. Add a New ToDo
3. Delete a ToDo
Q. Quit
""")

	reply = input("> ")

	if reply == '1':
		display_todo()
	elif reply == '2':
		add_todo()
	elif reply == '3':
		delete_todo()
	elif reply == "q" or reply == 'Q':
		response = input("Are you sure? Y / N ")
		if response == 'y' or response == 'Y' or response == 'Yes' or response == "YES" or response == 'yes':
			exit()
		else:
			menu_choice()
	else:
		menu_choice()

	return ()
#----------------------
def display_todo():

	return()

def add_todo():
	return ()

def delete_todo():
	return()

def quit():
