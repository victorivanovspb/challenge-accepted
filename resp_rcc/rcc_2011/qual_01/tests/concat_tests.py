# -*- coding: utf-8 -*-
import tests_common
import pytest
from subprocess import Popen, PIPE

@pytest.mark.parametrize(('f1', 'f2'),tests_common.get_filenames("./resp_rcc/rcc_2011/qual_01/tests/concat_tests_data/", 1, 15))
def test_simple_assume(f1, f2):
    
    test   = open(f1, "r").readline().strip('\n')
    answer = open(f2, "r").readline().strip('\n')
        
    proc = Popen("python ./resp_rcc/rcc_2011/qual_01/concat/concat.py", stdout=PIPE, stdin=PIPE, stderr=PIPE)
    response = proc.communicate(input=test)
    
    assert response[0] == answer
