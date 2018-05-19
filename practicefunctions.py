__author__ = 'tocando'

MAX_VALUE = 9


def instructions():
    '''This is the doc statement.'''
    print('This is the instructions:')

def ask_yes_or_no(question):
    responce = None
    while responce not in ('y', 'n'):
        responce = raw_input('Enter y or no ').lower()
    return responce

def ask_number(question, low, high):
    '''Ask for a number'''
    response = None
    while response not in range(low, high):
        response = int(raw_input(question))
    return response

def main():
    instructions()
    answer = ask_yes_or_no('I need to put some junk in here...')
    print('the answer was... drumroll', answer, ' Wow.')
    print('now for a number asking function')
    value = ask_number('What is your number 0-9', 0, MAX_VALUE)
    print('Gran Finale you chose the number... ', value)

main()


