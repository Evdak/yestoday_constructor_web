from django.db import models
from django.core.files.base import ContentFile
from yestoday_constructor_web.settings import ALLOWED_HOSTS
import requests


class Audio(models.Model):
    text_up = models.CharField(
        'Текст сверху', max_length=255, blank=True, null=True)
    text_down = models.CharField(
        'Текст сверху', max_length=255, blank=True, null=True)
    seekbar = models.BooleanField('Доавить шкалу времени', default=False)
    src = models.CharField('Ссылка на источник',
                           max_length=255, blank=True, null=True)
    file = models.FileField('Файл', upload_to='audio', blank=True, null=True)

    class Meta:
        verbose_name = "Аудио"
        verbose_name_plural = "Аудио"

    def __str__(self) -> str:
        return f"{self.text_up}, {self.text_down}"[:50] + '...'

    def save(self, *args, **kwargs) -> None:
        if 'api.voicerss.org' in self.src:
            r = requests.get(self.src)
            new_id = Audio.objects.latest('id').id + 1
            self.file = ContentFile(r.content, f"{new_id}.mp3")
        return super().save(*args, **kwargs)

    def to_html(self) -> str:

        if self.seekbar:
            seekbar = """
        <div>
                    <progress class="podcast-progress" id='podcast-progress' value="0" max="1"
                        onclick="audioTimeLineClick(this, event)"></progress>
                    <div class="f-container" id='f-container'>
                        <div class="podcast-time" id='podcast-time'>00:00 / 00:00</div>
                        <div class="podcast-speed" id='podcast-speed'>
                            <a class="podcast-speed-10 active" href="javascript:void(0)"
                                onclick="audioChangeSpeedClick(this)">1x</a> / <a class="podcast-speed-15"
                                href="javascript:void(0)" onclick="audioChangeSpeedClick(this)">1.5x</a> / <a
                                class="podcast-speed-20" href="javascript:void(0)"
                                onclick="audioChangeSpeedClick(this)">2x</a>
                        </div>
                    </div>
                </div>
        """
        else:
            seekbar = ""

        return f"""
        <div class='audio-tts{self.id} audio-div' id='audio-tts'>
                <audio class="audio-player{self.id}" id='audio-player' src="{'https://'+ ALLOWED_HOSTS[0] + self.file.url if 'api.voicerss.org' in self.src else self.src}"
                    onended="audioOnEnded(this)" oncanplay="audioOnCanPlay(this)" onplay="audioPlay(this)"
                    onpause="audioPause(this)"></audio>
                <div class="podcast-container" id='podcast-container'>
                    <div class="h-container" id='h-container'>
                        <div class="podcast-playpause" id='podcast-playpause'>
                            <img class="play" id="play"
                                src="https://fs.getcourse.ru/fileservice/file/download/a/44237/sc/337/h/cb28b80bb66ad56d3c12fd1885bc3ef8.svg"
                                onclick="playPauseClick(this)">
                            <img class="pause" id="pause"
                                src="https://fs.getcourse.ru/fileservice/file/download/a/44237/sc/197/h/7395c5433ab34099a1d5b9b139efdd5b.svg"
                                onclick="playPauseClick(this)">
                        </div>
                        <div>
                            <div class="podcast-title" id='podcast-title'>{self.text_up}
                            <button type="button" onclick="audioSaveBtnClick(this)" id="{self.id}"><i
                                    class="bi bi-bookmark-star-fill active"></i></button></div>
                            <div class="podcast-subtitle" id='podcast-subtitle'>{self.text_down}</div>
                        </div>
                    </div>

                </div>
                {seekbar}

            </div>
            """


class GetCourseUser(models.Model):
    accountUserId = models.BigIntegerField('ID с GetCourse')
    audios = models.ManyToManyField(
        Audio,
        verbose_name='Аудио'
    )

    class Meta:
        verbose_name = "Пользователь GetCourse"
        verbose_name_plural = "Пользователи GetCourse"

    def get_audios(self):
        return "\n".join([str(p) for p in self.audios.all()])
