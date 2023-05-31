from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from django.conf.urls import url
from hcs.views import *
from hcs.views import vote_report
from . import views


urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', homepage),
    path("register/", views.register, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path('accounts/', include('allauth.urls')),

]

app_name = 'scam_report'

urlpatterns = urlpatterns + [
    path('reports/', ScamReportListView.as_view(), name='list'),
    path('report/', ScamReportCreateView.as_view(), name='report'),
    path('create/', ScamReportCreateView.as_view(), name='create'),
    path('<int:pk>/', ScamReportDetailView.as_view(), name='detail'),
    path('vote_report/<int:pk>/', vote_report, name='vote_report'),
    path('<int:pk>/update/', ScamReportUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ScamReportDeleteView.as_view(), name='delete'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = urlpatterns + [
        # For anything not caught by a more specific rule above, hand over to
        # the list:
        path('__debug__/', include('debug_toolbar.urls')),
]
