from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from farm_buddies.buddies.models import Track


@login_required
def dashboard(request):
    context = {}
    return render(request, "buddies/dashboard.html", context)


class TrackListView(LoginRequiredMixin, ListView):
    model = Track
    template_name = "buddies/tracks-list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["page_title"] = "Tracks"
        return context

    def get_queryset(self):
        return Track.objects.all()


trackListView = TrackListView.as_view()
