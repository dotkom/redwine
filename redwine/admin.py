from django.contrib import admin
from .models import Penalty


class PenaltyAdmin(admin.ModelAdmin):
    list_display = ("to", "giver", "amount", "committee", "date", "deleted", "item")
    list_filter = ("to", "giver", "amount", "committee", "date", "deleted", "item")

admin.site.register(Penalty, PenaltyAdmin)
