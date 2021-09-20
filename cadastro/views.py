# aqui vai renderizar a API

from rest_framework import viewsets
from cadastro.models import NoticiaTb
from cadastro.serializer import NoticiaTbSerializer


class NoticiaTbViewSet(viewsets.ModelViewSet):
    queryset = NoticiaTb.objects.all()
    serializer_class = NoticiaTbSerializer