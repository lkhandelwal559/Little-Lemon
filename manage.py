#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
"""
import os
import sys

# Define the default settings module as a constant for easy modification.
DJANGO_SETTINGS_MODULE = 'littlelemon.settings'


def main():
    """Run administrative tasks."""
    # Set the default Django settings module environment variable.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)
    
    try:
        # Import Django's management utility to execute commands from the command line.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise a helpful error message if Django is not installed or the environment is misconfigured.
        raise ImportError(
            "Couldn't import Django. Make sure it is installed and available "
            "on your PYTHONPATH environment variable. You might also need to "
            "activate a virtual environment. To install Django, run:\n\n"
            "    pip install django"
        ) from exc
    
    # Execute the command-line arguments passed to this script.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Entry point of the script.
    main()
