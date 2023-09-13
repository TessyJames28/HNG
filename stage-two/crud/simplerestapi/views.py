from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework.exceptions import NotFound

# Create your views here.
class PersonView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        limit = self.request.GET.get('limit')           
        if limit:
            return super().get_queryset()[:int(limit)]
        return super().get_queryset()

    
class SinglePersonView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    def get_object(self):
        user_id = self.kwargs.get('pk')
        try:
            user = Person.objects.get(pk=user_id)
        except Person.DoesNotExist:
            raise NotFound("User does not exist")
        return user
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        print(serializer.initial_data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def perform_update(self, serializer):
        serializer.save()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        instance.delete()   