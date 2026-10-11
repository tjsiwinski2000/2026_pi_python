from django.db import models

# Create your models here.
class HangmanWord(models.Model):

    class Difficulty(models.TextChoices):
        EASY   = 'easy',   'Easy'
        MEDIUM = 'medium', 'Medium'
        HARD   = 'hard',   'Hard'

    word       = models.CharField(max_length=100)
    hint       = models.TextField()
    difficulty = models.CharField(
        max_length=10,
        choices=Difficulty.choices,
        default=Difficulty.MEDIUM,
    )

    def __str__(self):
        return f"{self.word} ({self.difficulty})"