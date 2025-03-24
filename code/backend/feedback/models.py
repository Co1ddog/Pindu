from django.db import models


# Create your models here.
class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('people.User', on_delete=models.CASCADE)
    aftersaleman = models.ForeignKey('people.Admin', on_delete=models.CASCADE, related_name="aftersaleman", blank=True,
                                     null=True)
    assetman = models.ForeignKey('people.Admin', on_delete=models.CASCADE, related_name="assetman", blank=True,
                                 null=True)

    # 0:未处理,1:售后反馈资金,2:资金反馈售后,3:售后反馈用户
    que_condition = models.IntegerField(default=0)

    # A给B的问题内容
    que_content_user2aftersaleman = models.CharField(max_length=300, blank=True)
    que_content_aftersaleman2user = models.CharField(max_length=300, blank=True)
    que_content_assetman2aftersaleman = models.CharField(max_length=300, blank=True)
    que_content_aftersaleman2assetman = models.CharField(max_length=300, blank=True)

# class FeedBackAftersaleman2User(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey('people.User', on_delete=models.CASCADE)
#     aftersaleman = models.ForeignKey('people.Admin', on_delete=models.CASCADE, null=True)
#
#     # 0:未处理,1:售后反馈资金,2:资金反馈售后,3:售后反馈用户
#     que_condition = models.IntegerField(default=0)
#
#     # A给B的问题内容
#     que_content_user2aftersaleman = models.CharField(max_length=300, blank=True)
#     que_content_aftersaleman2user = models.CharField(max_length=300, blank=True)
#     que_content_aftersaleman2assetman = models.CharField(max_length=300, blank=True)
#
#
# class FeedBackAssetman2Aftersaleman(models.Model):
#     id = models.AutoField(primary_key=True)
#     assetman = models.ForeignKey('people.Admin', on_delete=models.CASCADE, null=True)
#     feedback_aftersaleman2user = models.ForeignKey('FeedBackAftersaleman2User', on_delete=models.CASCADE)
#
#     # A给B的问题内容
#     que_content_assetman2aftersaleman = models.CharField(max_length=300, blank=True)
