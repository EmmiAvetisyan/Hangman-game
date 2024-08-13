from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Event, Category
from .serializers import EventSerializer, UserSerializer, RegisterSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken .for_user(user)
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "refresh" : str(refresh),
            "access" : str(refresh.access_token),
        })

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer