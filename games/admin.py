from django.contrib import admin
from .models import WebGame, Score
from django.contrib import admin

# Register your models here.


class ScoreManager(admin.ModelAdmin):
    ordering = ('-last_played', )
    list_display = ('player', 'game', 'score')
    list_filter = ('player', 'game')


admin.site.register(WebGame)
admin.site.register(Score, ScoreManager)
