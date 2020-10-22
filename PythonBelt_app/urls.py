from django.urls import path
from . import views

urlpatterns = [
    # '' is localhost
    path('', views.index),
    #-------------------------------------------------------------------------------------------
    # 'main' is my main html
    path('main', views.main),
    #-------------------------------------------------------------------------------------------
    # 'register' is the register process
    path('register', views.register),
    #-------------------------------------------------------------------------------------------
    # 'dashboard' shows the tables
    path('dashboard', views.home),
    #-------------------------------------------------------------------------------------------
    # logout is the logout button process
    path('logout', views.logout),
    #-------------------------------------------------------------------------------------------
    # 'login' is the login button process
    path('login', views.login),
    #-------------------------------------------------------------------------------------------
    # 'wish_items/create' is the addItem page that allows the User to create a new wishlist item
    path('wish_items/create', views.addItem),
    #-------------------------------------------------------------------------------------------
    # 'processItem' is the process for the created item being processed and added to the dashboard. 
    path('processItem', views.processItem),
    #-------------------------------------------------------------------------------------------
    # 'wish_items/<wishid>' is the redirect show page for the item being added or the item that was already added.
    path('wish_items/<wishid>', views.show),
    #-------------------------------------------------------------------------------------------
    # 'wishAdd/<wishid>' is the button that adds a wish to the liked list. 
    path('wishAdd/<wishid>', views.wishAdd),
    #-------------------------------------------------------------------------------------------
    # 'removeWish/<wishid>' is the button that removes a wish item from the list of liked wish items
    path('removeWish/<wishid>', views.removeWish),
    #-------------------------------------------------------------------------------------------
    # 'deleteWish/<wishid>' is the button that removes a wish item from the list of liked wish items
    path('deleteWish/<wishid>', views.deleteWish),
]