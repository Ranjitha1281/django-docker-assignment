from django.contrib import admin
from django.urls import path
from items.views import item_list  # ✅ Import your view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', item_list),  # ✅ This connects /items/ to your view
]
