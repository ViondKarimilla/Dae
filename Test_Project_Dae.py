import pytest
import Project_Dae


def test_cal_top15():
    top15_list = Project_Dae.cal_top15()
    assert top15_list.length == 15
    assert top15_list[0]=="The Shawshank Redemption"
    assert top15_list[-1] == "The Dark Knight Rises"
    