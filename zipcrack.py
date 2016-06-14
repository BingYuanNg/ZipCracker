import zipfile

def main():
	file = zipfile.ZipFile('test.zip')
	passfile = open('dictionary.txt')

	for pw in passfile.readlines():
		pw = pw.strip('\n')
		try:
			print("Trying : " + pw)
			file.extractall(pwd=pw)
			exit(0)
		except:
			pass
	print("Success")

if __name__ == '__main__':
	main()