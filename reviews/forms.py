from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):

    """ Create Review Form Definition """

    accuracy = forms.IntegerField(min_value=1, max_value=5)
    communication = forms.IntegerField(min_value=1, max_value=5)
    cleaniness = forms.IntegerField(min_value=1, max_value=5)
    location = forms.IntegerField(min_value=1, max_value=5)
    check_in = forms.IntegerField(min_value=1, max_value=5)
    value = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = models.Review
        fields = (
            "review",
            "accuracy",
            "communication",
            "cleaniness",
            "location",
            "check_in",
            "value",
        )

    def save(self):
        review = super().save(commit=False)
        return review
