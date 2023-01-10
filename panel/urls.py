from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel, name="panel"),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    path('add-panel/', views.AddPlanView.as_view(), name="add_plan"),
    path('delete-panel/<int:pk>/', views.DeletePlanView.as_view(), name="delete_plan"),
    path('update-panel/<int:pk>/', views.UpdatePlanView.as_view(), name="update_plan"),

    path('add-client/', views.AddClientView.as_view(), name="add_client"),
    path('view-client/<str:pk>/', views.view_client, name="view_client"),
    path('delet-client/<int:pk>/', views.DeleteClientView.as_view(), name="delete_client"),
    path('update-client/<str:pk>/', views.update_client, name="update_client"),

    path('register/', views.RegisterEmployeeView.as_view(), name='register'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('login', views.LoginEmployeeView.as_view(), name="login"),
    path('login/password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         views.auth_views.PasswordResetConfirmView.as_view(template_name='panel/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         views.auth_views.PasswordResetCompleteView.as_view(template_name='panel/password_reset_complete.html'),
         name='password_reset_complete'),
]
