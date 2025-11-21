from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Feedback
from .serializers import StaffFeedbackSerializer
from common.utils.mixins import FieldFilterOverviewMixin

class StaffFeedbackViewSet(FieldFilterOverviewMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = StaffFeedbackSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['subject', 'text', 'user__username', 'user__email']
    ordering_fields = ['created_at']
    lookup_field = 'id'
    http_method_names = ['get', 'delete', 'head', 'options']

    def get_queryset(self):
        return Feedback.objects.all().select_related('user')