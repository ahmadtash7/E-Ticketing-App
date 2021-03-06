"""nusttickets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import Buy, Index, Events, Pay, Tickets, SignUp, LoginView, LogoutView,Reserve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('events/', include('events.urls')),
    path('admin/', admin.site.urls),
    path('', Index, name='index'),
    path('event/<str:oid>', Events, name='event'),
    path('ticketDetails/<str:oid>', Tickets, name='ticket'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('signup/', SignUp, name='signup'),
    path('buy/<str:oid>/', Buy, name='buy'),
    path('pay/<str:oid>/', Pay, name='pay'),
    path('reserve/<str:oid>/', Reserve, name='reserve'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
