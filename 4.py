# Slicing string to create substring by extracting elements from another string
# syntax that you can use is indexing[] or slice()

# name = "John Hammond"
#       0123 4 567891011
# Value of variable name is an array and you can slice it by calling a number of array that you want to use (array is started by 0)

# first_name = name[0] # This will print J,
# first_name = name[0:4] # This will print John because the last number you input is will not printed and the first number of array you can started from any number you want

# last_name = name[5:12]

# print(first_name)
# print(last_name)

# Slice

url = "http://youtube.com"
url2 = "http://google.com"
sliceUrl = slice(7, -4) # This should remove "http://" and ".com" and leave it just youtube in variable sliceUrl

print(url[sliceUrl])
print(url2[sliceUrl])