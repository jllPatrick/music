#from django.http import Http404
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render,get_object_or_404
from .models import Album,Song

'''
def index(request):
    return HttpResponse('<h1>This is the Music app homepage</h1>')
'''    
def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    
    #contaxt:the information template need
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html',context)
    '''
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) #+ '/'
        html += '<a href = "' + url + '">' + album.album_title +  '</a><br>'
        
    return HttpResponse(html)
    '''
    #return HttpResponse(template.render(context,request))
    
def detail(request, album_id):
    #return HttpResponse('<h2>Details for Albumid:' + str(album_id) + '</h2>')
    '''
    try:
        album = Album.objects.get(pk = album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exsit")
    '''
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html',{'album': album})    
    
def favourite(request, album_id):
     album = get_object_or_404(Album, pk=album_id)
     try:
         selected_song = album.song_set.get(pk = request.POST['song'])
     except (keyError, Song.DoesNotExist):
         return render(request, 'music/detail.html',{
             'album':album,
             'error_message': 'No song selected',
         })
     else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html',{'album': album}) 