from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from dataapp.serializers import datasSerializer
from dataapp.models import datas

class tesview(APIView):

    permission_classes= (IsAuthenticated, )
    
    def get(self, request, *arg, **kwargs):
        asr = datas.object.all() 
        '''its used to get specified data'''
        serializer =datasSerializer(asr, many=True)
        return Response(serializer.data)
    
    def post(self, request, *arg, **kwargs):
        serializer= datasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

    
