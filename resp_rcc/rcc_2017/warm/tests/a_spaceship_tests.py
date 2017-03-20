# -*- coding: utf-8 -*-
import tests_common # resp_rcc/tests_common
import pytest
from subprocess import Popen, PIPE

@pytest.mark.parametrize(('task_file', 'answer_file'),tests_common.get_filenames("./resp_rcc/rcc_2017/warm/tests/a_spaceship_tests_data_unoriginal/", 1, 2))
def test_unoriginal_simple_assume(task_file, answer_file):
    
    answer = open(answer_file, "r").readline().strip('\n')
    proc = Popen("python ./resp_rcc/rcc_2017/warm/a_spaceship/a_spaceship.py", stdout=PIPE, stdin=PIPE, stderr=PIPE)
    
    for line in open(task_file, "r"):
        proc.stdin.write(line)
    response = proc.stdout.readline()
     
    assert response == answer

