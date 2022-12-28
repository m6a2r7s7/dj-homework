from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Tag, Through_Tag

class Through_TagInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            tag = form.cleaned_data.get('main')
            if tag == True:
                count += 1
        if count > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif count == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()

class Through_TagInline(admin.TabularInline):
    model = Through_Tag
    extra = 0
    formset = Through_TagInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [Through_TagInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass