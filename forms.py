"""
Forms for adding and editing Snippets.

"""

from django import newforms as forms
from models import Language

# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary.
attrs_dict = { 'class': 'required' }

class SnippetForm(forms.Form):
    """
    Form used for adding and editing Snippets.
    
    """
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs=attrs_dict))
    description = forms.CharField(widget=forms.Textarea(attrs=attrs_dict))
    code = forms.CharField(widget=forms.Textarea(attrs=attrs_dict))
    tag_list = forms.CharField(max_length=250, widget=forms.TextInput(attrs=attrs_dict))
    language_id = forms.ModelChoiceField(queryset=Language.objects.all(), widget=forms.Select(attrs=attrs_dict))

