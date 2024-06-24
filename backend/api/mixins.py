from urllib import request
from rest_framework import permissions
from .permissions import IsStaffEditorPermission
from products.models import Products



class StaffEDitorPermissionMixin():
        permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]




class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs): 
          user = self.request.user
          lookup_data = {}
          lookup_data[self.user_field] = user
          qs = super().get_queryset(*args, **kwargs)
          return qs
