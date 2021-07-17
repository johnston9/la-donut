"""Widget for the Recipe App
"""
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """Widget for the image field
    """
    clear_checkbox_label = _('To change images click here then update \
        before adding new image')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/widgets_custom/clearable_file_input.html'
