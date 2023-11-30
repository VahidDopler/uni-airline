# Create your views here.
from django.views.generic import ListView

from .models import normal_user


class UserListView(ListView):
    model = normal_user
    template_name = 'users/all_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = normal_user.objects.all()
        return context
