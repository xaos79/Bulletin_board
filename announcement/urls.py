from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnnouncementListView.as_view(), name='home'),
    path('announcement/<int:pk>', views.AnnouncementDetailView.as_view(), name='detail'),
    path('create_announcement', views.AnnouncementCreateView.as_view(), name='create'),
    path('delete/<int:pk>', views.AnnouncementDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.AnnouncementUpdateView.as_view(), name='update'),
    path('add_respond/<int:pk>', views.add_respond, name='add_respond'),
    path('your_responds', views.RespondListView.as_view(), name='responds'),
    path('your_responds/<int:pk>', views.RespondDetailView.as_view(), name='respond_detail'),
    path('your_responds_announcement/<int:pk>', views.RespondAnnouncementListView.as_view(),
         name='responds_announcement'),
    path('delete_respond/<int:pk>', views.delete_respond, name='delete_respond'),
    path('accept_respond/<int:pk>', views.accept_respond, name='accept_respond'),
]
