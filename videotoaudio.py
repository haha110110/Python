from moviepy.editor import VideoFileClip

video_file = "D:\戴公连精彩视频.mp4"

video_clip = VideoFileClip(video_file)
audio_clip = video_clip.audio

audio_file = "D:\戴公连精彩视频.mp3"
audio_clip.write_audiofile(audio_file, codec="libmp3lame")


