from django.urls import path
from .views import (SubscriptionList, SubscriptionDetail)

# api/v1/sub
urlpatterns = [
    path('', SubscriptionList.as_view(), name='sub-list'),
    # api/v1/sub/{pk}
    path('<int:pk>', SubscriptionDetail.as_view(), name='sub-detail')
]