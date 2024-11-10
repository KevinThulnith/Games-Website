from django.conf import settings
from django.db import models


# Create your models here.
class WebGame(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


user = settings.AUTH_USER_MODEL


class Score(models.Model):
    player = models.ForeignKey(user, on_delete=models.CASCADE)
    game = models.ForeignKey(WebGame, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    last_played = models.DateTimeField(verbose_name='last played',
                                       auto_now=True)

    def __str__(self):
        return f" {self.score} "

    def myView(self):
        return f' <li class="row"><div class="name">{self.player}</div><div class="score">{self.score}</div></li>'

    class Meta:
        unique_together = ('player', 'game')