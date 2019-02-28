import hashlib
import time
print("--------------------")
print("| Hash Encrypter by |")
print("|   The Piraticas   |")
print("---------------------")
def hash():
	text = input("Enter the text that you would like to encrypt: ")
	type = input("Enter the encryption type you would like to use (md5, sha1, sha224, sha256, sha384, or sha512): ")
	print(text)
	print(type)
	if type.lower() == "md5":
		encryption = hashlib.md5(text.encode('utf-8')).hexdigest()
		print(encryption)
	elif type.lower() == "sha1":
		encryption = hashlib.sha1(text.encode('utf-8')).hexdigest()
		print(encryption)
	elif type.lower() == "sha224":
		encryption = hashlib.sha224(text.encode('utf-8')).hexdigest()
		print(encryption)
	elif type.lower() == "sha256":
		encryption = hashlib.sha256(text.encode('utf-8')).hexdigest()
		print(encryption)
	elif type.lower() == "sha384":
		encryption = hashlib.sha384(text.encode('utf-8')).hexdigest()
		print(encryption)
	elif type.lower() == "sha512":
		encryption = hashlib.sha512(text.encode('utf-8')).hexdigest()
		print(encryption) 
	else:
		print("This program does not support that hash, if that even is a hash. Please try again")
		hash()
def repeat():
	again = input("Would you like to try again (Y/N)? ")
	if again.lower() == "y":
		hash()
	if again.lower() == "n":
		print("Ok. Goodbye!")
		time.sleep(2)
		exit()
	else:
		repeat()
hash()
repeat()