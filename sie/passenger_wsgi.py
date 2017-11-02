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

from django_fastcgi.servers.fastcgi import runfastcgi
from django.core.servers.basehttp import get_internal_wsgi_application
wsgi_application = get_internal_wsgi_application()
runfastcgi(wsgi_application, method="prefork", daemonize="false", minspare=1, maxspare=1, maxchildren=1)
