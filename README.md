---

# Video Part Generator

This project is a Python script that splits a video into multiple clips and adds custom information, such as a title and part number, to each clip. It's perfect for creating clips for social media platforms like TikTok.

## Features

- **Video Splitting**: Divides a video into multiple clips with random durations (default between 61 and 77 seconds).
- **Text Overlay**: Adds a title and part number (e.g., "Part 1", "Part 2") to each video clip.
- **Automatic Organization**: Saves each clip in a folder named after the video's title for easy organization.
- **Hashtag Conversion**: Converts the video title into hashtags, making it easier to share on social media.

## Prerequisites

- Python 3.x
- [MoviePy](https://zulko.github.io/moviepy/): to install, run the following command:

  ```bash
  pip install moviepy
  ```

## Usage

1. **Set Paths**:
   - Change `input_video` in the code to point to your input video file.
   - Change `output_directory` to specify the output folder where the clips will be saved.

2. **Run the Script**:
   - Execute the script in a terminal or IDE.
   - Enter the title of your video when prompted. This title will be added to each clip and converted into hashtags.

3. **Output Files**:
   - Clips will be saved in a folder named after the video title.
   - Each video file will include the title, part number, and the hashtag `#flosvd` in its name, e.g., `FilmTitle Part1 #flosvd.mp4`.

## Example Command

```python
input_video = "/path/to/video.mp4"
output_directory = "/path/to/output_folder/"
create_video_parts(input_video, output_directory)
```

## Customization

You can adjust certain parameters directly in the code:

- `min_duration` and `max_duration`: Minimum and maximum duration of clips.
- `text_size` and `text_color`: Font size and color of the text displayed on the video.

## Notes

- Ensure the output folder exists or that you have permissions to create folders in the specified output path.
- The script uses the `libx264` codec and a frame rate of 30 FPS for the generated videos.

---

With this script, you can easily prepare video clips for social media, adding titles and organized information to each.