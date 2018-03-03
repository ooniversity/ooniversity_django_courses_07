from django.conf.urls import include, url
from django.contrib import admin
from django.views import generic
from django.conf import settings
from quadratic.views import quadratic_results
from pybursa.views import IndexView
from feedbacks.views import FeedbackView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^contact/$', generic.TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
    
    url(r'^quadratic/results/', quadratic_results, name='results'),

    url(r'^polls/', include('polls.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^coaches/', include('coaches.urls'))]

admin.site.site_header = 'PyBursa Administration'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
