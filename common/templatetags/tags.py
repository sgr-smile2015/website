from django import template
from django.utils.html import mark_safe
from datetime import datetime
#from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag
def render_app_name(admin_class):
    return admin_class.model._meta.verbose_name


@register.simple_tag
def get_query_sets(admin_class):
    return admin_class.model.objects.all()


@register.simple_tag
def build_table_row(obj, admin_class):
    """
    obj: crm.models.Customer
    admin_class: common.base_admin.CustomerAdmin
    return: mark_safe string
    """
    row_ele = ""
    for column in admin_class.list_display:
        field_obj = obj._meta.get_field(column)
        #choice tpye
        if field_obj.choices:
            data = getattr(obj, "get_%s_display" % column)()
        else:
            data = getattr(obj, column)
        try:
            if field_obj.auto_now_add:
                s = getattr(obj, 'date')
                data = s.strftime('%Y-%m-%d %H:%M:%S')
        except Exception:
            pass

        row_ele += '<td>%s</td>' % data
    return mark_safe(row_ele)


@register.simple_tag
def render_page_ele(loop_counter, query_sets):
    if abs(query_sets.number - loop_counter) <= 1:
        ele_class = ""
        if query_sets.number == loop_counter:
            ele_class = "active"
        ele = '''<li class="%s"><a href="?page=%s">%s</a></li>''' % (ele_class, loop_counter, loop_counter)

    return mark_safe(ele)
