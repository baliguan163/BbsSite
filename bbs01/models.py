from django.db import models

from django.contrib.auth.models import  User

# Create your models here.

# 唯一标识符id（默认自增）
# 主题title
# 概述summary
# 板块category
# 内容content
# 浏览数view
# 评论数comment
# 作者author
# 置顶排名ranking（1000以前为置顶）
# 创建日期publish_date
# 修改日期modify_date
class bbs(models.Model):
    # 唯一标识符id（默认自增）
    # 主题title
    title=models.CharField(max_length=128)
    #概述summary
    summary=models.CharField(max_length=256,blank=True,null=True)
    # 内容content
    content = models.TextField()
    # 板块content
    category=models.ForeignKey('category')
    # 浏览数view_count
    view_count = models.IntegerField(default=1)
    # 评论数comment
    comment_count = models.IntegerField(default=0)
    # 作者
    author=models.ForeignKey('bbs_user')
    # 置顶排名ranking（1000以前为置顶）
    ranking=models.IntegerField()
    # 创建日期publish_date
    publish_date=models.DateTimeField()
    # 修改日期modify_date
    modify_date=models.DateTimeField()

    def __unicode__(self):
        return self.title


# # 评论id（默认自增）
# # 评论内容content
# # 用户IDuesr_id
# # 评论的帖子bbs_id
# # 评论日期date
class comment(models.Model):
    # 评论内容content
    content=models.CharField(max_length=128)
    # 用户ID uesr_id
    uesr_id=models.ForeignKey('bbs_user')
    # 评论的帖子bbs_id
    bbs_id=models.ForeignKey('bbs')

    def __unicode__(self):
        return self.content

class category(models.Model):
    name = models.CharField(max_length=64,unique=True)
    admin = models.ForeignKey('bbs_user')

    def __unicode__(self):
        return self.name

class bbs_user(models.Model):
    #继承自带的用户表
    #user = models.OneToOneField(User)
    user_name = models.CharField(max_length=64)
    user_nice = models.CharField(max_length=64,default='')
    user_passwd = models.CharField(max_length=16)
    user_signature = models.CharField(max_length=128,default='用户很懒,什么也没留下')
    user_photo = models.ImageField(upload_to='upload_imgs/', default='upload_imgs/user_default.jpg')

    def __unicode__(self):
        return self.user_name
