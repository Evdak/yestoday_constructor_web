from .models import Audio, GetCourseUser


def add_audio_to_getcourse_user_dict(user_id: int, audio_id: int):
    audio = _get_audio(audio_id)
    if audio:
        _get_getcourse_user(user_id).audios.add(audio)
        return True
    return False


def delete_audio_from_getcourse_user_dict(user_id: int, audio_id: int):
    audio = _get_audio(audio_id)
    if audio:
        _get_getcourse_user(user_id).audios.remove(audio)
        return True
    return False


def get_audio_ids_from_getcourse_user_dict(user_id: int):
    return [el.id for el in _get_getcourse_user(user_id).audios.all()]


def show_getcourse_user_dict(user_id: int):
    return "\n".join([el.to_html() for el in _get_getcourse_user(user_id).audios.all()])


def _get_getcourse_user(user_id: int):
    user: GetCourseUser
    user, created = GetCourseUser.objects.get_or_create(accountUserId=user_id)
    return user


def _get_audio(audio_id: int):
    return Audio.objects.get(pk=audio_id)
