__author__ = 'tocando'

print('Opening and closing files')
text_file = open('sowpods.txt', 'r')
print(text_file.readline(10))

text_file.close()

