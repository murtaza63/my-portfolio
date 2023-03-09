from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .serializers import (
    UserSerializer,
    EductionSerializer,
    WorkSerializer,
    PorfolioSerializer,
)
from .models import Education, Work, Portfolio


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EductionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class WorkVewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PorfolioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
