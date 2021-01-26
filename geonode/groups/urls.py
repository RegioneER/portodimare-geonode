# -*- coding: utf-8 -*-
#
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#

from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import GroupDetailView, GroupActivityView
from . import views

urlpatterns = [  # 'geonode.groups.views',
    url(r'^$', login_required(TemplateView.as_view(
        template_name='groups/group_list.html')), name="group_list"),

    url(r'^categories/$',
        login_required(TemplateView.as_view(
            template_name="groups/category_list.html")),
        name="group_category_list"),
    url(r'^categories/_create/$', 
        login_required(views.group_category_create),
        name="group_category_create"),
    url(r'^categories/(?P<slug>[-\w]+)/$',
        login_required(views.group_category_detail), name="group_category_detail"),
    url(r'^categories/(?P<slug>[-\w]+)/update/$', 
        login_required(views.group_category_update), name="group_category_update"),
    url(r'^create/$', login_required(views.group_create), name="group_create"),
    url(r'^group/(?P<slug>[-\w]+)/$',
        login_required(GroupDetailView.as_view()), name='group_detail'),
    url(r'^group/(?P<slug>[-\w]+)/update/$',
        login_required(views.group_update), name='group_update'),
    url(r'^group/(?P<slug>[-\w]+)/members/$',
        login_required(views.group_members), name='group_members'),
    url(r'^group/(?P<slug>[-\w]+)/members_add/$',
        login_required(views.group_members_add), name='group_members_add'),
    url(r'^group/(?P<slug>[-\w]+)/member_remove/(?P<username>.+)$', 
        login_required(views.group_member_remove),
        name='group_member_remove'),
    url(r'^group/(?P<slug>[-\w]+)/remove/$',
        login_required(views.group_remove), name='group_remove'),
    url(r'^group/(?P<slug>[-\w]+)/join/$',
        login_required(views.group_join), name='group_join'),
    url(r'^group/(?P<slug>[-\w]+)/activity/$',
        login_required(GroupActivityView.as_view()), name='group_activity'),
]
