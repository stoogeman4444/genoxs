from commands.start import cmd_start
from commands.help import cmd_help
from commands.error import cmd_error
from commands.restart import cmd_restart
from commands.stop import cmd_stop


def commands():
    cmd_start()
    cmd_restart()
    cmd_stop()
    cmd_help()
    cmd_error()
    pass
