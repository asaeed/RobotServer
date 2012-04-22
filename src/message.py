'''
Created on Apr 22, 2012

@author: saeed
'''

class Message:
    '''
    This serves as a dictionary and parser/constructor of JSON
    '''

    def __init__(self):
        pass
        
    def __str__(self):
        s = "{"
        firstTime = True
        for key in self.__dict__:
            if firstTime:
                firstTime = False
            else:
                s += ','
            value = self.__dict__[key]
            s += '"' + key + '":'
            if type(value) == str: 
                s += '"' + value + '"'
            if type(value) == float or type(value) == int:
                s += str(value)
        s += "}"
        return s
        
    def parse(self, input):
        if self.isValid(input):
            dictionary = eval(input)
            for key in dictionary.keys():
                self.__dict__[key] = dictionary[key]
            
    def isValid(self, input):
        returnValue = False
        if input[0] == 123 and input[-1] == 125: #check for '{' and '}'
            returnValue = True
        return returnValue
    
    
##################    
# self-test code #
##################

if __name__ == '__main__':
    m = Message()
    m.neck = 100
    m.leftMotor = 8
    m.rightMotor = 4 
    print(m)
    
    n = Message()
    n.parse(b"{'ip':'192.168.1.10','heading':75}")
    print(n)
    