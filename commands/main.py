try:
    from commands.start import cmd_start
    from commands.help import cmd_help
    from commands.error import cmd_error
except ImportError as err:
    print(f"Import failed, {err}")
    exit(1)


def commands():
    cmd_start()
    cmd_help()
    cmd_error()
    pass
