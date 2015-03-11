from django.shortcuts import render_to_response
from django.template import RequestContext


import datetime
from django.contrib.auth.models import Group, User
from django.http import HttpResponse, HttpResponseRedirect


def empresa(request):

 
  from ticket.models import *
  empresa = Empresa.objects.all().order_by('-id')
  from blogapp.models import *
  empresa_ticket = Empresa.objects.all().order_by('-id')

  if request.method == 'POST':

    name = request.POST['name']
    Empresa(name=name).save()
    return HttpResponseRedirect("/empresa")
  


  return render_to_response('home.html', {'empresa_ticket':empresa_ticket,'empresa':empresa},
                              context_instance=RequestContext(request))

def equipo(request,id):


  empresa = Empresa.objects.get(id=id)
  equipo = Equipos.objects.filter(empresa=id).order_by('-id')

  if request.method == 'POST':



    name = request.POST['name']
    print name
    Equipos(empresa=id,name=name).save()
    return HttpResponseRedirect("/equipo/"+str(id))


  return render_to_response('equipo.html', {'equipo':equipo,'empresa':empresa},
                              context_instance=RequestContext(request))

def parametro(request,id,ide):

  empresa= Empresa.objects.get(id=ide)
  equipo = Equipos.objects.get(id=id)
  parametro = Parametro.objects.filter(equipo=id).order_by('-id')


  if request.method == 'POST':



    ip = request.POST['ip']
  
    Parametro(equipo=id,ip=ip).save()
    return HttpResponseRedirect("/parametro/"+str(id)+"/"+str(ide))


  return render_to_response('parametro.html', {'empresa':empresa,'equipo':equipo,'parametro':parametro},
                              context_instance=RequestContext(request))


def servicio(request,idp,ide,idem):

  empresa= Empresa.objects.get(id=idem)
  equipo = Equipos.objects.get(id=ide)
  parametro = Parametro.objects.get(id=idp)
  servicio = Servicio.objects.filter(id=idp).order_by('-id')


  if request.method == 'POST':



    servicio = request.POST['servicio']
  
    Servicio(servicio=servicio).save()
    return HttpResponseRedirect("/servicio/"+str(idp)+"/"+str(ide)+"/"+str(idem))


  return render_to_response('servicio.html', {'servicio':servicio,'empresa':empresa,'equipo':equipo,'parametro':parametro},
                              context_instance=RequestContext(request))




'''

def index(request):
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       content = request.POST['content']

       post = Post(title=title)
       post.last_update = datetime.datetime.now() 
       post.content = content
       post.save()

    # Get all posts from DB
    posts = Post.objects 
    return render_to_response('index.html', {'Posts': posts},
                              context_instance=RequestContext(request))


def update(request):
    id = eval("request." + request.method + "['id']")
    post = Post.objects(id=id)[0]
    
    if request.method == 'POST':
        # update field values and save to mongo
        post.title = request.POST['title']
        post.last_update = datetime.datetime.now() 
        post.content = request.POST['content']
        post.save()
        template = 'index.html'
        params = {'Posts': Post.objects} 

    elif request.method == 'GET':
        template = 'update.html'
        params = {'post':post}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              

def delete(request):
    id = eval("request." + request.method + "['id']")

    if request.method == 'POST':
        post = Post.objects(id=id)[0]
        post.delete() 
        template = 'index.html'
        params = {'Posts': Post.objects} 
    elif request.method == 'GET':
        template = 'delete.html'
        params = { 'id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))
                              
    
'''