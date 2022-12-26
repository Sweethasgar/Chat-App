from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.index,name="index"),
    path("friend/<str:pk>", views.detail ,name="detail"),
    path("sent_msg/<str:pk>", views.SendMessages ,name="sendmessages"),
    path("rec_msg/<str:pk>", views.receivedMessages ,name="receivedmessages"),
    path("notification/", views.notification,name="notification")
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)