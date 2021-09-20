from django.db import models
from django.db.models.fields import AutoField
from http.server import BaseHTTPRequestHandler
from cowpy import cow
#aqui eu cadastro as tabelas que quero criar no banco de dados
#oui seja tabela cliente e os dados que vao conter nela

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
        self.wfile.write(message.encode())
        return

class NoticiaTb(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.TextField(blank=True, null=True)
    subtitulo = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'noticia_tb'

    

