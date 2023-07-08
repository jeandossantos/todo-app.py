from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    def __str__(self) -> str:
        return f"{self.id} - {self.title}"

    priority_choices = (
        (1, 'Baixa'),
        (2, 'Média'),
        (3, 'Alta'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=55, verbose_name="Título")
    description = models.TextField(blank=True, verbose_name="Descrição")
    priority = models.IntegerField(
        max_length=1, choices=priority_choices, verbose_name="Prioridade", default=0
    )
    deadline = models.DateTimeField(
        null=True, verbose_name="Prazo", blank=True
    )
    done = models.BooleanField(default=False, verbose_name="Concluído")
    created_at = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name="Criado"
    )
