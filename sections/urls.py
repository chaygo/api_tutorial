from django.urls import path
from . import views
app_name="sections"
urlpatterns = [
    path('sections/',views.SectionViews.as_view(),name="sections"),
    path('sections/<int:pk>/',views.SectionDetail.as_view(),name="sectionsdetail"),
    path('workers/',views.WorkerViews.as_view(),name="workers"),
    path('workers/<int:pk>/',views.WorkerDetail.as_view(),name="workersdetail"),
    path('works/<int:pk>/',views.WorksDetail.as_view(),name="worksdetail"),
    
]
