from selenium import webdriver
from conectar import *

from getpass import getpass

login = input("Login: ")
password = getpass('Password: ')
driver = Conectar.Conexao(webdriver.Chrome(), login, password)