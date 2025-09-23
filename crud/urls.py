from rest_framework import routers

from crud.views import FileView, PhotoView, ProductView

router = routers.DefaultRouter()
router.register(r'products', ProductView, basename='product')
router.register(r'photos', PhotoView, basename='photos')
router.register(r'files', FileView, basename='files')


urlpatterns = router.urls