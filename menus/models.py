from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Системное имя меню, используется в теге {% draw_menu 'name' %}",
    )
    verbose_name = models.CharField(
        max_length=200,
        blank=True,
        help_text="Человеко-читаемое название (для админки)",
    )

    def __str__(self):
        return self.verbose_name or self.name
    

class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name="items",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )

    title = models.CharField(max_length=200)

    url = models.CharField(
        max_length=255,
        blank=True,
        help_text="Явный URL",
    )
    named_url = models.CharField(
        max_length=100,
        blank=True,
        help_text="Имя URL из urls.py",
    )

    sort_order = models.IntegerField(
        default=0,
        help_text="Порядок сортировки внутри одного уровня",
    )

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return "#"
        if self.url:
            return self.url
        return "#"


