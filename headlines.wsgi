activate_this = '/home/virtenvs/flasky/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0, "/var/www/Headlines")
from headlines import app as application
