from django.contrib import admin
from django.urls import path
from django.urls import re_path

from ..urls import urlpatterns


class FakeViewForUrl(object):

    def __call__(self):
        raise Exception("Should not get called.")


urlpatterns += [
    re_path(r"^admin/", admin.site.urls),
    path("the/app/", FakeViewForUrl, name="the_app"),
    path("accounts/signup/", FakeViewForUrl, name="signup"),
    path("password/reset/confirm/<path:token>/", FakeViewForUrl,
         name="password_reset"),
]
