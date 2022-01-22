# Looping
# While, for

# While loop (unlimited)

# while 1==1:         # This same as true condition which mean looping never end
#     print("Hello")

# name = ""
# while len(name) == 0:   # This looping end if user input their name
#     name = input("Enter your name: ")

# print("Hello " + name)

# Or you can make it more readable for human

# name = None

# while not name:
#     name = input("Enter your name: ")

# print("Hi "+name)

# for loop (limited)

# This same as for (int i=0; i<10; i++) and printed value i which is 1 - 9
# for i in range(10): 
#     print(i+10)


# This loop will start in 50 and ended in 99 same as for(int i = 50; i<100; i++)
for i in range(50,100):
    print(i)