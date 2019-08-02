from django.db import models
from django.contrib import admin

# Create your models here.
class NewsClass(models.Model):
    name = models.CharField('分类名称', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资讯类别'
        verbose_name_plural = '资讯类别'


class News(models.Model):
    # 默认添加
    # id = models.AutoField(primary_key=True)
    title = models.CharField('文章标题', max_length=30)
    content = models.TextField('文章内容')
    date = models.DateTimeField('发布时间')
    show = models.BooleanField('是否显示')
    news_class = models.ForeignKey(
        NewsClass, verbose_name='文章分类', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '资讯'
        verbose_name_plural = '资讯'



class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'news_class', 'date', 'show')

    class Media:
        # 在管理后台的相关HTML文件中加入js文件
        js = (
            '/static/kindeditor/kindeditor-all-min.js',
            '/static/kindeditor/lang/zh-CN.js',
            '/static/kindeditor/config.js',
        )