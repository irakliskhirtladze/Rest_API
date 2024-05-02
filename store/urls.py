from django.urls import path
from store.views import start_page, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView,\
    ProductDeleteView


urlpatterns = [
    path('', start_page, name='start_page'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
