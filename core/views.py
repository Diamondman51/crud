
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated


from core.custom_perms import IsAdminOrReadOnly
from core.models import User
from core.serializers import UserSer

class UserView(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    serializer_class = UserSer