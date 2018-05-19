__author__ = 'tocando'

scores = []

choice = None

while choice != '0':
    print(
    """

Hight Scores

0 - Exit
1 - Show  Scores
2 - Add a Score
3 - Delete a Score
4 - Sort Scores
"""
)

    choice = raw_input('Choice: ')
    print()

    if choice == '0':
        print('Good-bye.')

    elif choice == '1':
       print('High Scores\n')
       print('NAME\tSCORE')
       for entry in scores:
           score, name = entry
           print(name, '\t', score)

    elif choice == '2':
        name = raw_input('What is the players name: ')
        score = int(raw_input("What score did the player get: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]

    else:
        print('sorry but', choice, 'is not a valid choice.')


