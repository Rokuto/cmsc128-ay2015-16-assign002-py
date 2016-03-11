def getHammingDistance( str1, str2 ):
	# Catch input annomalies
	if len( str1 ) != len( str2 ) or len( str1 ) <= 0 or len( str2 ) <= 0:
		return  -1
	
	# count the character/s that differ from str1
	inversion = 0
	for x in xrange( 0, len( str1 ) ):
		if str1[x] != str2[x]:
			inversion += 1

	# return answer
	return inversion

def countSubstrPattern( original, pattern ):
	# Cathc input annomalies
	if len( original ) < len( pattern ) or len( original ) <= 0 or len( pattern ) <= 0:
		return 0

	# count the time a pattern occurs in the original string
	substr = 0
	for x in xrange( 0, ( len( original ) - ( len( pattern ) - 1 ) ) ):
			for y in xrange( 0, len( pattern ) ):
					# stop iteration when the two characters are not equal
					if original[x + y] != pattern[y]:
						break
					if y == ( len( pattern ) -1 ):
						substr += 1;

	# return answer
	return substr

def isValidString( str1, alphabet ):
	# Catch any error in inputs
	if len( alphabet ) <= 0 or len( str1 ) <= 0:
		return False

	# Replace all the instace of alphabet in str1
	for x in xrange( 0, len( alphabet ) ):
		if alphabet[x] not in str1:
			continue

		for y in xrange( 0, len( str1 ) ):
			if alphabet[x] == str1[y]:
				temp = list( str1 )
				temp[y] = '#'
				str1 = ''.join( temp )

	#Validate if all of the characters in str1 were replaced 
	for x in xrange( 0, len( str1 ) ):
		#When a character failed to match the replaced character
		if str1[x] != '#':
			return False

	#retrun anser
	return True

def getSkew( str1, n ):
	# Catch any errors in input
	if len( str1 ) == 0 or n == 0 or ( len( str1 ) < n ):
		return "Error"

	#Count how many g occured
	g = 0
	for x in xrange( 0, n ):
		if str1[x] == 'g' or str1[x] == 'G':
			g += 1

	#Count how many c occured
	c = 0
	for x in xrange( 0, n ):
		if str1[x] == 'c' or str1[x] == 'C':
			c += 1

	#compute skew
	return ( g - c ) 

def getMaxSkewN( str1, n ):
	# Error handling
	if len( str1 ) == 0 or n == 0 or ( len( str1 ) < n ):
		return "Error"

	skew = 5;
	g = 0
	c = 0

	# get Max skew of each charater in the str1
	for y in xrange(0, n):
		# locate g
		if str1[y] == 'g' or str1[y] == 'G':
			g += 1

		#locate c
		if str1[y] == 'c' or str1[y] == 'C':
			c += 1

		# Update
		if skew < ( g - c ):
			skew = ( g - c );

	#return answer
	return skew

def getMinSkewN( str1, n ):
	#Error handling
	if len( str1 ) == 0 or n == 0 or ( len( str1 ) < n ):
		return "Error"

	skew = 5;
	g = 0
	c = 0

	# get Max skew of each charater in the str1
	for y in xrange(0, n):
		#locate g
		if str1[y] == 'g' or str1[y] == 'G':
			g += 1

		#locate c
		if str1[y] == 'c' or str1[y] == 'C':
			c += 1

		# Update
		if skew > ( g - c ):
			skew = ( g - c );

	#return anser
	return skew