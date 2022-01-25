# Python Telegram Bot Template

## Concepts
Customizable `python-telegram-bot` template implementing code refactoring to streamline development process:

  - `handlers`
    - directory containing all function members of the command handlers
    - one index to call all the function members
    - one help_command that will generate help text from docstring


  - `configuration.yaml` 
    - separation of development and production mode 
    - defined in one single configuration file

## Preparation
  - prepare two bot accounts from @botfather
  - one bot for development 
  - one bot for production


## Clone this repository
```bash
git clone https://github.com/jansenicus/python-telegram-bot-template
cd bot
pipenv install -r requirements.txt
```


## Edit the configuration file
`configuration-sample.yaml` and save into `configuration.yaml`

```yaml
mode: dev
prod:
  - botname: My Production Bot
    username: my_production_bot
    token: 
      1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi
    about:
      "this is some short text about my bot"
    description:
      "This is a description of what my bot can do which customer will use"

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

## Run locally
Enter into `python-telegram-bot-template\bot` directory
```bash
python main.py
```

## Run through docker container
Enter into `python-telegram-bot-template` directory
```
docker-compose up --build
```
or
```bash
chmod +x build-docker.sh
./build-docker.sh
```