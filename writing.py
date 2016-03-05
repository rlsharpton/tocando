__author__ = 'tocando'

f = open('scores.txt', 'w')

while True:
    participant = raw_input('Your name >')

    if participant == 'q':
        print("quitting")
        break

    score = raw_input('Score for ' + participant + '> ')
    f.write(participant + ',' + score + '\n')

f.close()

