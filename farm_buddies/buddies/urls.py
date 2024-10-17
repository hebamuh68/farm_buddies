from django.urls import path

from farm_buddies.buddies.views import dashboard
from farm_buddies.buddies.views import trackListView
from farm_buddies.users.urls import app_name
from farm_buddies.users.urls import urlpatterns

app_name = "buddies"

urlpatterns = [
    path("", view=dashboard, name="dashboard"),
    path("tracks/", view=trackListView, name="tracks"),
]
