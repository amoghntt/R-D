from django.conf.urls import url
from . import views
#from perlscripts import views as s
#from javacode import views as j
#from scriptsOptimization import views as so
#from errorlogs import views as e
#from usecase1 import views as usecase1
#from AdaptivePlanning import views as a

urlpatterns=[
    url(r'^$', views.index, name='index1'),
    
    url(r'^about$', views.about, name='about'),
    url(r'^aspire$', views.aspire, name='aspire'),
    #url(r'^perlscripts/$', s.index, name='index'),
    #url(r'^javacode/$', j.index, name='index'),
    #url(r'^scriptsOptimization/$', so.index, name='index'),
    #url(r'^errorlogs/$', e.index, name='index'),
    #url(r'^perlscripts/result/$', s.perl, name='perl'),
    url(r'^result/$', views.result, name='result'),
    url(r'^index/$', views.indices, name='index')
    #url(r'^errorlogs/result/$', e.error_logs, name='Error_logs'),
    #url(r'^usecase1/$', usecase1.metrics, name='usecase1'),
    #url(r'^AdaptivePlanning/$', a.adp, name='AdaptivePlanning'),'''
    ]




