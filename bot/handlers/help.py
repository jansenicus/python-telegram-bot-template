def help_command():
    """
    /help:
    return this help
    """
    print('HELP:')
    for k, v in index().items():
        print(v.__doc__)