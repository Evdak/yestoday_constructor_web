import os
from django.http import FileResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .settings import MEDIA_ROOT


@csrf_exempt
def get_audio_file(request: HttpRequest, auidoname: str):
    print(f"{auidoname=}")
    response = FileResponse(
        open(os.path.join(MEDIA_ROOT, "audio/", auidoname), "rb"))
    return response
