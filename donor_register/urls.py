from django.urls import path,include
from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.donor_form,name='donor_insert'), # get and post req. for insert operation
    path('<int:id>/', views.donor_form,name='donor_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.donor_delete,name='donor_delete'),
    path('list/',views.donor_list,name='donor_list'), # get req. to retrieve and display all records
    path('', views.donor_form,name="home")
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)