'''
Created on Apr 22, 2012

@author: saeed
'''


def mapNum(x, inMin, inMax, outMin, outMax):
    return (x - inMin) * (outMax - outMin) / (inMax - inMin) + outMin


##################    
# self-test code #
##################

if __name__ == '__main__':
    print (mapNum(50, 0, 100, 0, 200))