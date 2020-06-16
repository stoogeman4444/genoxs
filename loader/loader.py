from cloud import cloud
from commands import commands
from services import services


def loader():
    cloud()
    services()
    commands()
    pass
