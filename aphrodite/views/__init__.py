from django.views.generic import TemplateView

from ..models.content import MenuItem, QuickLink
from ..models.course import Department


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menuItems'] = MenuItem.objects.prefetch_related('sections__items').all()
        context['quicklinks'] = QuickLink.objects.all()
        context['departments'] = Department.objects.all()
        return context
