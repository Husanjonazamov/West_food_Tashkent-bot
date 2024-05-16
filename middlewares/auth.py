# custom_middleware.py
from django.shortcuts import redirect
from django.urls import resolve, reverse


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        view_func = resolve(request.path_info)
        if view_func.app_name in ['sponsors', "control", "adm"]:
            if request.user.is_authenticated:
                return self.get_response(request)
            else:
                return redirect(reverse("login"))

        return self.get_response(request)
