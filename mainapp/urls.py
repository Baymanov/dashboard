from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('billing', views.billing, name="billing"),
    path('profile', views.profile, name="profile"),
    path('rtl', views.rtl, name="rtl"),
    path('sign_in', views.sign_in, name="sign_in"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('tables', views.tables, name="tables"),
    path('virtual_reality', views.virtual_reality, name="virtual_reality"),

    path('create_student', views.create_student, name="create_student"),
    path('update_student/<str:pk>', views.update_student, name="update_student")
]