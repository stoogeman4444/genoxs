try:
    from commands.main import commands
except ImportError as err:
    print(f"Import failed, {err}")
    exit(1)
