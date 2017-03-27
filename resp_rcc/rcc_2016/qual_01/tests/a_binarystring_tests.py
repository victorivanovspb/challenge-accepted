# -*- coding: utf-8 -*-
import tests_common # resp_rcc/tests_common
import pytest
from subprocess import Popen, PIPE

def count_string(msg):
    """Подсчёт входящих в строку (msg) подстрок '00', '01', '10', '11'."""
    a = 0
    b = 0
    c = 0
    d = 0
    prev = msg[0:1]
    for curr in msg[1:]:
        if prev == "0":
            if curr == "0":
                a += 1
            elif curr == "1":
                b += 1
        elif prev == "1":
            if curr == "0":
                c += 1
            elif curr == "1":
                d += 1
        prev = curr
    return (a, b, c, d)

@pytest.mark.parametrize(('task_file', 'answer_file'),tests_common.get_filenames("./resp_rcc/rcc_2016/qual_01/tests/a_binarystring_tests_data/", 1, 2))
def test_simple_assume(task_file, answer_file):
    
    proc = Popen("python ./resp_rcc/rcc_2016/qual_01/a_binarystring/a_binarystring.py", stdout=PIPE, stdin=PIPE, stderr=PIPE)
    
    answer = open(answer_file, "r")
    task = open(task_file, "r")
    n = task.readline().strip("\n")
    proc.stdin.write(n + "\n")
    
    counter = 0
    for i in xrange(int(n)):
        msg = task.readline()
        proc.stdin.write(msg)
        task_msg = proc.stdout.readline().strip('\n')
        answ_msg = answer.readline().strip('\n')
        if answ_msg == "impossible":
            counter += 1
        else:
            if count_string(task_msg) == count_string(answ_msg):
                counter += 1
            else:
                err_msg = "Troubles with tests data file + \'" + task_file + "\', test number=" + str(i) + "."
                assert err_msg == -1
    answer.close()
    task.close()
    
    assert int(counter) == int(n)