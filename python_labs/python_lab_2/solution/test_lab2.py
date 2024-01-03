from byu_pytest_utils import run_python_script, max_score, this_folder
import json

@max_score(3)
def test1():
    run_python_script("lab2.py", "--string","Its corn, with a big lump with knobs. It has juice. I cant imagine a more beautiful thing. Its corn, I can tell you all about it. I mean, look at this thing. When I tried it with butter everything changed.")
    with open(this_folder/"word-counts.json") as word, open("test_files/test1.json") as test:
        dict1 = json.load(word)
        dict2 = json.load(test)
    assert dict1 == dict2

@max_score(3)
def test2():
    run_python_script("lab2.py", "--string","Peter Piper picked a peck of pickled peppers. Did Peter Piper pick a peck of pickled peppers. If Peter Piper picked a peck of pickled peppers, wheres the peck of pickled peppers Peter Piper picked.")
    with open("word-counts.json") as word, open("test_files/test2.json") as test:
        dict1 = json.load(word)
        dict2 = json.load(test)
    assert dict1 == dict2
@max_score(4)
def test3():
    run_python_script("lab2.py", "--string","My milkshake brings all the boys to the yard And theyre like, its better than yours, dang right its better than yours I can teach you, but I have to charge. My milkshake brings all the boys to the yard. And theyre like, its better than yours, dang right its better than yours I can teach you, but I have to charge.")
    with open("word-counts.json") as word, open("test_files/test3.json") as test:
        dict1 = json.load(word)
        dict2 = json.load(test)
    assert dict1 == dict2
