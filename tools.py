from os import listdir
from os.path import isfile, join, isdir
import os.path
import enchant
import os
import shutil
from nltk.stem.lancaster import LancasterStemmer

def listFiles(path):
	return [ f for f in listdir(path) if isfile(join(path,f)) and not f.startswith('.')]
	
def listFolders(path):
	return [ f for f in listdir(path) if isdir(join(path,f)) and not f.startswith('.')]
	
def removeDocs(doc_names, path):
	for doc in doc_names:
		if isfile(join(path, doc)):
			os.remove(join(path, doc))

def checkWord(word):
	d = enchant.Dict("en_US")
	st = LancasterStemmer()
	return d.check(word) or d.check(word.capitalize()) or d.check(st.stem(word))

def keepEnglishWords(path, output):
	word_dict = []
	filenames = listFiles(path)
	for name in filenames:
		print '=====processing: ' + name + '======='
		filepath = join(path, name)
		p = open(filepath, 'r')
		content = p.read()
		p.close()
		words = content.strip().split(' ')
		res = []
		for word in words:
			if word in word_dict:
				res.append(word)
			else:
				if checkWord(word):
					word_dict.append(word)
					res.append(word)
				else:
					print word + ', false'
		res = ' '.join(res)
		p = open(join(output, name), 'w')
		p.write(res)
		p.close()
		
def mergeMultiFoldersToOne(folders_path, dest_folder_path, addFolderName):
	folders = listFolders(folders_path)
	for folder in folders:
		folder_path = join(folders_path, folder)
		files = listFiles(folder_path)
		if addFolderName is True:
			for file in files:
				file_path = join(folder_path, file)
				file_path2 = join(folder_path, folder + '_' + file)
				os.rename(file_path, file_path2)
				shutil.copy(file_path2, dest_folder_path)
		else:
			for file in files:
				file_path = join(folder_path, file)
				shutil.copy(file_path, dest_folder_path)

def removeLen2Words(path, output):
	filenames = listFiles(path)
	for name in filenames:
		print '=====processing: ' + name + '======='
		filepath = join(path, name)
		p = open(filepath, 'r')
		content = p.read()
		p.close()
		words = content.strip().split(' ')
		res = []
		for word in words:
			if len(word) > 2:
				res.append(word)
			else:
				print word + ', false'
		res = ' '.join(res)
		p = open(join(output, name), 'w')
		p.write(res)
		p.close()

def removeFoldersWithSmallNoDocs(path, num):
	folders = listFolders(path)
	for folder in folders:
		if len(listFiles(join(path, folder))) < num:
			shutil.rmtree(join(path, folder))
			
def removeFilesWithSmallSize(folder_path, size):
	files = listFiles(folder_path)
	for file in files:
		if os.path.getsize(join(folder_path, file)) < size:
			os.remove(join(folder_path, file))