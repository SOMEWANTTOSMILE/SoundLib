from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from premium.serializers import PremiumInfoSerializer, GetPremiumSerializer, UserPremiumSerializer
from premium.models import ServiceProduct, UserSubscription


class PremiumInfoListView(ListAPIView):
    queryset = ServiceProduct.objects.all()
    serializer_class = PremiumInfoSerializer
    permission_classes = (AllowAny, )


class GetPremiumView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = GetPremiumSerializer

    def post(self, request):
        serializer = GetPremiumSerializer(data=request.data,
                                          context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


class UserPremiumView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserPremiumSerializer

    def get(self, request):
        user = request.user
        queryset = UserSubscription.objects.filter(user=user).all()
        serializer = UserPremiumSerializer(queryset, many=True)
        return Response(serializer.data)



