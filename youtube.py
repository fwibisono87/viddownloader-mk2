from pytube import YouTube
import os
import wget
import shutil
import ffmpeg


vidPath = os.join(os.getcwd(), 'temp', 'video.mp4')
audPath = os.join(os.getcwd(), 'temp', 'audio.mp4')
temPath = os.join(os.getcwd(), 'temp', 'temp.mp4')


def CleanDirectory():
    '''
    Clears temp and downloads folder
    '''
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


def YTParseLink(link):
    '''
    Parses a YouTube Link \n
    :param link: string \n
    :return video: a YouTube object
    '''
    try:
        if type(link) is not str:
            raise TypeError("Link has to be of type str")
    except TypeError:
        print(TypeError)

    video = YouTube(link)

    return video


def YTGetTitle(video):
    try:
        if type(video) is not YouTube:
            raise TypeError("Video has to be of type YouTube")
    except TypeError:
        print(TypeError)

    title = CleanTitle(video.title)

    return title


def YTChooseResolution(video, resolution):
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


def YTGetAudio(video):
    aud = video.streams.filter(progressive=True) \
        .filter(mime_type="audio/mp4").order_by('abr').desc().first()

    return aud


def YTDownload(video):
    try:
        if type(video) is not YouTube:
            raise TypeError("Video has to be of type YouTube")
    except TypeError:
        print(TypeError)


def YTJoin(video):
    title = YTGetTitle(video)
    os.system('ffmpeg -i %s -i %s -c:v copy -c:a aac %s' % (vidPath, audPath, temPath))
    expPath = os.path.join(os.getcwd(), 'videos', '%s.mp4' % title)
    shutil.move(temPath, expPath)

    return expPath


def CleanTitle(title):
    try:
        if type(title) is not str:
            raise TypeError("Title has to be of type str")
    except TypeError:
        print(TypeError)

    cleaned = title.replace("<", "").replace(">", "").replace("/", "").replace(":", "").replace('"', "") \
        .replace("|", "").replace("/", "").replace('?', "").replace("*", "")

    return cleaned


