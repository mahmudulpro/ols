from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from api.models import Question
from api.serializers import QuestionSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class QuestionList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/index.html'

    def get(self, request):
        queryset = Question.objects.all()
        return Response({'questions': queryset})
