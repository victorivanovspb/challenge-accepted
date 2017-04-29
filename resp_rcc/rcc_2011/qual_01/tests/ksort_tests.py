# -*- coding: utf-8 -*-

# Working dir: challenge-accepted
import tests_common # resp_rcc/tests_common
import pytest
from subprocess import Popen, PIPE

@pytest.mark.parametrize(('task_file', 'answer_file'),tests_common.get_filenames("./resp_rcc/rcc_2011/qual_01/tests/ksort_tests_data/", 1, 25))
def test_ksort_assume(task_file, answer_file):
    
    answer = open(answer_file, "r").readline().strip('\n')
    proc = Popen("python ./resp_rcc/rcc_2011/qual_01/ksort/ksort.py", stdout=PIPE, stdin=PIPE, stderr=PIPE)
    superline = ""
    for line in open(task_file, "r"):
        superline += line
        proc.stdin.write(line)
    response = proc.stdout.readline()

    assert response == answer