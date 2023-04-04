from colorama import init
from colorama import Fore, Back, Style

init()

def arg(text):
    print('{} ' + text + ' {}'.format(Fore.BLUE, Fore.YELLOW))