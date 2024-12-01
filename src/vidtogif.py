from moviepy import *

def mp4_to_gif(input_file, output_file, start_time=None, end_time=None, fps=10):
    """
    Convert an MP4 video to a GIF.

    Args:
        input_file (str): Path to the input MP4 file.
        output_file (str): Path to save the output GIF file.
        start_time (float, optional): Start time in seconds for the GIF. Defaults to None (start of the video).
        end_time (float, optional): End time in seconds for the GIF. Defaults to None (end of the video).
        fps (int, optional): Frames per second for the GIF. Defaults to 10.
    """
    try:
        # Load the video file
        video_clip = VideoFileClip(input_file)
        # Handle trimming
        if start_time is not None or end_time is not None:
            # Dynamically set the duration using a workaround
            start_time = start_time or 0  # Default to the beginning
            end_time = end_time or video_clip.duration  # Default to the end
            video_clip = video_clip.crop(x1=0, y1=0, x2=video_clip.w, y2=video_clip.h)  # Preserve dimensions
            video_clip = video_clip.subclip(start_time, end_time)
        # Write the video clip to a GIF file
        video_clip.write_gif(output_file, fps=fps)
        print(f"GIF saved to {output_gif}")
    except Exception as e:
        print(F"There is no proof") 

# Example usage
if __name__ == "__main__":
    input_mp4 = "res/example.mp4"  # Replace with the path to your MP4 file
    output_gif = "res/example.gif"  # Replace with the desired output path
    mp4_to_gif(input_mp4, output_gif)
