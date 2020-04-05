try:
    from cloud import cloud
    from commands import commands
except ImportError as err:
    print(f"Import failed, {err}")
    exit(1)


def loader():
    cloud()
    commands()
    pass
