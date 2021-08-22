from django.contrib.auth.models import Group
from django.db import models


class Menu(models.Model):
    path = models.CharField("directory name/file name", max_length=100, default='/', help_text="目录名或文件名")
    icon = models.CharField("icon name", max_length=32, null=True, help_text="icon name")
    title = models.CharField("路由显示名", max_length=255, null=False, help_text="路由显示名")
    show = models.BooleanField("该路由是否显示", default=False, help_text="该路由是否显示")
    parent = models.ForeignKey("self", null=True, verbose_name="parent menu", help_text="parent menu", on_delete=models.CASCADE)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name="menu_set",
        related_query_name="menu",
        help_text="belong groups",
    )

    class Meta:
        ordering = ["id"]
        db_table = "view_menu"

    def __str__(self):
        return "{} {}".format(self.title, self.path)
