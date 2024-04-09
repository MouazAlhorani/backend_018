from django.db import models,migrations


class GROUPS(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    groupname=models.CharField(unique=True,max_length=255)
    notification=models.BooleanField(default=True)
    chat_id=models.EmailField(blank=True,max_length=100)
    api_token=models.CharField(blank=True,max_length=255)
    users=models.TextField(default='')

class USERS(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    fullname=models.CharField(unique=True,max_length=128)
    username=models.CharField(unique=True,max_length=128)
    email=models.EmailField(null=True,blank=True,default=None)
    phone=models.CharField(max_length=128)
    password=models.CharField(max_length=128)
    admin=models.CharField(default='user',max_length=15)
    enable=models.BooleanField(default=True)
    groups=models.TextField(default='')
    loginstatus=models.BooleanField(default=False)
    lastlogin=models.DateTimeField(null=True,blank=True)
    ip=models.GenericIPAddressField(null=True,blank=True)
    
class APPVAL(models.Model):
    valstatus=models.TextField()
    errmsg=models.TextField()

class USERSLOG(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    log=models.TextField()
    logdate=models.DateTimeField()
    user_log=models.ForeignKey(USERS,on_delete=models.SET_NULL,null=True)

class Help(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    helpname=models.CharField(unique=True,max_length=255)
    helpdesc=models.TextField(default=None)

class DailyTasks(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    task=models.TextField(unique=True)
    taskhelp=models.ForeignKey(Help,on_delete=models.SET_NULL,null=True,default=None)
    
class DailyTasksReport(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    report=models.TextField(default='')
    reportdate=models.DateTimeField(null=True,blank=True)
    lastupdate=models.DateTimeField(null=True,blank=True)
    createby=models.CharField(default=None,max_length=100)
    createby_id=models.ForeignKey(USERS,on_delete=models.SET_NULL,null=True)

class UsersReportsShow(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    user_id=models.ForeignKey(USERS,on_delete=models.SET_NULL,null=True)
    report_id=models.ForeignKey(DailyTasksReport,on_delete=models.SET_NULL,null=True)   
   
class Reminder(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    remindname=models.CharField(unique=True,max_length=100)
    url=models.CharField(max_length=150)
    reminddesc=models.CharField(max_length=150)
    remindtype=models.CharField(max_length=10)
    expiredate=models.DateTimeField(null=True,blank=True)
    remindbefor=models.IntegerField(default=10)
    groups=models.CharField(max_length=100,default=None,null=True)
    remainingdays=models.CharField(max_length=100,null=True)
    lastupdate=models.DateTimeField(null=True,blank=True)
    remindlog=models.TextField()
    notification=models.BooleanField(default=True)
    prev_alertstatus=models.BooleanField(default=False)
    alertstatus=models.BooleanField(default=False)
    createby_id=models.ForeignKey(USERS,on_delete=models.SET_NULL,null=True)
       
class EmailsCheck(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    emailname=models.CharField(unique=True,max_length=100)
    error_des=models.CharField(max_length=250)
    days=models.CharField(max_length=250)
    time_hours=models.CharField(max_length=100)
    case=models.CharField(max_length=100)
    arrival_time=models.DateTimeField(null=True,blank=True)
    execpted_arrival_time=models.DateTimeField(null=True,blank=True)
    groups=models.CharField(max_length=100,default=None,null=True)
    

class GROUPSUSERS(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    user=models.ForeignKey(USERS,on_delete=models.CASCADE,null=True)
    group=models.ForeignKey(GROUPS,on_delete=models.CASCADE,null=True)

class GROUPSREMIDES(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    group=models.ForeignKey(GROUPS,on_delete=models.CASCADE,null=True)
    remind=models.ForeignKey(Reminder,on_delete=models.CASCADE,null=True)

class GROUPSEMAILS(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    group=models.ForeignKey(GROUPS,on_delete=models.CASCADE,null=True)
    email=models.ForeignKey(EmailsCheck,on_delete=models.CASCADE,null=True)