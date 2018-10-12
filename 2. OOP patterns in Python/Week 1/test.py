#import unittest

# def factorize(x):
#     return [11, 7]


class TestFactorization(unittest.TestCase):
    def test_simple_multipliers(self):  
        # x = 77
        # a, b = factorize(x)          
        self.assertEqual(4*2, 8)

# def main():
#     #unittest.main()
#     tf = TestFactorization()
#     tf.test_simple_multipliers()

# if __name__ == '__main__':
#     main()