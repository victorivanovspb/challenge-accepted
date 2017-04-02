# -*- coding: utf-8 -*-
import tests_common # resp_rcc/tests_common
import pytest
from subprocess import Popen, PIPE

@pytest.mark.parametrize(('task_file', 'answer_file'),tests_common.get_filenames("./resp_rcc/rcc_2016/qual_01/tests/b_tunnel_tests_data/", 1, 2))
def test_simple_assume(task_file, answer_file):
    pass
    assert False