# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.simple_tag
def active_page(request, view_name=None):
    from django.core.urlresolvers import reverse, Resolver404
    # XXX: BREAKPOINT!!
    import pdb
    pdb.set_trace()
    if not request:
        return ""
    if not view_name or view_name == '':
        return ""
    try:
        return "active" if reverse(view_name) == request.path_info else ""
    except Resolver404:
        return ""
