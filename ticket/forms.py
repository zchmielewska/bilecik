from django import forms

from ticket import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ("title", "model", "year", "month", "version")
