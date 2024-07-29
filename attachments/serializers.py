from rest_framework import serializers
from django.conf import settings

from attachments.models import FileAttachments, AudioAttachments
from attachments.utils.formatter import Formatter


class FileAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAttachments
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        formatter = Formatter()
        data['size'] = formatter.format_byte(instance.size)
        data['rsc'] = f"{settings.CURRENT_URL}{instance.rsc}"
        return data


class AudioAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioAttachments
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['rsc'] = f"{settings.CURRENT_URL}{instance.rsc}"
        return data
