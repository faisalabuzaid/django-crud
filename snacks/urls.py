from snacks.views import (
    AboutPageView,
    HomePageView,
    SnackDetailView,
    SnackListView,
    SnackCreateView,
    SnackUpdateView,
    SnackDeleteView
)

from django.urls import path

urlpatterns = [
    path('', SnackListView.as_view(), name="snack_list"),
    path('<int:pk>/', SnackDetailView.as_view(), name="snack_detail"),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('create/', SnackCreateView.as_view(), name='snack_create'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete')
]
