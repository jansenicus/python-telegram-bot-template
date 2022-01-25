# handlers

this folder serves as the placeholder of all function handlers called with the `CommandHandler` method
```
handlers
|___ ...
|___ index.py
|___ ...
|___ start.py
|___  echo.py
```

## `index.py`
this file provides a convenient way for `main.py` in the parent folder to import all function handlers in one call
```
from handlers.index import *
```

## `start.py`
this is a sample function file which handles the `\start` command
```
    /start: 
    a start function that replies some simple word
```

