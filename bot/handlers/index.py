"""
index.py
---------
index all function handlers
"""


# imports here -----------------------
from .start import start
from .echo import echo
from .help import help_command
from .hello import hello
from .whoami import whoami

index_items = {
    'start': start,
    'echo' : echo,
    # ....
    # one-to-one correspondence mapping 
    # map command to function here
    # ....
    'whoami' : whoami,
    'hello' : hello,
    'help' : help_command
    }

# --------------------------------------
def index():
    """
    
    """
    return index_items