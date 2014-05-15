from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	def pre_save(self, obj):
		obj.owner = self.request.user
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
						  IsOwnerOrReadOnly,)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	def pre_save(self, obj):
		obj.owner = self.request.user
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
						  IsOwnerOrReadOnly,)
	
class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer