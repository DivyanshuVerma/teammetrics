from metrics.models import *
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import *
import os

def get_team_list():
    fl = open(os.getcwd() + '/metrics/team_names','r')
    t = ()
    for i in fl:
        if i == '\n' or i == '':
            continue
        t += (i[:-1],)
    fl.close()
    return t

for i in get_team_list():
    admin.site.register(eval(i))
    
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)    
