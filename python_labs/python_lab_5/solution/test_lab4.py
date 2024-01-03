from byu_pytest_utils import run_python_script, max_score, this_folder, dialog, test_files
import subprocess


@max_score(3)
@dialog(test_files / 'answer1.txt', 'lab4.py', '--array', '1 2 3 4 5')
def test_1():
    ...
@max_score(3)
@dialog(test_files / 'answer2.txt', 'lab3.py', '--array', '1 2 3 4 5 6 7 8 9 10 9 8 7 6 5 4 3 2 1')
def test_2():
    ...
@max_score(4)
@dialog(test_files / 'answer3.txt', 'lab3.py', '--array', '1 2 3 4 5 6 7 8 9 10')
def test_3():
    ...
