from django import forms
from django.template.loader import render_to_string



class GoogleMapPointWidget(forms.TextInput):
    def render(self, name, value, attrs, renderer=None):

        context = {
            'google_api_key': 'AIzaSyD_IUoYFNCLrekGoqKadflBm48FUrxl2TQ',
        }

        html = render_to_string('widgets/google_map_point_widget.html', context)

        parent_html = super().render(name, value, attrs)

        return parent_html + html