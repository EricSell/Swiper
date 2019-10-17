from django.db import models


class User(models.Model):
    """
    用户表：
        手机号
        昵称
        出生年
        出生月
        出生日
        个人形象
        常居地
    """
    SEX = (
        ('male', '男'),
        ('female', '女')
    )
    phonenum = models.CharField(verbose_name='手机号', max_length=20, unique=True)
    nickname = models.CharField(verbose_name='昵称', max_length=256)
    sex = models.CharField(verbose_name='性别', choices=SEX, max_length=10)
    birth_year = models.IntegerField(verbose_name='出生年', default=2000)
    birth_month = models.IntegerField(verbose_name='出生月', default=1)
    birth_day = models.IntegerField(verbose_name='出生日', default=1)
    avatar = models.CharField(verbose_name='个人形象', max_length=256)
    location = models.CharField(verbose_name='常居地', max_length=128)

    def __str__(self):
        return f'<User {self.nickname, self.id}>'

    class Meta:
        db_table = 'users'


class Profile(models.Model):
    '''个人交友资料'''

    SEX = (
        ('male', '男'),
        ('female', '女')
    )

    location = models.CharField(verbose_name='目标城市', max_length=128)
    min_distance = models.CharField(verbose_name='最小查找范围', default=0)
    max_distance = models.CharField(verbose_name='最大查找范围', default=50)
    min_dating_age = models.IntegerField(verbose_name='最小交友年龄', default=18)
    max_dating_age = models.IntegerField(verbose_name='最大交友年龄', default=50)
    dating_sex = models.CharField(verbose_name='匹配的性别', choices=SEX, max_length=10, default='male')
    vibration = models.BooleanField(verbose_name='开启震动')
    only_matche = models.BooleanField(verbose_name='不让为匹配的人看我的相册')
    auto_play = models.BooleanField(verbose_name='自动播放视频')

    class Meta:
        db_table = 'profile'
