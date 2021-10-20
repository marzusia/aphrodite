from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse

from .base.abstracts import UpdatableModel
from .base.mixins import AutoSlugMixin


class Department(UpdatableModel, AutoSlugMixin):
    auto_slug_populate_from = 'preslug'

    name = models.CharField(
        help_text=_('The short, friendly name of this department, e.g Science.'),
        max_length=128,
    )
    full_name = models.CharField(
        help_text=_('The full name of this department, e.g Department of Science.'),
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
    description = models.TextField(
        help_text=_('A short introduction to this department.'),
    )
    promo_image = models.ImageField(
        help_text=_('A small image exemplifying this department, to appear on the department page.'),
        null=True,
        blank=True,
        upload_to='department/'
    )

    @property
    def link(self):
        return reverse('department.show', kwargs={'slug': self.slug})

    @property
    def preslug(self):
        return 'Dept %s' % self.name

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Course(UpdatableModel, AutoSlugMixin):
    class DegreeLevel:
        UNDERGRAD = 'undergrad'
        POSTGRAD = 'postgrad'
        CHOICES = (
            (UNDERGRAD, 'Undergraduate'),
            (POSTGRAD, 'Postgraduate'),
        )

    department = models.ForeignKey(
        Department,
        help_text=_('The department that provides this course.'),
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        help_text=_('The name of this course.'),
        max_length=128,
    )
    accreditation = models.CharField(
        help_text=_('The accreditation achieved by this course, e.g BA (Hons), PhD, etc.'),
        max_length=32,
    )
    code = models.CharField(
        help_text=_(
            'A short unique code for this course, usually an uppercase '
            'abbreviation, such as LING for Linguistics.'
        ),
        max_length=32,
    )
    slug = models.SlugField(
        help_text=_('How this article will appear in URLs (leave blank for auto).'),
        null=False,
        blank=True,
        db_index=True,
        unique=True,
        max_length=128,
    )
    level = models.CharField(
        help_text=_('The degree level of this qualification.'),
        max_length=128,
        choices=DegreeLevel.CHOICES,
    )
    length = models.IntegerField(
        help_text=_('The length of this course in years.'),
    )
    description = models.TextField(
        help_text=_('A short introduction to this course.'),
    )
    requirements = models.TextField(
        help_text=_('A short description of the academic/other requirements for admission to this course.'),
    )
    promo_image = models.ImageField(
        help_text=_('A small image exemplifying this course, to appear on the course page.'),
        null=True,
        blank=True,
        upload_to='course/'
    )

    @property
    def link(self):
        return reverse('course.show', kwargs={
            'department': self.department.slug,
            'slug': self.slug,
        })

    def __str__(self):
        return '%s %s' % (self.name, self.accreditation)

    class Meta:
        ordering = ['name']

class Module(UpdatableModel):
    course = models.ForeignKey(
        Course,
        help_text=_('The course to which this module belongs.'),
        on_delete=models.CASCADE,
    )
    code = models.CharField(
        help_text=_(
            'A short code unique to this module. Typically made up of the '
            'course abbreviation (e.g LING for Linguistics) followed by a '
            'three-digit number, whereby the first is the course year and '
            'the second two are arbitrary and unique. An example would be '
            'LING102 as a first-year module for Semantics, and LING204 as '
            'a second-year module for Pragmatics.'
        ),
        unique=True,
        max_length=32,
    )
    name = models.CharField(
        help_text=_('The friendly name of the module, e.g Reinassance Art.'),
        max_length=128,
    )
    description = models.TextField(
        help_text=_('A short introduction to this module.'),
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['code']
