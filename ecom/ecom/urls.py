"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('aboutus/',views.aboutus),
    path('shop/',views.shop),
    path('login/',views.ulogin),
    path('register/',views.register),
    path('logout/',views.ulogout),
    path('storybook/<cid>/',views.storybook),
    path('biography/<cid>/',views.biography),
    path('lkgukg/<cid>/',views.lkgukg),
    path('firsttofifth/<cid>/',views.firsttofifth),
    path('sixthtotenth/<cid>/',views.sixthtotenth),
    path('writtinginstruments/<cid>/',views.writtinginstruments),
    path('product_details/<pid>/',views.product_details),
    path('addtocart/<pid>',views.addtocart),
    path('cart/',views.viewcart),
    path('delete/<cid>/',views.deletecart),
    path('updateqty/<x>/<cid>/',views.updateqty),
    path('checkaddress/',views.checkaddress),
    path('fetchorder/',views.fetchorder),
    path('placeorder/',views.placeorder),
    path('makepayment/',views.makepayment),
    path('email_send/',views.email_send),
    # path('order_history/',views.order_history),
    path('update_order_status/',views.update_order_status),
    path('search/',views.search,name="search"),
    path("profile/", views.userinfo, name="profile"),
    path("delete_user/<int:uid>/", views.delete_user, name="delete"),
    path('myorder/',views.myorder),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)