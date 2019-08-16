from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from pc.models import *


class UsersView(TemplateView):
    template_name = "users_list.html"

    def get(self, request, *args, **kwargs):
        context = super(UsersView, self).get_context_data(**kwargs)

        users = Users.objects.all()  # データベースからオブジェクトを取得して
        context['users'] = users  # 入れ物に入れる


        return render(self.request, self.template_name, context)
