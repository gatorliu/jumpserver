from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = ['SafeRoleBinding']


class SafeRoleBinding(models.Model):
    """ 用户-保险箱级别的角色绑定 """
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name=_('User'))
    role = models.ForeignKey('rbac.Role', on_delete=models.PROTECT, verbose_name=_('Role'))
    # only safe-role
    safe = models.ForeignKey('accounts.Safe', on_delete=models.PROTECT, verbose_name=_('Safe'))

    class Meta:
        unique_together = ('user', 'role', 'safe')