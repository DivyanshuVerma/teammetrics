from django.http import HttpResponse
from django.shortcuts import render_to_response
from metrics.models import *
import subprocess
import os

def home(request):
    team_names = get_team_list()
    return render_to_response('metrics/template_nonjs.html', {'flag1':'true', 'teams':team_names})

def add(request):
    return render_to_response('metrics/template_add.html')
    
def addteam(request,team_name,fields):
    team_names = get_team_list()
    if team_name in team_names:
        return render_to_response('metrics/template_nonjs.html', {'flag1':None, 'data':'Team '+team_name+' already exists', 'teams':team_names})
    att = fields.split('&')
    gtfields = '"' + '","'.join(att) + '"'
    gtfields = "'" + gtfields + "'"
    gtlist = '[self.year,self.' + ',self.'.join(att) + ']'
    att.insert(0,'year')
    props = '\n\nclass ' + team_name + '(models.Model):\n    class Meta:\n        verbose_name_plural = "'+team_name+'"\n    '
    for i in range(len(att)):
        props += att[i] + ' = models.IntegerField()\n    '
    props += '\n    def __unicode__(self):\n        return str(self.year)\n\n    def getlist(self):\n        return '+ gtlist + '\n\n    def getfields(self):\n        return '+ gtfields
    f = open( os.getcwd() + '/metrics/models.py','a')
    f.write(props)
    f.close()
    f = open( os.getcwd() + '/metrics/team_names','a')
    f.write( '\n' +team_name + '\n')
    f.close()
    cmd = ['python ' + os.getcwd() + '/manage.py syncdb']
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).wait()
    #return HttpResponse(os.getcwd() + ' Successfully added' + props.replace('\\n','<br/>').replace(' ','&nbsp;'))
    team_names = get_team_list()    
    return render_to_response('metrics/template_nonjs.html', {'flag1':None, 'data':'The team <b>' + team_name + '</b> was added successfully.', 'teams':team_names})

