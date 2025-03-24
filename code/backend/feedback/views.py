from rest_framework import generics
from rest_framework.response import Response

from feedback.models import Feedback
from feedback.serializer import FeedbackSerializer, FeedbackListSerializer
from people.models import User


# from feedback.models import FeedBackAftersaleman2User, FeedBackAssetman2Aftersaleman
# from feedback.serializer import FeedbackStep1Serializer, FeedbackStep2Serializer
# from people.models import User
#
#
# class FeedbackStep1ListCreate(generics.ListCreateAPIView):
#     queryset = FeedBackAftersaleman2User.objects.all()
#     serializer_class = FeedbackStep1Serializer
#
#
# class FeedbackStep1RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = FeedBackAftersaleman2User.objects.all()
#     serializer_class = FeedbackStep1Serializer
#
#     def get(self, request, *args, **kwargs):
#         user_id = kwargs['pk']
#         user = User.objects.get(id=user_id)
#         feedback1 = FeedBackAftersaleman2User.objects.filter(user=user)
#         return Response(self.get_serializer(feedback1, many=True).data)
#
#
# class FeedbackStep2ListCreate(generics.ListCreateAPIView):
#     queryset = FeedBackAssetman2Aftersaleman.objects.all()
#     serializer_class = FeedbackStep2Serializer
class FeedbackListCreate(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get(self, request, *args, **kwargs):
        return Response(FeedbackListSerializer(self.get_queryset().all(), many=True).data)


class FeedbackRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = User.objects.get(id=user_id)
        feedback = Feedback.objects.filter(user=user)
        return Response(self.get_serializer(feedback, many=True).data)


class FeedbackListPending(generics.ListCreateAPIView):
    queryset = Feedback.objects.filter(que_condition=0)
    serializer_class = FeedbackListSerializer


class FeedbackListPendingFromAsset(generics.ListCreateAPIView):
    queryset = Feedback.objects.filter(que_condition=2)
    serializer_class = FeedbackListSerializer


class FeedbackListFromAftersale(generics.ListCreateAPIView):
    queryset = Feedback.objects.filter(que_condition__in=[1,2])
    serializer_class = FeedbackListSerializer


class FeedbackListPendingFromAftersale(generics.ListCreateAPIView):
    queryset = Feedback.objects.filter(que_condition=1)
    serializer_class = FeedbackListSerializer
