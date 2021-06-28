from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from core.api.serializers import TodoSerializer
from core.models import ToDo


class TodoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        request_data = dict(request.data)
        request_data['user'] = request.user
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(reise_exeption=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
