
import libZ

choice = 0

while choice != 7:
	print "[1] Get Hamming Distance"
	print "[2] Count Sub Str Pattern"
	print "[3] Is Valid String Str"
	print "[4] Get Skew"
	print "[5] Get Max Skew N"
	print "[6] Get Min Skew N"
	print "[7] Exit"
	choice = int( input("Enter Choice: ") );

	if choice == 7:
		break
	elif choice == 1:
		x = getHammingDistance( str( raw_input("Enter str1: ") ) , str( raw_input("Enter str2: ") ) )
		if x == -1:
			print "Error! Strings are not equal!"
		else:
			print x
	elif choice == 2:
		print countSubstrPattern( str( raw_input("Enter original str: ") ), str( raw_input("Enter pattern str: ") ) )
	elif choice == 3:
		print isValidString( str( raw_input("Enter str1: ") ), str( raw_input("Enter alphabet: ") ) )
	elif choice == 4: 
		print getSkew( str( raw_input("Enter str1: ") ), int( input("Enter int n: ") ) ) 
	elif choice == 5:
		print getMaxSkewN( str( raw_input("Enter str1: ") ), int( input("Enter int n: ") ) ) 
	elif choice == 6:
		print getMinSkewN( str( raw_input("Enter str1: ") ), int( input("Enter int n: ") ) ) 
		
	else :
		print "Invalid Input"

