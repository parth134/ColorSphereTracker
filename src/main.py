from video_processing import process_video

def main():
    input_video_path = 'D:/cv_task/data/input_video.mp4'
    output_video_path = 'D:/cv_task/output/processed_video.avi'
    log_file_path = 'D:/cv_task/output/event_log.txt'
    
    process_video(input_video_path, output_video_path, log_file_path)

if __name__ == "__main__":
    main()
