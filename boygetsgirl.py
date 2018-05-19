__author__ = 'tocando'

class Boy(object):
    ''' The boy class
    '''

    def get(self, who):
        print('we know what he wants')
        who.accept()

class Girl(object):
    ''' Wants to be "got"
    '''

    def accept(self):
        print("finally my one true love!")

#main
print('Boy meets girl.')

joe = Boy()
jill = Girl()
joe.get(jill)
