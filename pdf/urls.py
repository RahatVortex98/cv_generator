from django.urls import path

from pdf import views


urlpatterns = [
    path('',views.accept,name='accept'),
    path('generate-pdf/<int:profile_id>/', views.generate_cv, name='generate_cv'),  # Pass profile_id
    path('download-cv/<int:profile_id>/', views.download_cv, name='download_cv'),  # New URL for downloading CV
    path('confirm-cv/<int:profile_id>/', views.confirm_cv, name='confirm_cv'),  # New URL for confirming CV
]
 
