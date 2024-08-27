from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from .models import Todo


@api_view(["get"])
def todo_list(request):
    data = Todo.objects.all()
    serializer = TodoSerializer(data, many=True)
    return Response(serializer.data)

@api_view(["get"])
def todo_detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)