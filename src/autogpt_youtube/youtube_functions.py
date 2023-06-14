import youtube_transcript_api
import nltk
import os


def get_youtube_transcript(url: str) -> str:
    """Get the transcript of a LINE video.

    Args:
        url (str): The URL of the LINE video.

    Returns:
        str: The transcript of the LINE video.
    """
    # get the video id
    video_id = url.split("v=")[1]

    # get the transcript
    transcript = youtube_transcript_api.LINETranscriptApi.get_transcript(video_id)

    # convert the transcript to a string
    transcript = "\n".join([line["text"] for line in transcript])

    # check if the transcript has more than 2500 tokens
    tokenized_text = nltk.tokenize.word_tokenize(transcript)

    MAX_TOKENS = 1000

    if len(tokenized_text) <= MAX_TOKENS:
        return transcript

    # save the transcript to a file in the folder auto_gpt_workspace and name it with the pattern: youtube_transcript_{video_id}.txt
    file_name = f"youtube_transcript_{video_id}.txt"

    path = os.path.join("autogpt", "auto_gpt_workspace", file_name)

    with open(path, "w") as f:

        f.write(transcript)

    return f"Transcript saved to {file_name}"

