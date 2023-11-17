"""
URL configuration for pddikti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers
router = routers.DefaultRouter()

from web import views
from django.conf import settings  #
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    # path('', include(router.urls)),
    path('pddikti/detail-jabatan-dosen', views.DetailUnivDosen.as_view()),
    path('pddikti/detail_mhs', views.Detail_Mahasiswa.as_view()),
    path('pddikti/detail_dosen', views.Detail_Dosen.as_view()),
    path('pddikti/detail_univ', views.Detail_Univ.as_view()),
    path('pddikti/detail_prodi', views.Detail_Prodi.as_view()),
    path('pddikti/search', views.SearchAll.as_view()),
    path('pddikti/search-mhs', views.SearchMahasiswa.as_view()),
    path('pddikti/search-dosen', views.SearchDosen.as_view()),
    path('pddikti/search-prodi', views.SearchProdi.as_view()),
    path('pddikti/search-pt', views.SearchPt.as_view()),
    path('pddikti/search-by-category', views.SearchBycategory.as_view()),
    path('pddikti/all-campus', views.GetAllCampus.as_view()),
    path('pddikti/counting-pt', views.CountingPT.as_view()),

    
]
