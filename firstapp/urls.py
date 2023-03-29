from django.urls import path, re_path
from . import views


app_name = 'firstapp'
urlpatterns = [
    path('', views.trang_chu, name=''),
    path('tham-so/<int:so_2>/<int:so_1>/', views.tham_so, name=''),
    re_path(r'^read-year/(?P<year>[0-9]{4})/$', views.read_year, name=''),  # https://docs.python.org/3/library/re.html
    re_path(r'^read-month-year/(?P<month>[0-9]{2})/(?P<year>[0-9]{4})/$', views.read_month_year, name=''),
    path('ngay-hien-hanh', views.ngay_hien_hanh),
    path('demo-tag/', views.tinh_diem_tb),
    path('cart/', views.cart),
    path('add-category/', views.create_category),
    path('websites/', views.read_websites, name='websites'),
    path('contents/', views.read_contents, name='contents'),
    path('contents/<int:pk>/', views.contents_by_web, name='contents_by_web'),
    path('contents-2/<int:id>/', views.contents_by_web_2, name='contents_by_web_2'),
    path('demo-ckeditor/', views.demo_ckeditor, name='demo_ckeditor'),
]

