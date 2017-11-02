#!/home/ftp_sie/.virtualenvs/diu/bin/python
# -*- coding: utf-8 -*-
import sys, os
cwd = os.getcwd()
sys.path.append(cwd)

INTERP = "/home/ftp_sie/.virtualenvs/diu/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, "/home/ftp_sie/sie.seedprojects.org/TesisDiunys/sie")
sys.path.insert(0, "/home/ftp_sie/.virtualenvs/diu/bin")
sys.path.insert(0, "/home/ftp_sie/.virtualenvs/diu/lib/python2.7/site-packages/django")
sys.path.insert(0, "/home/ftp_sie/.virtualenvs/diu/lib/python2.7/site-packages")
os.environ['DJANGO_SETTINGS_MODULE'] = 'sie.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
