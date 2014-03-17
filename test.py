__author__ = 'Rizzy'

import os

selection = os.listdir('D:/')
for each in selection:
    if 'maya' in each.lower():
        print each
