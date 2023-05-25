#!/usr/bin/env python
###################################################
# Fast API Scraper bot by x4leqxinn<3.
###################################################
import os

def main():
    os.environ.setdefault('BOT_SETTINGS_MODULE', 'settings.development')
    from core import start 
    start()


if __name__ == '__main__':
    main()