from file_load import file_path
# from spleeter.audio.adapter import get_default_audio_adapter
from spleeter.separator import Separator

def separate2file(music_path, music_name):
    separator = Separator('spleeter:2stems')
    for path in music_path:
        separator.separate_to_file(path, './separated', synchronous=False)

if __name__ == "__main__":
    file_list, file_name, folder_list, folder_name = file_path('./SpotifyMP3_select', '.mp3')
    separate2file(file_list, file_name)