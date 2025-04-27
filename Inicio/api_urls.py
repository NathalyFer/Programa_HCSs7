from rest_framework.routers import DefaultRouter
from . import views

#enrutador de api rest
router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet, basename='usuario')
router.register(r'productos', views.ProductoViewSet, basename='producto')
router.register(r'categorias', views.CategoriaViewSet, basename='categoria')
router.register(r'tipousuarios', views.TipoUsuarioViewSet, basename='tipousuario')
router.register(r'tipoproductos', views.TipoProdViewSet, basename='tipoproducto')
router.register(r'marcas', views.MarcaViewSet, basename='marca')
router.register(r'modelos', views.ModeloViewSet, basename='modelo')
router.register(r'ventas', views.VentaViewSet, basename='venta')
router.register(r'detalles', views.DetalleViewSet, basename='detalle')
router.register(r'direcciones', views.DireccionViewSet, basename='direccion')
router.register(r'regiones', views.RegionViewSet, basename='region')
router.register(r'comunas', views.ComunaViewSet, basename='comuna')

urlpatterns = router.urls