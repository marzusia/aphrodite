from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from .base.abstracts import UpdatableModel
from .base.mixins import AutoSlugMixin


class Category(UpdatableModel, AutoSlugMixin):
    name = models.CharField(
        help_text=_('The name of this category.'),
        max_length=128,
    )
    slug = models.SlugField(
        help_text=_('How this article will appear in URLs (leave blank for auto).'),
        null=False,
        blank=True,
        db_index=True,
        unique=True,
        max_length=128,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Page(UpdatableModel, AutoSlugMixin):
    auto_slug_populate_from = 'title'

    title = models.CharField(
        help_text=_('The title of this page.'),
        max_length=128,
    )
    category = models.ForeignKey(
        Category,
        help_text=_('The category that this page belongs to. Will appear in the page\'s URL.'),
        on_delete=models.CASCADE,
    )
    subtitle = models.TextField(
        help_text=_('The subtitle to appear below the title.'),
        blank=True,
    )
    slug = models.SlugField(
        help_text=_('How this article will appear in URLs (leave blank for auto).'),
        null=False,
        blank=True,
        db_index=True,
        unique=True,
        max_length=128,
    )
    summary = models.TextField(
        help_text=_('A short summary of the article for the homepage.'),
        blank=True,
    )
    content = RichTextUploadingField(
        help_text=_('The content of this page.'),
        blank=True,
    )
    banner_image = models.ImageField(
        help_text=_('The image that should appear at the very top of the page. It should be wide, and high quality.'),
        null=True,
        blank=True,
        upload_to='page/banner/',
    )
    index_page = models.BooleanField(
        help_text=_('Should this page be the index page of the website?'),
        default=False,
    )

    def __str__(self):
        return self.title


class MenuItem(UpdatableModel):
    """
    Represents a root item on the website's menu.
    """
    label = models.CharField(
        help_text=_('The label for this menu item.'),
        max_length=128,
    )
    index = models.IntegerField(
        help_text=_('The index (order) that this menu item should appear in the menu.'),
        unique=True,
    )

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['index']


class MenuSection(UpdatableModel):
    """
    Represents a section of navigable links belonging to a root menu item.
    """
    menu = models.ForeignKey(
        MenuItem,
        help_text=_('The menu item this section should appear below.'),
        on_delete=models.CASCADE,
        related_name='sections',
    )
    heading = models.CharField(
        help_text=_('The heading for this menu section, to appear above its sub-items.'),
        max_length=128,
    )
    index = models.IntegerField(
        help_text=_('The index (order) that this section should appear in the submenu.'),
    )

    def __str__(self):
        return '%s > %s' % (self.menu, self.heading)

    class Meta:
        unique_together = (('menu', 'index'),)
        ordering = ['index']


class MenuSectionItem(UpdatableModel):
    """
    Represents a navigable link belonging to a submenu (menu section).
    """
    section = models.ForeignKey(
        MenuSection,
        help_text=_('The menu section this link should belong to.'),
        on_delete=models.CASCADE,
        related_name='items',
    )
    page = models.ForeignKey(
        Page,
        help_text=_('The page this link should navigate to.'),
        on_delete=models.CASCADE,
    )
    label = models.CharField(
        help_text=_('The label for this link.'),
        max_length=128,
    )
    index = models.IntegerField(
        help_text=_('The index (order) that this link should appear in the section.'),
    )

    @property
    def link(self):
        return reverse('page.show', kwargs={
            'category': self.page.category.slug,
            'slug': self.page.slug,
        })

    def __str__(self):
        return '%s > %s' % (self.section, self.label)

    class Meta:
        unique_together = (('section', 'index'),)
        ordering = ['index']


class QuickLink(UpdatableModel):
    label = models.CharField(
        help_text=_('The label for this link.'),
        max_length=128,
    )
    page = models.ForeignKey(
        Page,
        help_text=_('The page this link should navigate to.'),
        on_delete=models.CASCADE,
    )
    index = models.IntegerField(
        help_text=_('The index (order) that this link should appear in the menu.'),
        unique=True,
    )

    @property
    def link(self):
        return reverse('page.show', kwargs={
            'category': self.page.category.slug,
            'slug': self.page.slug,
        })

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['index']
