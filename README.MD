# Ball Tracking Project

## Description
This project tracks the movement of balls of different colors across various quadrants in a video. It logs the events of each ball entering and exiting each numbered quadrant.

## Setup

### Prerequisites
Ensure you have Python installed on your system. The project requires Python 3.6 or higher.

### Installation
1. Clone the repository:
    sh
    git clone https://github.com/yourusername/ColorSphere_Tracker.git
    cd ColorSphere_Tracker
    

2. Install the dependencies:
    sh
    pip install -r requirements.txt
    

3. Place your input video in the data directory.

## Running the Project
To process the video and generate the output:

1. Navigate to the project directory:
    sh
    cd cv_task
    

2. Run the main script:
    sh
    python src/main.py
    

## Output
- The processed video will be saved in the output directory as processed_video.avi.
- The event log will be saved in the output directory as event_log.txt.

## Explanation of Code

### Main Script (src/main.py)
- Entry point of the application.
- Calls the process_video function with paths to the input video, output video, and log file.

### Video Processing (src/video_processing.py)
- Handles reading the input video, processing each frame to track balls, and saving the output.
- Uses tqdm for displaying the progress of video processing.
- Ensures output directories exist before writing files.

### Ball Tracking (src/ball_tracking.py)
- Contains the logic for tracking balls of different colors.
- Defines HSV ranges for red, blue, yellow, and white.
- Creates masks based on the HSV color ranges.
- Uses morphological operations to clean up the masks.
- Detects contours of the masked areas to identify balls.
- Identifies which quadrant the ball is in.
- Logs the events of balls entering/exiting quadrants.

### Unit Testing (tests/test_ball_tracking.py)
- Validates the quadrant determination function using simple unit tests.

