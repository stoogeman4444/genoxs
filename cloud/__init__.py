try:
    from cloud.main import cloud
except ImportError as err:
    print(f"Import failed, {err}")
