import unittest
 
def isprime(value):
    divisor=value-1
    while divisor > 1:
        if value % divisor == 0:
            return False
        divisor = divisor-1
    return True
    
    
class TestIsPrime(unittest.TestCase):
    def test_whit_1(self):
        result = isprime(1)
        self.assertTrue(result)
    
    def test_whit_2(self):
        result = isprime(2)
        self.assertTrue(result)
        
    def test_whit_3(self):
        result = isprime(3)
        self.assertTrue(result)
    
    def test_whit_4(self):
        result = isprime(4)
        self.assertFalse(result)

unittest.main()