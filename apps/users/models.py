from django.contrib.auth.models import AbstractUser
from django.db import models
from menu.models import Menu


class User(AbstractUser):
    name = models.CharField("NAME", max_length=32, null=True, help_text="NAME")
    phone = models.CharField("PHONE", max_length=11, null=True, help_text="PHONE")
    github_username = models.CharField("GITHUB ACCOUNT", max_length=50, null=True, help_text="GITHUB ACCOUNT")
    github_token = models.CharField("GITHUB TOKEN", max_length=100, null=True, help_text="GITHUB TOKEN")
    id_rsa_key = models.TextField(null=True)
    id_rsa_pub = models.TextField(null=True)

    class Meta:
        verbose_name = "user"
        ordering = ["id"]
        db_table = 'auth_user'
        permissions = (
            ("can_view_user", "cat view user"),
        )

    def __str__(self):
        return self.username

    def get_view_permissions(self):
        if self.is_superuser:
            return Menu.objects.all()
        return Menu.objects.filter(groups__in=self.groups.all())
