from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.views.generic import ListView, DetailView
from .models import UserProfile


def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = UserProfileForm()
    return render(request, 'user_profile.html', {'form': form})


def success_page(request):
    return render(request, 'success_page.html')


class ForAdminPage(ListView):
    def get(self, request):
        context = {}
        clay = UserProfile.objects.all()
        context['data'] = clay
        return render(request, 'admin/admin.html', context)


class UserDetailView(DetailView):
    model = UserProfile
    template_name = 'admin/user_detail.html'