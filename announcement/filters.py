from django_filters import FilterSet
from .models import Respond

class RespondForm(FilterSet):
    class Meta:
        model = Respond
        fields = ('')