
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import DashboardView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # /account/login/
    # /redirect_authenticated_user = True : fonction on l'utilise quand la session est ouverte il ne demande pas de nouveau le login er password
    path('login/', view=LoginView.as_view(template_name="account/login.html",
                                          redirect_authenticated_user=True), name="login"),
    # /account/logout
    path('logout/', view=LogoutView.as_view(), name="logout"),
    # /account/dashboard
    path('dashboard/', view=DashboardView.as_view(), name="dashboard"),

]
