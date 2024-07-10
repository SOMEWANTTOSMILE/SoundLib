from django.urls import path
from premium.views import PremiumInfoListView, GetPremiumView, UserPremiumView


urlpatterns = [
    path('info/', PremiumInfoListView.as_view(), name='Premium-info/'),
    path('premium/', GetPremiumView.as_view(), name='get-premium'),
    path('my-premium/', UserPremiumView.as_view(), name='my-premium')
]
