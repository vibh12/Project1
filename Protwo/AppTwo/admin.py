# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from AppTwo.models import Topic, Webpage, AccessRecord

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)

# Superuser
# vibhu
# vibhorgoy@gmail.com
# appl1234

