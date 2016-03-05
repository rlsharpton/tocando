__author__ = 'tocando'
word = 'pizza'

print("Enter the beginning and ending index for your slice of 'pizza'.")
print("Press the enter key at 'Start' to exit.")
start2 = None
while start2 != "":
    start2 = (input("\nStart: "))

    if start2:
        start2 = int(start2)

        finish = int(input("Finish: "))

        print("word[", start2, ":", finish, "] is")
        print(word[start2:finish])
