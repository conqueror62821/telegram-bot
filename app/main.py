#!/usr/bin/env python
###################################################
# Fast API Scraper bot by x4leqxinn<3.
###################################################
import os

def main():
    os.environ.setdefault('BOT_SETTINGS_MODULE', 'settings.development')
    from core import run_server
    run_server()


if __name__ == '__main__':
    main()