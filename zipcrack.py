import zipfile

def trypass(file,pw):
	try:
		print("Trying : " + pw)
		file.extractall(pwd=pw)
		return pw
	except:
		return

def main():
	file = zipfile.ZipFile('test.zip')
	passfile = open('dictionary.txt')

	for pw in passfile.readlines():
		pw = pw.strip('\n')
		match = trypass(file,pw)
		if match:
			print("Success")
		else:
			print("Failed")
	file.close()


if __name__ == '__main__':
	main()