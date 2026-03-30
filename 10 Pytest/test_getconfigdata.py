from utils.ConfigFileParser import ConfigFileParser
from utils.myconfigparser import *  # noqa: F403

config = ConfigFileParser("prod.ini")


def test_getgmailurl():
    print(getGmailUrl())  # noqa: F405


def test_getoutlookurl():
    print(config.getOutlookUrl())
