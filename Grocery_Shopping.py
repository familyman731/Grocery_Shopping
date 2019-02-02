import webbrowser
import csv
import glob
import os
import time
import re
import ctypes
from pywinauto.findwindows import find_window
from pywinauto.win32functions import SetForegroundWindow

archive = "E:\\Documents\\Meal_Plans\\"


def downloadShoppingList():
	webbrowser.open("https://plantoeat.com/shopping_lists/export_csv")
	print("Waiting for download")
	# SetForegroundWindow(find_window(title='Grocery Shopping'))
	while 1:
		file_path = glob.glob(r"E:\Downloads\PTE*")
		if(file_path and not file_path[0].endswith(".crdownload")):
			break
		time.sleep(1)
	return file_path


def openShoppingList(file_path):
	with open(file_path[0]) as file:
		csvfile = csv.DictReader(file)
		for row in csvfile:
			webbrowser.open("https://grocery.walmart.com/products?query=" + row['Title'])


def archiveShoppingList(file_path,archive):
	file_name = re.search("PTE(.*)",file_path[0]).group()

	if not os.path.exists("E:\\Documents\\Meal_Plans\\" + file_name):
		archive = archive + file_name
		os.rename(file_path[0],archive)
		print("Shopping list archived here:" + archive)
	else:
		os.remove(file_path[0])
		print("List previously archived. File deleted.")


# ctypes.windll.kernel32.SetConsoleTitleW("Grocery Shopping")

file_path = downloadShoppingList()
openShoppingList(file_path)
archiveShoppingList(file_path,archive)

# SetForegroundWindow(find_window(title='Grocery Shopping'))
input("Press enter to exit...")