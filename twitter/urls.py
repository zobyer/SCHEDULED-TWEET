from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    #Auth
    path('login', views.login, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('tweet', views.postTweet, name='postTweet'),
    path('gen-url-verifier', views.generateTwitterVerifierUrl, name='gen-url-verifier'),
    path('my-tweets', views.showMyTweets, name='my-tweets'),
]