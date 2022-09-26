from rest_framework import api_view
from rest_framework.response import Response
from app.serializers import TodoSerializer
from app.models import Todo

@map_view(['GET'])
def todo_list(request):
  todo = Todo.objects,all()
  json = TodoSerializer(todo, many=True)
  return Response(json.data)