def team(request, team_name,ye1=0,ye2=0):
    team_names = get_team_list()
    flag = 'false'
    if team_name not in team_names:
        return render_to_response('metrics/template_nonjs.html', {'flag1':None, 'data':'The selected team: <b>'+team_name.capitalize()+ '</b> was not found.', 'teams':team_names})
    if ye1==0 and ye2==0:
        a = eval(team_name).objects.all()
        if len(a) < 1:
            return render_to_response('metrics/template_nonjs.html', {'flag1':None, 'data':'Team <b>'+team_name+'</b> exists, but there is no data available.', 'teams':team_names})
        fields = a[0].getfields()
        f = open(os.getcwd() + '/static/demo.data','w')
        years = ''
        for i in range(1,len(a[0].getlist())):
            f.write('0' + '\t')
        f.write('\n')
        for i in a:
            tmp_list = i.getlist()
            for k in range(len(tmp_list)):
                if(k==0):
                    years += '"' + str(tmp_list[k]) + '",'
                f.write(str(tmp_list[k])+'\t')
            f.write('\n')
        f.close()
        years = years[:-1]
        makeScript(team_name,years,fields)
        cmd = ['Rscript ' + os.getcwd() + '/static/myscript.r']
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).wait()
        data = 'Graph for team: <b>'+team_name.capitalize()+'</b> <br/><img src="res.png" alt="Graph" width="1000px" height="600px"></img>'
        return render_to_response('metrics/template_nonjs.html', {'flag1':None, 'data':data, 'teams':team_names})
    elif ye2==0:
        tm = correction( eval(team_name), ye1,ye2)
        ye1,ye2 = tm[0],tm[1]
        a = eval(team_name).objects.filter(year=ye1)
        if len(a) < 1:
            return render_to_response('metrics/template_nonjs.html', {'flag1':None, 'data':'Team <b>'+team_name+'</b> exists, but there is no data available.', 'teams':team_names})        
        fields = a[0].getfields()
        f = open(os.getcwd() + '/static/demo.data','w')
        years = ''
        for i in range(1,len(a[0].getlist())):
            f.write('0' + '\t')
        f.write('\n')
        for i in a:
            tmp_list = i.getlist()
            for k in range(len(tmp_list)):
                if(k==0):
                    years += '"' + str(tmp_list[k]) + '",'
                f.write(str(tmp_list[k])+'\t')
            f.write('\n')
        f.close()
        years = years[:-1]
        makeScript(team_name,years,fields)
        cmd = ['Rscript ' + os.getcwd() + '/static/myscript.r']
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).wait()
        data = 'Graph for team: <b>'+team_name.capitalize()+'</b> <br/><img src="res.png" alt="Graph" width="1000px" height="600px"></img>'
        if tm[2]:
            return render_to_response('metrics/template_nonjs.html', {'flag1':None, 'data':data, 'teams':team_names, 'error':'<b>Error:</b> The statistical data is not available for the selected year. So, the selected year is ' + str(ye1)})
        else:
            return render_to_response('metrics/template_nonjs.html', {'flag1':None, 'data':data, 'teams':team_names})
    else:
        a = []
        tm = correction( eval(team_name), ye1,ye2)
        ye1,ye2 = tm[0],tm[1]
        ye1_copy = ye1
        while ye1<=ye2:
            a += eval(team_name).objects.filter(year=ye1)
            ye1 = str(int(ye1) + 1) 
        if len(a) < 1:
            return render_to_response('metrics/template_nonjs.html', {'flag1':None, 'data':'Team <b>'+team_name+'</b> exists, but there is no data available.', 'teams':team_names})
        fields = a[0].getfields()
        f = open(os.getcwd() + '/static/demo.data','w')
        years = ''
        for i in range(1,len(a[0].getlist())):
            f.write('0' + '\t')
        f.write('\n')
        for i in a:
            tmp_list = i.getlist()
            for k in range(len(tmp_list)):
                if(k==0):
                    years += '"' + str(tmp_list[k]) + '",'
                f.write(str(tmp_list[k])+'\t')
            f.write('\n')
        f.close()
        years = years[:-1]
        makeScript(team_name,years,fields)
        cmd = ['Rscript ' + os.getcwd() + '/static/myscript.r']
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).wait()
        data = 'Graph for team: <b>'+team_name.capitalize()+'</b> <br/><img src="res.png" alt="Graph" width="1000px" height="600px"></img>'
        if tm[2]:
            return render_to_response('metrics/template_nonjs.html', {'flag1':None, 'data':data, 'teams':team_names, 'error':'<b>Error:</b> The statistical data is not available for the selected year duration. So, the selected duration is ' + str(ye1_copy) + '-' + str(ye2)})
        else:
            return render_to_response('metrics/template_nonjs.html', {'flag1':None, 'data':data, 'teams':team_names})

def image(request,add):
    f = open(os.getcwd() + '/static/'+add,'r')
    s = ''
    for i in f:
        s = s + i
    f.close()
    return HttpResponse(s)

def makeScript(team_name,years,fields):
    f = open(os.getcwd() + '/static/myscript.r','w')
    f.write("\n\
data <- read.table(file='" + os.getcwd() + "/static/demo.data', sep = '\t', fill=TRUE, header=TRUE )\n\
\n\
mycolors=c('red', 'blue', 'darkorange', 'darkgreen', 'darkorchid', \n\
           'brown', 'cornflowerblue', 'brown2', 'chartreuse3', 'aquamarine4')\n\
\n\
plotcolors <- mycolors[1:6]\n\
\n\
png('" + os.getcwd() + "/static/res.png', width = 1366, height = 768)\n\
\n\
barplot(t(data),\n\
    beside=TRUE,col=plotcolors,main='Graph for " + team_name.capitalize() + "', \n\
    legend.text=c(" + fields + "), \n\
    ylab='Statistics', \n\
    xlab='Year',names.arg=c(" + years + "))\n\
\n\
dev.off()")

def correction(ins, ye1, ye2):
    a = ins.objects.filter()
    l = []
    for i in a:
        l += [str(i)]
    pas = False
    if ye1 not in l:
        ye1 = l[0]
        pas = True
    if int(ye2) is not 0:
        if ye2 not in l:
            ye2 = l[-1]
            pas = True
    return [str(ye1),str(ye2),pas]

def get_team_list():
    fl = open(os.getcwd() + '/metrics/team_names','r')
    t = ()
    for i in fl:
        if i == '\n' or i == '':
            continue
        t += (i[:-1],)
    fl.close()
    return t
    
