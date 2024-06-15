from djoser.views import UserViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from users.serializers import FillingProfileSerializer
from users.models import CustomUser


# Create your views here.
class TestLoginView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        return Response('Welcome')


class ActivateUser(UserViewSet):

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        kwargs['data'] = {
            'uid': self.kwargs['uid'],
            'token': self.kwargs['token']}
        return serializer_class(*args, **kwargs)


class FillingProfileView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = FillingProfileSerializer

    def put(self, request, *args, **kwargs):
        user = CustomUser.objects.get(email=request.user)
        data = request.data
        serializer = FillingProfileSerializer(data=request.data, instance=user, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})





