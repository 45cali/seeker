from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from seeker.rest import apiviews

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'users',  apiviews.UserViewSet)
router.register(r'groups', apiviews.GroupViewSet)
router.register(r'alerts', apiviews.AlertViewSet)
router.register(r'products', apiviews.ProductViewSet)
router.register(r'lookup', apiviews.LookUpViewSet)
router.register(r'templates', apiviews.TemplateViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'seeker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/$', apiviews.api_root),
    url(r'api/', include(router.urls)),
    url(r'^api/seek/', apiviews.Seeker, name='seeker'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),

)
