from django.conf.urls import url
from django.urls import path
from . import views

app_name = "Journal"

urlpatterns = [
    path('Journal', views.landing_page, name='landing_page'),
    path('login', views.login_user, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('register', views.register, name='register'),
    path('Journal/entry/<int:pk>', views.entry, name='entry'),
    path('Journal/entry_list/<int:pk>', views.entry_list, name='entry_list'),
    path('Journal/entry_list/edit_entry/<int:entry_id>', views.entry_edit, name='entry_edit'),
    path('Journal/entry_list/edit_entry/<int:entry_id>/update', views.entry_update, name='entry_update'),
]
