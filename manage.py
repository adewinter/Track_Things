#!/usr/bin/env python
from django.core.management import execute_manager
import imp
import sys, os

# use a default settings module if none was specified on the command line
DEFAULT_SETTINGS = 'localsettings'

DEFAULT_TEST_SETTINGS = 'test_localsettings'
settings_specified = any([arg.startswith('--settings=') for arg in sys.argv])
if not settings_specified and len(sys.argv) >= 2:
    if sys.argv[1] == 'test':
        settings = DEFAULT_TEST_SETTINGS
    else:
        settings = DEFAULT_SETTINGS
    sys.argv.append('--settings=%s' % settings)
    print "NOTICE: using default settings module '%s'" % settings


import settings

if __name__ == "__main__":
    execute_manager(settings)
