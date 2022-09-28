from django.urls import path
from app.views import TodoListCreate, TodoDetailChangeDelete

urlpatterns = [
  path('', TodoListCreate.as_view()),
  path('<int:pk>/', TodoDetailChangeDelete.as_view())
]
