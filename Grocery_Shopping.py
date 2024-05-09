import webbrowser
import csv
import glob
import os
import time
from pathlib import Path

store_search = r"https://www.meijer.com/shopping/search.html?text="

def downloadShoppingList():
	webbrowser.open("https://plantoeat.com/shopping_lists/export_csv")
	print("Waiting for download")
	# SetForegroundWindow(find_window(title='Grocery Shopping'))
	while 1:
		downloads = str(Path.home() / "Downloads")
		file_path = glob.glob(downloads + r"\PTE*")
		if(file_path and not file_path[0].endswith(".crdownload")):
			break
		time.sleep(1)
	return file_path


def openShoppingList(file_path):
	with open(file_path[0]) as file:
		csvfile = csv.DictReader(file)
		for row in csvfile:
			webbrowser.open(store_search + row['Title'])


file_path = downloadShoppingList()
openShoppingList(file_path)
os.remove(file_path[0])