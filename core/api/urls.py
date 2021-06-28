from rest_framework.routers import DefaultRouter

from core.api.views import TodoViewSet

router = DefaultRouter()
router.register('todos', TodoViewSet)

urlpatterns = router.urls
