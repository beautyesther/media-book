from django.forms import ModelForm
from creatMedia.models import CreateMedia


class CreateMediaForm(ModelForm):
    class Meta:
        model = CreateMedia
        fields = [
            'userName',
            'image',
            'description'
        ]
