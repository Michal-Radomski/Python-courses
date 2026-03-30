import configparser
from pathlib import Path

cfgFile = "qa.ini"
cfgFileDirectory = "config"

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
# print("BASE_DIR:", BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(cfgFile)
# print("CONFIG_FILE:", CONFIG_FILE)

config.read(CONFIG_FILE)


def getGmailUrl():
    return config["gmail"]["url"]


def getGmailUser():
    return config["gmail"]["user"]


def getGmailPass():
    return config["gmail"]["pass"]


print(getGmailUrl())
