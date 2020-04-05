# -*- coding: utf-8 -*-

# Importing launcher
try:
    from core import launch
    from loader import loader
    loader()
except ImportError as err:
    print(f"Import failed, {err}")
    exit(1)

if __name__ == '__main__':
    launch()
    pass
