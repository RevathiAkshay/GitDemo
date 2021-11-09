str1 = " revathi.akshay@gmail.com "
print(str1[0]) #prints the first character in the srting
print(str1[0:7])  #prints the substring in the srting

print("@" in str1) # to print if a string is there in the original string or not

# split method for stringsprint(str1.lstrip())
arr = str1.split("@")
print(arr[0])
print(arr[1])

#to remove the spaces form the  string
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())

## concatinate the 2 strins
str2 = "hello "
print(str2 + str1)

## to convert first letter into capital
print(str2.capitalize())

## to convert a word into capital
print(str2.upper())
