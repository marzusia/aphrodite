from django.contrib import admin

from .models.content import \
    Category, Page, MenuItem, MenuSection, \
    MenuSectionItem, QuickLink
from .models.course import Department, Course, Module


for model in [
    # Content
    Category,
    Page,
    MenuItem,
    MenuSection,
    MenuSectionItem,
    QuickLink,
    # Course
    Department,
    Course,
    Module,
]: admin.site.register(model)