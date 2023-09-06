from django.shortcuts import render, redirect
from .forms import AudioFileForm

# def index(request):
#     return render(request,"index.html")

def upload_audio(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            audio_file = form.save(commit=False)
            audio_file.title = str(request.FILES['audio'])
            # print(audio_file)
            audio_file.save()
            audio_file.audio_url = audio_file.audio.url
            audio_file.save()
            # return redirect('index')  # Redirect to a success page
    else:
        form = AudioFileForm()

    return render(request, 'index.html', {'form': form})
