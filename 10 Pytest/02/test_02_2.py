import pytest  # type: ignore[import-not-found]


def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0
        # assert 3 > 3


# def func1():
#     raise ValueError("IndexError func1 raised")


# def test_case02():
#     with pytest.raises(Exception) as excinfo:
#         # assert (1,2,3) == (1,2,4)
#         func1()
#     print(str(excinfo))
#     assert (str(excinfo.value)) == "Exception func1 raised"


class TestMyStuff:
    def test_type(self):
        assert type(1.3) is float

    def test_strs(self):
        assert str.upper("python") == "PYTHON"
        assert "pytest".capitalize() == "Pytest"
