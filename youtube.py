from pytube import YouTube
import os
import shutil

vidPath = os.path.join(os.getcwd(), 'temp', 'video.mp4')
audPath = os.path.join(os.getcwd(), 'temp', 'audio.mp4')
temPath = os.path.join(os.getcwd(), 'temp', 'temp.mp4')


def clean_directory():
    """
    Clears temp and downloads folder
    """
    if not os.exist(os.join(os.getcwd(), 'temp')):
        os.mkdir(os.join(os.getcwd(), 'temp'))
    else:
        os.rmtree(os.join(os.getcwd(), 'temp'))
        os.mkdir(os.join(os.getcwd(), 'temp'))
    if not os.exist(os.join(os.getcwd(), 'downloads')):
        os.mkdir(os.join(os.getcwd(), 'downloads'))
    else:
        os.rmtree(os.join(os.getcwd(), 'downloads'))
        os.mkdir(os.join(os.getcwd(), 'downloads'))


def youtube_parse_link(link):
    """
    Parses a YouTube Link \n
    :param link: string \n
    :return video: a YouTube object
    """
    try:
        if type(link) is not str:
            raise TypeError("Link has to be of type str")
    except TypeError:
        print(TypeError)

    video = YouTube(link)

    return video


def youtube_get_title(video):
    """
    Returns title from a YouTube object
    :param video: YouTube \n
    :return title: String
    """
    try:
        if type(video) is not YouTube:
            raise TypeError("Video has to be of type YouTube")
    except TypeError:
        print(TypeError)

    title = clean_title(video.title)

    return title


def youtube_choose_resolution(video, resolution):
    """
    Finds Youtube stream from a list of streams
    :param video:
    :param resolution:
    :return vid:
    """
    try:
        if resolution == "1080p":
            vid = video.streams.filter(resolution="1080p").filter(progressive=True) \
                .filter(mime_type="video/mp4").first()
        elif resolution == "720p":
            vid = video.streams.filter(resolution="720p").filter(progressive=True) \
                .filter(mime_type="video/mp4").first()
        elif resolution == "360p":
            vid = video.streams.filter(resolution="360p").filter(progressive=True) \
                .filter(mime_type="video/mp4").first()
        elif resolution == "240p":
            vid = video.streams.filter(resolution="240p").filter(progressive=True) \
                .filter(mime_type="video/mp4").first()
        elif resolution == "144p":
            vid = video.streams.filter(resolution="144p").filter(progressive=True) \
                .filter(mime_type="video/mp4").first()
        if vid.isnull():
            raise ValueError("Stream resolution not found, try lowering resolution!")

    except ValueError:
        print(ValueError)

    return vid


def youtube_get_audio(video):
    """
    Retrieves audio stream from YouTube object
    :param video: YouTube
    :return: aud
    """
    aud = video.streams.filter(progressive=True) \
        .filter(mime_type="audio/mp4").order_by('abr').desc().first()

    return aud


def youtube_download(video, audio):
    """
    Downloads a video and audio stream to local disk
    :param video: Video Stream
    :param audio: Audio Stream
    """
    try:
        if type(video) is not YouTube:
            raise TypeError("Video has to be of type YouTube")
        video.download(vidPath)
        audio.download(audPath)
    except TypeError:
        print(TypeError)


def youtube_join(video):
    """
    Mixes audio and video streams, and renames it to the title, and returns exporting path
    :param video:
    :return: expPath
    """
    original_title = youtube_get_title(video)
    title = clean_title(original_title)
    os.system('ffmpeg -i %s -i %s -c:v copy -c:a aac %s' % (vidPath, audPath, temPath))
    expPath = os.path.join(os.getcwd(), 'videos', '%s.mp4' % title)
    shutil.move(temPath, expPath)

    return expPath


def clean_title(title):
    """
    Checks and removes forbidden characters from a title
    :param title:
    :return:
    """
    try:
        if type(title) is not str:
            raise TypeError("Title has to be of type str")
    except TypeError:
        print(TypeError)

    cleaned = title.replace("<", "").replace(">", "").replace("/", "").replace(":", "").replace('"', "") \
        .replace("|", "").replace("/", "").replace('?', "").replace("*", "")

    return cleaned
