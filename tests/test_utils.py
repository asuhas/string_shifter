import unittest
from stringshifter.utils import *
import string
import pandas as pd
import os
from itertools import chain,combinations

class PreconditionsTest(unittest.TestCase):
    def powerset(self,iterable):
        '''
        Taken from itertools official docs : https://docs.python.org/2/library/itertools.html#recipes
        :return:
        '''
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    def generate_shift_out(self,x):
        val = x.index.values
        n = x.name[0]
        x=  [ convert_to_input_case(shift_string(n,int(o)),map_case(n)) for o in val]
       # x= shift_string(n,1)
        return x
    def test_check_num(self):
        x= range(-10000,10000)
        [check_num(y) for y in x]
        self.assert_(True)

    def test_check_num_raises(self):
        z= range(-10000,10000)
        [self.assertRaises(ValueError,lambda : check_num(float(j))) for j in z]
        [self.assertRaises(ValueError,lambda :  check_num(str(j))) for j in z]
        self.assertRaises(ValueError,lambda : check_num(z))

    def test_all_valid_alphabets(self):
        cases = list(string.ascii_letters)
        for case in cases:
            check_string_validity("".join(case))

    def test_all_invalid_strings(self):
        cases = list(string.punctuation+string.whitespace+string.digits)
        for case in cases:
            self.assertRaises(ValueError, lambda :check_string_validity("".join(case)))

    def test_shift(self):
        cases=pd.read_csv(os.path.dirname(os.path.realpath(__file__))+"\\"+'shift_test_cases.csv', header=0,index_col=0)
        cases.apply(lambda x: self.assertEqual(list(x.values),self.generate_shift_out(x)),axis=1)

    def test_power_set(self):
        x = list(range(1,10))
        k = list(self.powerset(x))
        for i in x:
            s= generate_power_set(x,i)
            o = [list(g) for g in k if len(g)==i]
            if [c for c in s if c not in o]:
                self.fail("Powerset is different")
