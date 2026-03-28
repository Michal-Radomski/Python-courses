import sys

import pytest  # type: ignore[import-not-found]

pytestmark = pytest.mark.skipif(
    sys.platform != "win32", reason="It will run only on windows 32 OS"
)
# print(sys.platform)

const = 9 / 5


def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah


# print (cent_to_fah())


@pytest.mark.skip(reason="Skipping for no reason specified")
def test_case01():
    assert type(const) is float


# @pytest.mark.skipif(sys.version_info < (3,8), reason="Doesn't work on py version above 3.6")
# @pytest.mark.skipif(cent_to_fah()==32, reason="Default value test, so skipping")
def test_case02():
    assert cent_to_fah() == 32


@pytest.mark.skipif(pytest.__version__ < "5.4.0", reason="Pytest version is less")
def test_case03():
    assert cent_to_fah(38) == 100.4
