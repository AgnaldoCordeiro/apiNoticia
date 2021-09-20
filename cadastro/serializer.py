from django.db import models
from django.db.models import fields
from rest_framework import serializers
from cadastro.models import NoticiaTb


#é o que vai converter em json 


class NoticiaTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticiaTb
        fields = ['title', 'subtitulo', 'url', 'data', 'image_url']
        