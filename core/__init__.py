try:
    from core.bot import launch, bot
except ImportError as err:
    print(f"Import failed, {err}")
    exit(1)