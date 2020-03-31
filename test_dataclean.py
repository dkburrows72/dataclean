import pytest

import dataclean.dataclean as dc

def test_dataclean_with_comma_sep():
    bad_data = ["4: matthew,burrows,158 Harmon dr, box 1292, 8603833549\n",]

    assert dc.find_bad_data("testdata.csv") == bad_data

def test_check_line():
    good_data = "matthew,burrows,'158 Harmon dr, box 1292', 8603833549\n"

    assert dc.check_line(good_data,"'") == 4
