# Python Strings Examples

# capitalize
s = "this is string example....wow!!!"
print("s.capitalize() : ", s.capitalize())
# Output: s.capitalize() :  This is string example....wow!!!

# count
s = "this is string example....wow!!!"
sub = "i"
print ("s.count(sub, 4, 40) : ", s.count(sub, 4, 40))
sub = "wow"
print ("s.count(sub) : ", s.count(sub))
# Output
# s.count(sub, 4, 40) :  2
# s.count(sub) :  1

# endswith
s = "this is string example....wow!!!"
suffix = "wow!!!"
print (s.endswith(suffix))
print (s.endswith(suffix,20))
suffix = "is"
print (s.endswith(suffix, 2, 4))
print (s.endswith(suffix, 2, 6))
# Output
# True
# True
# True
# False

# find
str1 = "this is string example....wow!!!"
str2 = "exam"
print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))
# Output
# 15
# 15
# -1

# isalnum
s= "this2009"  # No space in this string
print (s.isalnum())
s= "this is string example....wow!!!"
print (s.isalnum())
# Output
# True
# False

# isalpha
s= "this"  # No space & digit in this string
print (s.isalpha())
s= "this is string example....wow!!!"
print (s.isalpha())
# Output
# True
# False

# isdigit
s= "123456"  # Only digit in this string
print (s.isdigit())
s= "this is string example....wow!!!"
print (s.isdigit())
# Output
# True
# False

# islower
s= "THIS is string example....wow!!!" 
print (s.islower())
s= "this is string example....wow!!!"
print (s.islower())
# Output
# False
# True

# isalnum
s= "this2009"  
print (s.isnumeric())
s= "23443434"
print (s.isnumeric())
#Output
#False
#True

#isupper
s= "THIS IS STRING EXAMPLE....WOW!!!" 
print (s.isupper())
s= "THIS is string example....wow!!!"
print (s.isupper())
#Output
#True
#False

#len
s= "this is string example....wow!!!"
print ("Length of the string: ", len(s))
#Output
#Length of the string:  32

#islower
s= "THIS IS STRING EXAMPLE....WOW!!!"
print (s.lower())
#Output
#this is string example....wow!!!

#strip
s= "0000000this is string example....wow!!!0000000"
print (s.strip('0'))
#Output
#this is string example....wow!!!

#replace
s= "this is string example....wow!!! this is really string"
print (s.replace("is", "was"))
print (s.replace("is", "was", 3))
#Output
#thwas was string example....wow!!! thwas was really string
#thwas was string example....wow!!! thwas is really string

#join
s = "-"
seq = ("a", "b", "c") # This is sequence of strings.
print (s.join( seq ))
#Output
#a-b-c

#split
s= "Line1-abcdef \nLine2-abc \nLine4-abcd"
print (s.split( ))
print (s.split(' ', 1 ))
#Output
#['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
#['Line1-abcdef', '\nLine2-abc \nLine4-abcd']