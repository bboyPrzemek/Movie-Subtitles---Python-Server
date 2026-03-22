import SubtitlesClient
import SubtitlesCleaner

def get_unique_words_from_subtitles(movieId):

    data = SubtitlesClient.get_subtitles(movieId)
    
    fileId = data['data'][0]['attributes']['files'][0]['file_id'] # Get the file ID of the first subtitle file
    subtitleURL = SubtitlesClient.get_subtitle_file(fileId)["link"]

    subtitlesFromURl = SubtitlesClient.get_subtitle_file_from_url(subtitleURL)

    unique_words = SubtitlesCleaner.get_unique_words_from_subtitles(subtitlesFromURl)
    return unique_words






    

    


