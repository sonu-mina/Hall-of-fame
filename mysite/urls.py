
from django.contrib import admin,auth
from django.urls import path,include
from halls import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard',views.dashboard,name='dashboard'),
    path('',views.home,name='home'),
    path('signup',views.signup.as_view(),name='signup'),
    path('login',auth_views.LoginView.as_view(),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('halloffame/create',views.CreateHall.as_view(),name='create_hall'),
    path('halloffame/<int:pk>',views.DetailHall.as_view(),name='detail_hall'),
    path('halloffame/<int:pk>/update',views.UpdateHall.as_view(),name='update_hall'),
    path('halloffame/<int:pk>/delete',views.DeleteHall.as_view(),name='delete_hall'),
    path('halloffame/<int:pk>/add_video',views.add_video,name='add_video'),
    path('video/search',views.video_search,name='video_search'),
    path('video/<int:pk>/delete_video',views.DeleteVideo.as_view(),name='delete_video'),
]

urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)