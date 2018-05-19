__author__ = 'tocando'

# Geek Translator
# Demonstrates using dictionaries

geek = {"404": "clueless.  From the web error message 404, meaning page not found.",
        "Googling": "searching the Internet for background information on a person.",
        "Keyboard Plaque" : "the collection of debris found in computer keyboards.",
        "Link Rot" : "the process by which web page links become obsolete.",
        "Percussive Maintenance" : "the act of striking an electronic device to make it work.",
        "Uninstalled" : "being fired.  Especially popular during the dot-bomb era."}

choice = None
while choice != "0":

    print(
    """
    Geek Translator

    0 - Quit
    1 - Look Up a Geek Term
    2 - Add a Geek Term
    3 - Redefine a Geek Term
    4 - Delete a Geek Term
    """
    )

    choice = raw_input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    elif choice == '1':
        term = raw_input('What term do you want me to translate?: ')
        if term in geek:
            definition = geek[term]
            print("\n", term, "means", definition)
        else:
            print("\nSorry, I don't know", term)

    elif choice == '2':
        term = raw_input("What term would you like to add?")
        if term not in geek:
            definition = raw_input('\nWhat is the new definition?')
            geek[term] = definition
            print("\nterm has been added.")
        else:
            print('That term already exists!')

    elif choice == '3':
        term = raw_input('What term do you want to redefine?')
        if term in geek:
            definition = raw_input('what is the definition?')
            geek[term] = definition
            print('Added')
        else:
            print('That term does not exist try adding it.')

    elif choice == '4':
        term = raw_input('What term do you want to delete?')
        if term in geek:
            del geek[term]
            print('Ok deleted.')
        else:
            print('term does not exist.')

    else:
        print('Sorry but', choice, 'is invalid.')



