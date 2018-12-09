import unittest
import os


def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover(os.getcwd()+"/tests","test*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
if __name__=="__main__":
    run_tests()

