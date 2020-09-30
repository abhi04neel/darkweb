#!/usr/bin/env python/This is beuatiful website
import os, sys,py

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "darkweb.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

