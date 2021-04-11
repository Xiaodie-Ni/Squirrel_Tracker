from django.forms import ModelForm
from .models import Sighting


class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SightingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
