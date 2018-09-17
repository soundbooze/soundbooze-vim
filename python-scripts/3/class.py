class GetTest(object):
    def __init__(self, name):
        print('Greetings!! {0}'.format(name))
    def another_method(self):
        print('I am another method which is not' ' automatically called')

a = GetTest('yasoob')
b = GetTest()
