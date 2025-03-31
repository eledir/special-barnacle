"""
URL configuration for locallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# Import the admin module from django.contrib to manage the admin interface
from django.contrib import admin

# Import the path function from django.urls to define URL patterns
from django.urls import path

# Use include() to add URLs from the catalog application and authentication system
from django.urls import include

urlpatterns = [
    # URL pattern for the admin interface
    path('admin/', admin.site.urls),
]

urlpatterns += [
    # URL pattern for the catalog application
    path('catalog/', include('catalog.urls')),
]

# Use static() to add URL mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

# Add URL mapping for static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

# Redirect the base URL to the catalog application
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# Add Django site authentication URLs (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]