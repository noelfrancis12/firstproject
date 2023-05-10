from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.djafun,name='djafun'),
    path('link',views.link,name='link'),
    path('link2',views.link2,name='link2'),
    path('link3',views.link3,name='link3'),
    path('ktm',views.ktm,name='ktm'),
    path('wyd',views.wyd,name='wyd'),
    path('ekm',views.ekm,name='ekm'),
    path('back',views.back,name='back')
]
