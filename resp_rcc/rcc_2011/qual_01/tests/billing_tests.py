# -*- coding: utf-8 -*-

# Working dir: challenge-accepted
import tests_common # resp_rcc/tests_common
import pytest
from subprocess import Popen, PIPE


@pytest.mark.parametrize(('task_file', 'answer_file'),tests_common.get_filenames("./resp_rcc/rcc_2011/qual_01/tests/billing_tests_data/", 1, 23))
def test_simple_assume(task_file, answer_file):
    
    answer = open(answer_file, "r").readline().strip('\n')
    proc = Popen("python ./resp_rcc/rcc_2011/qual_01/billing/billing.py", stdout=PIPE, stdin=PIPE, stderr=PIPE)
    superline = ""
    for line in open(task_file, "r"):
        superline += line
        proc.stdin.write(line)
    response = proc.stdout.readline()

    assert response == answer
