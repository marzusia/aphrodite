from django.http import Http404

from . import BaseView
from ..models.content import Page


class PageView(BaseView):
    template_name = 'aphrodite/content/show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.setdefault('index', False)
        context['page'] = None

        if context['index']:
            context['page'] = Page.objects.filter(index_page=True).first()
        else:
            context['page'] = Page.objects.filter(
                category__slug=context['category'],
                slug=context['slug']
            ).first()

        if context['page'] is None:
            raise Http404

        return context