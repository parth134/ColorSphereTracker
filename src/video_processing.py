import cv2
import os
from ball_tracking import track_balls, log_event
import time
from tqdm import tqdm

def process_video(input_video_path, output_video_path, log_file_path):
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_video_path), exist_ok=True)
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    cap = cv2.VideoCapture(input_video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (frame_width, frame_height))
    
    start_time = time.time()
    log = []

    with tqdm(total=total_frames, desc="Processing video") as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            current_time = time.time() - start_time
            frame, events = track_balls(frame, current_time)

            for event in events:
                log_event(log, event['time'], event['quadrant'], event['color'], event['event_type'])

            out.write(frame)
            pbar.update(1)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    with open(log_file_path, 'w') as f:
        for entry in log:
            f.write(entry + '\n')
