import os

dirName = "syns"

def findIndexForSynonym(synonym):
	try:
		with open(dirName + os.path.sep + synonym + ".txt", "r") as f:
			words = f.readlines()
			words = [word.strip() for word in words]
	except:
		return -1
	index = 0
	for word in words:
		if word == synonym:
			return index
		index += 1
	raise BaseException("Synonym missing")

def storeSynonymList(synonyms):
	content = "\n".join(synonyms)
	for synonym in synonyms:
		with open(dirName + os.path.sep + synonym + ".txt", "w+") as f:
			f.write(content)

if __name__ == "__main__":
	storeSynonymList(["cool", "good", "awesome"])
	print(findIndexForSynonym("good"))
	print(findIndexForSynonym("awesome"))
	print(findIndexForSynonym("cool"))
	print(findIndexForSynonym("bad"))

