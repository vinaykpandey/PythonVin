'''
import module name/ filename without py
import functions  as F  (same directory relative path: functions.py)
import module.functions as F (relativ path: module/functions.py)
import sys    (for absolute path)
sys.path.append('var/www/python/pymodule/')  full path = var/www/python/pymodule/functions.py
import functions  as F
'''
import sys
sys.path.append()
