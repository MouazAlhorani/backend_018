from django.urls import path, include
from .views import LoginViewSet,GetDataViewSet,DeleteViewSet,UsersViewSet,GroupsViewSet,HelpsViewSet,DailyTasksViewSet,DailyTasksReportsViewSet,RemindsViewSet,HomeView,EmailsViewSet



urlpatterns = [
    path('', HomeView.as_view({'get': 'gethome'})),
    path('api/login/', LoginViewSet.as_view({'post': 'checklogin'})),
    path('api/logout/', LoginViewSet.as_view({'post': 'logout'})),
    path('api/getalldata/', GetDataViewSet.as_view({'post': 'getalldata'})),
    path('api/getsingledata/', GetDataViewSet.as_view({'post': 'getsingledata'})),
    path('api/delete/', DeleteViewSet.as_view({'post': 'delete'})),
    path('api/deletebulk/', DeleteViewSet.as_view({'post': 'deletebulk'})),
    path('api/users/createuser/', UsersViewSet.as_view({'post': 'createuser'})),
    path('api/users/createbulkusers/', UsersViewSet.as_view({'post': 'createbulkusers'})),
    path('api/groups/creategroup/', GroupsViewSet.as_view({'post': 'creategroup'})),
    path('api/groups/createbulkgroups/', GroupsViewSet.as_view({'post': 'createbulkgroups'})),
    path('api/helps/createhelp/', HelpsViewSet.as_view({'post': 'createhelp'})),
    path('api/helps/createbulkhelps/', HelpsViewSet.as_view({'post': 'createbulkhelps'})),
    path('api/dailytasks/createdailytask/', DailyTasksViewSet.as_view({'post': 'createdailytask'})),
    path('api/dailytasks/createbulkdailytasks/', DailyTasksViewSet.as_view({'post': 'createbulkdailytasks'})),
    path('api/dailytasksreports/createdailytaskreport/', DailyTasksReportsViewSet.as_view({'post': 'createdailytaskreport'})),
    path('api/dailytasksreports/createbulkdailytasksreports/', DailyTasksReportsViewSet.as_view({'post': 'createbulkdailytasksreports'})),
    path('api/reminds/createremind/', RemindsViewSet.as_view({'post': 'createremind'})),
    path('api/reminds/remindfromtogather/', RemindsViewSet.as_view({'post': 'remindfromtogather'})),
    path('api/reminds/createbulkreminds/', RemindsViewSet.as_view({'post': 'createbulkreminds'})),
    path('api/dailytasks/createemailelement/', EmailsViewSet.as_view({'post': 'createemailelement'})),
   
    # path('checklogin/',v.checklogin),
    # path('logout/',v.logout),

    # path('getdevs/',v.getdevices),

    # path('getalldata/',v.getalldata),
    # path('getsingledata/',v.getsingledata),
    # path('delete/',v.delete),
    # path('deletebulk/',v.deletebulk),

    # path('createuser/',v.createuser),
    # path('createbulkusers/',v.createbulkusers),

    # path('creategroup/',v.creategroup),
    # path('createbulkgroups/',v.createbulkgroups),

    # path('createhelp/',v.createhelp),
    # path('createbulkhelps/',v.createbulkhelps),

    # path('createdailytask/',v.createdailytask),
    # path('createblukdailytasks/',v.createbulkdailytasks),

    # path('createreminds/',v.createremind),
    # path('createbulkreminds/',v.createbulkreminds),

    # path('createdailytaskreport/',v.createdailytaskreport),
    # path('createbulkreports/',v.createbulkdailytasksreports),
    
    # path('',v.home,name='home')
]