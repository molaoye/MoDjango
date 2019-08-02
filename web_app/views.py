from django.shortcuts import render, HttpResponse
from web_app.models import *
from web_app.serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse('你好')

# http://127.0.0.1:8000/news/?id=1
def news_content(request):
    id_num = request.GET.get('id')
    context = {}
    try:
        context['News'] = News.objects.get(id=id_num)
        context['title'] = context['News'].title
    except News.DoesNotExist:
        context['News'] = '404'
        context['title'] = '404'
        return render(request, 'web_app/article.html', context)
    return render(request, 'web_app/article.html', context)


# http://127.0.0.1:8000/get_news/?id=1
class GetNews(APIView):
    def get(self, request):
        # 获取url参数
        id_num = request.GET.get('id')
        serializer = NewsSerializer(News.objects.all(), many=True)
        # 返回信息
        msg = {
            'success': True,
            'data': serializer.data
        }
        # 防止中文乱码
        return JsonResponse(msg, json_dumps_params={'ensure_ascii': False})