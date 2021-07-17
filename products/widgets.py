"""Widget for the Product App Image field
"""
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """Custom Widget for the Product App Image field
    """
    clear_checkbox_label = _('To change images first check box then click update \
        to delete the old one before selecting new image')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/widgets_custom/clearable_file_input.html'
