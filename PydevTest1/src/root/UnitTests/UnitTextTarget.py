'''
Created on Feb 17, 2013

@author: gagamama
'''
import cProfile

class UnitTextTarget(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def Add(self, a, b):
        return a + b
    
    def Subtract(self, a, b):
        return a-b
    
    def Multiply(self,a, b):
        return a*b
    
    def Multiply_straight(self, a, b):
        result = 0
        while a > 0:
            result = result+b
            a = a - 1
        return result
    
    def Multiply_branch(self, a, b):
        result = 0
        if a < b:
            limit = a
            val = b
        else:
            limit = b
            val = a
            
        while limit > 0:
            result = result + val
            limit = limit - 1
        return result
    
    def Profile(self):
        cProfile.run('UnitTextTarget().Multiply_straight(1000000,2)')
        cProfile.run('UnitTextTarget().Multiply_branch(1000000,2)')
        cProfile.run('UnitTextTarget().Multiply_straight(2,1000000)')
        cProfile.run('UnitTextTarget().Multiply_branch(2,1000000)')
        cProfile.run('UnitTextTarget().Multiply_straight(1000000,1000000)')
        cProfile.run('UnitTextTarget().Multiply_branch(1000000,1000000)')
        cProfile.run('(1000000 * 1000000)')
        
if __name__ == '__main__':
    UnitTextTarget().Profile()