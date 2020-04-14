CODING CHALLENGE SOLUTION:

- The solution has two files:
shape_coding_challenge.py
test_conf.yml : to run the with other parameters, replace test_conf.yml by any 
                other file using similar structure

- Software and browser versions tested for:
python:    3.7.1
selenium:  3.141.0
chrome:    80.0.3987.122 (Official Build) (64-bit)
safari:    13.0.5(13608.5.12)

- Python Style:
pep8

- Usage
$ python shape_coding_challenge.py -h
usage: shape_coding_challenge.py [-h] [-f CONF_FILE]

optional arguments:
  -h, --help    show this help message and exit
  -f CONF_FILE

- Sample Run
python shape_coding_challenge.py

All avatars appearing on the page
punisher
avatar5
avatar6
F
All word_length: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Longest words are 14 character long
Longest words on the page: {'exercitationem'}
.
======================================================================
FAIL: test_avatar (__main__.TestAvatar)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "shape_coding_challenge.py", line 134, in test_avatar
    "Punisher avatar is present on the page")
AssertionError: True is not false : Punisher avatar is present on the page

----------------------------------------------------------------------
Ran 2 tests in 9.528s

FAILED (failures=1)
