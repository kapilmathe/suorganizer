from django import forms
from .models import Tag,NewsLink,Startup
from django.core.exceptions import ValidationError

class SlugCleanMixin:
    """Mixin class for slug cleaning method."""
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        else:
            return new_slug

class TagForm(forms.ModelForm,SlugCleanMixin):
    class Meta:
        model = Tag
        fields = '__all__'

    # def save(self):
    #     new_tag = Tag.objects.create(
    #         name= self.cleaned_data['name'],
    #         slug = self.cleaned_data['slug']
    #     )
    #     return new_tag

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug =='create':
            raise ValidationError('Slug may not be "create".')

        return new_slug

    def clean_name(self):
        return self.cleaned_data['name']



class NewsLinkForm(forms.ModelForm):
    class Meta:
        model = NewsLink
        fields = '__all__'

class StartupForm(forms.ModelForm,SlugCleanMixin):
    class Meta:
        model = Startup
        fields = '__all__'

    # def clean_slug(self):
    #     new_slug = (self.cleaned_data['slug'].lower())
    #     if new_slug == 'create':
    #         raise ValidationError('Slug may not be "create".')
    #     return new_slug

    def clean_name(self):
        return self.cleaned_data['name']
