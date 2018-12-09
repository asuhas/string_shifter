import os
import unittest

import pandas as pd
from pandas.testing import assert_series_equal

from driver import StringShifter


class PatternTester(unittest.TestCase):
    def get_cases(self, contiguous=True):
        f = 'pattern_contiguous.csv'
        if not contiguous:
            f = 'pattern_non_contiguous.csv'
        return pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + "\\" + f, header=0,
                           index_col=0)

    def applyfunc(self, x, contiguous):
        first = x.name
        pattern = x['Pattern']
        shift = int(x['Shift'])
        tester = StringShifter(first, pattern, shift)
        tester.verbose = False
        if contiguous:
            tester.run_non_recursive_contiguous()
            x = tester.S_replaced
            tester.run_recursive_contiguous()
            y = tester.S_replaced
        else:
            tester.run_non_recursive_non_contiguous()
            x = tester.S_replaced
            tester.run_recursive_non_contiguous()
            y = tester.S_replaced
        return pd.Series([x, y])

    def test_driver_contiguous(self):
        cases = self.get_cases()
        cases[['NR', 'R']] = cases.apply(lambda x: self.applyfunc(x, True), axis=1)
        assert_series_equal(cases['Output'], cases['R'], check_names=False, check_index_type=False)
        assert_series_equal(cases['Output'], cases['NR'], check_names=False, check_index_type=False)

    def test_driver_non_contiguous(self):
        cases = self.get_cases(False)
        cases[['NR', 'R']] = cases.apply(lambda x: self.applyfunc(x, False), axis=1)
        assert_series_equal(cases['Output'], cases['R'], check_names=False, check_index_type=False)
        assert_series_equal(cases['Output'], cases['NR'], check_names=False, check_index_type=False)
