from rest_framework import serializers

from feedback.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackListSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    user_name = serializers.CharField(source='user.first_name')
    aftersaleman_id = serializers.IntegerField(source='aftersaleman.id', allow_null=True)
    aftersaleman_name = serializers.CharField(source='aftersaleman.name', allow_null=True)
    assetman_id = serializers.IntegerField(source='assetman.id', allow_null=True)
    assetman_name = serializers.CharField(source='assetman.name', allow_null=True)

    class Meta:
        model = Feedback
        fields = ['id', 'user_id', 'user_name', 'aftersaleman_id', 'aftersaleman_name', 'assetman_id', 'assetman_name',
                  'que_condition', 'que_content_user2aftersaleman', 'que_content_aftersaleman2user',
                  'que_content_assetman2aftersaleman',
                  'que_content_aftersaleman2assetman']
