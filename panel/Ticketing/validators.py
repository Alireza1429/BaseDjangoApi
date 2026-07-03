from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers

from panel.Ticketing.models import Attachment


def validate_attachment_extension(file):
    try:
        Attachment._meta.get_field("file").run_validators(file)
    except DjangoValidationError as exc:
        raise serializers.ValidationError(exc.messages) from exc
