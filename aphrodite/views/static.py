from . import BaseView


class IndexView(BaseView):
    template_name = 'aphrodite/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context