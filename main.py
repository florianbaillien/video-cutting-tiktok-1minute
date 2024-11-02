from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
import random

def titre_vers_hashtags(titre):
    mots = titre.split()
    hashtags = ['#' + mot for mot in mots]
    hashtags_str = ' '.join(hashtags)
    return hashtags_str

def create_video_parts(input_video, output_directory, min_duration=61.0, max_duration=77.0, text_size=125, text_color='white'):
    video = VideoFileClip(input_video)
    film_title = input("Entrez le titre : ")
    output_directory = os.path.join(output_directory, film_title)
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    start_time = 0
    clip_number = 1
    while start_time < video.duration:
        duration = random.uniform(min_duration, max_duration)
        end_time = min(start_time + duration, video.duration)
        clip = video.subclip(start_time, end_time)
        
        
        # Overlay the original video with its extended version
        final_clip = CompositeVideoClip([clip.set_position(('center', 'center')), clip.set_position(('center', 'center'))])
        
        # Add title and part number texts
        title_clip = TextClip(film_title, fontsize=text_size, color=text_color, font='Arial-Bold').set_position(('center', 'top')).set_duration(final_clip.duration)
        part_clip = TextClip(f"Part {clip_number}", fontsize= (text_size - 20), color=text_color, font='Arial-Bold').set_position(('center', 'bottom')).set_duration(final_clip.duration)
        
        # Composite title and part number texts on final clip
        final_clip = CompositeVideoClip([final_clip, title_clip.set_position(('center', video.size[1] - 1750)), part_clip.set_position(('center', video.size[1] -350))])
        
        # Convert film title to hashtags
        #hashtags = titre_vers_hashtags(film_title)
        filename = f"{film_title} Part{clip_number}.mp4"
        
        # Write the final clip to file
        final_clip.write_videofile(os.path.join(output_directory, filename), codec='libx264', fps=30)
        
        start_time = end_time
        clip_number += 1
    
    video.close()

# Usage
input_video = "{path of your input video}"
output_directory = "{path of the output video}"
create_video_parts(input_video, output_directory)
