from colorama import init
from colorama import Fore, Back, Style

init()

def arg(text):
    print(Fore.BLUE + text)

def important(text):
    print(Fore.RED + text)