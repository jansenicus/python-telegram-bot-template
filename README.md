# Python Telegram Bot Template

Modular customizable `python-telegram-bot` template to speed-up development process.

## Features

- ### _Easy configuration_ with a yaml file

- ### _Clear separation between Development Bot vs Production Bot_ 

- ### _Automated help text_ based on `docstring`

- ### _Simply and sophistication met in one directory to organize all command handlers_

- ### _Ready to deploy_ as a docker container



## _Easy configuration_ with a yaml file
`configuration.yaml`
```yaml
prod:
  - botname: My Production Bot
    username: my_production_bot
    token: 
      1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi
    about:
      "this is some short text about my bot"
    description:
      "This is a description of what my bot can do which customer will use"
```

## _Clear separation between Development Bot vs Production Bot_ 
`configuration.yaml`
```yaml
dev:
  - botname: Development Bot
    username: my_development_bot
    token: 
      1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi
    about:
      "this is some short text about development bot  "
    description:
      "This is a description of what my development bot can do with testing"
```
choose the mode
```yaml
mode: dev
```
or 
```yaml
mode: prod
```
## _Simplicity and sophistication met in one place_

  - `handlers` directory: as a placeholder for all command handlers  
  - `index.py` file: to register all the function members
  - 
  - sample command handlers
    - `echo.py` file: `/echo` command handler
    - `start.py` file: `/start` command handler
    - `hello.py` file: `/hello` command handler
    - `help.py` file: `/help` command handler
    - `whoami.py` file: `/whoami` command handler


## _Automated help text_ based on `docstring`
  - `help.py` will generate help text using `docstring` from all the function members
  - _*writing help as you code*_
    ```python

    def hello(update, context):
    """
    /hello
    just say hello and reply
    """
    update.message.reply_text(
        'Hi {}, how are you?'.format(update.message.from_user.first_name))

    ```
  - will produce help text
    ```
    /hello
    just say hello and reply
    ```


## _Ready to deploy_ as a docker container
Just run
```bash

docker-compose up --build

```

# Steps 
  ## 1. Preparation
  - prepare two bot accounts from [@botfather](https:///t.me/botfather)
  - one bot will be used for development 
  - another bot for production
  
  ## 2. Clone This Repository and Install Requirements 
  ```bash

    git clone https://github.com/jansenicus/python-telegram-bot-template
    cd bot
    pipenv install -r requirements.txt
    pipenv shell

  ```
  ## 3. Edit configuration file
  - edit `configuration-sample.yaml` accordingly
   ```yaml
prod:
  - botname: My Production Bot
    username: my_production_bot
    token: 
      1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi
    about:
      "this is some short text about my bot"
    description:
      "This is a description of what my bot can do which customer will use"
```
  - save the edit and rename it as `configuration.yaml`

  ## 4. Run in local machine
  Make sure you are in the `bot` directory to run
  ```bash

    python main.py

  ```

  ## 5. Build and Run as a container
  ```bash

      docker-compose up --build

  ```

