import os
import unittest

import pandas as pd
from pandas.testing import assert_series_equal

from stringshifter.patterns import  *
from stringshifter.utils import  *


def divide_S(S):
    len_S = get_len(S)
    one_three = int(len_S / 3)
    return S[0:one_three], S[one_three:]


def _shift(p, n):
    c = map_case(p)
    return convert_to_input_case(shift_string(p, n), c)


class PatternTestster(unittest.TestCase):
    def get_cases(self, contiguous=True):
        f = 'pattern_contiguous.csv'
        if not contiguous:
            f = 'pattern_non_contiguous.csv'
        return pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + "\\" + f, header=0,
                           index_col=0)

    def applyhelper(self, cases, func):
        return cases.apply(lambda x: self.applyfunc(x, func), axis=1)

    def applyfunc(self, x, func):
        first, second = divide_S(x.name)
        pattern = x['Pattern']
        shift = int(x['Shift'])
        shifted = _shift(pattern, shift)
        return func(first, second, pattern, shifted)

    def test_non_recursive_contiguous(self):
        cases = self.get_cases()
        cases['FuncOut'] = self.applyhelper(cases, pattern_replace_non_recursive)
        assert_series_equal(cases['Output'], cases['FuncOut'], check_names=False, check_index_type=False)

    def test_recursive_contiguous(self):
        cases = self.get_cases()
        cases['FuncOut'] = self.applyhelper(cases, pattern_replace_recursive)
        assert_series_equal(cases['Output'], cases['FuncOut'], check_names=False, check_index_type=False)

    def test_non_contiguous_non_recursive(self):
        cases = self.get_cases(False)
        cases['FuncOut'] = self.applyhelper(cases, non_contigious_right_replace_non_recursive)
        assert_series_equal(cases['Output'], cases['FuncOut'], check_names=False, check_index_type=False)

    def test_non_contiguous_recursive(self):
        cases = self.get_cases(False)
        cases['FuncOut'] = self.applyhelper(cases, non_contigious_right_replace_recursive)
        assert_series_equal(cases['Output'], cases['FuncOut'], check_names=False, check_index_type=False)
