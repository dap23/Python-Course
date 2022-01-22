# Loop control statement
# break
# continue
# pass



# while True:
#     name = input("Enter Your name: ")
#     if name != "": # If variable name has not have value, then don't stop the loop
#         break # This control statement for stoping the loop

# ph_number = "098-2288-2992"
# for i in ph_number:
#     # This will check if in variable ph_number is have (-), then remove it
#     if i == "-": 
#         continue # This will return i value that have'nt (-)
#     print(i, end="") # And print it into console


# This will print 1-20 except 10
for i in range(1,21):
    if i == 10:
        pass
    else:
        print(i)