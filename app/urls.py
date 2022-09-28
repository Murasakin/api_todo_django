from django.urls import path
from app.views import todo_list, todo_details_change_delete

urlpatterns = [
  path('', todo_list),
  path('<int:pk>/', todo_details_change_delete)
]
