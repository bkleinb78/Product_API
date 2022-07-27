from django.urls import path
from . import views

urlpatterns = [
  path('', views.products_list),
  path('<int:pk>/', views.products_detail),
  path('reviews', views.reviews_list),
  path('post-review/<int:fk>/', views.reviews_list),
  path('reviews/<int:pk>/', views.reviews_detail),
  path('reviews-by-product/<int:fk>/', views.all_reviews_by_product),
]