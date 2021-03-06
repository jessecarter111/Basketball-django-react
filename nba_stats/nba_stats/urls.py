"""nba_stats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
import stats.views as views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/players/$', views.players_list),
    re_path(r'^api/franchises/$', views.franchise_list),
    re_path(r'^api/teams/$', views.team_list),
    re_path(r'^api/games/(?P<player_id>.+)/(?P<season>.+)/$',
            views.player_game_list),
    re_path(r'^api/franchise/(?P<franchise_id>.+)/$',
            views.franchise_seasons)
]
