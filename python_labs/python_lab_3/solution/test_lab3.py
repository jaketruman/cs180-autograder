from byu_pytest_utils import run_python_script, max_score, this_folder, dialog, test_files
import subprocess


@max_score(3)
@dialog(test_files / '4.txt', 'lab3.py', '--n', '4')
def test_4():
    ...
@max_score(3)
@dialog(test_files / '4.txt', 'lab3.py', '--n', '4')
def test_5():
    ...
@max_score(3)
@dialog(test_files / '25.txt', 'lab3.py', '--n', '25')
def test_25():
    ...
