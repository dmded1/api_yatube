from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.views import PostViewSet, CommentViewSet, GroupViewSet


router1 = DefaultRouter()

router1.register('posts', PostViewSet, basename='posts')
router1.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                 basename='comments')
router1.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router1.urls)),
]
