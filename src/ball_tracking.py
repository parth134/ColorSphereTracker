import cv2
import numpy as np

def track_balls(frame, current_time):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    events = []

    # Define color ranges and masks
    color_ranges = {
        'Red': ([0, 120, 70], [10, 255, 255]),
        'Blue': ([110, 150, 50], [130, 255, 255]),
        'Yellow': ([20, 100, 100], [30, 255, 255]),
        'White': ([0, 0, 168], [172, 111, 255])
    }

    for color_name, (lower, upper) in color_ranges.items():
        lower_np = np.array(lower)
        upper_np = np.array(upper)
        mask = cv2.inRange(hsv_frame, lower_np, upper_np)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Determine quadrant and log entry/exit
            quadrant = determine_quadrant(x, y, w, h, frame.shape[1], frame.shape[0])
            events.append({
                'time': current_time,
                'quadrant': quadrant,
                'color': color_name,
                'event_type': 'Entry/Exit'
            })

    return frame, events

def determine_quadrant(x, y, w, h, frame_width, frame_height):
    if x < frame_width // 2 and y < frame_height // 2:
        return 1
    elif x >= frame_width // 2 and y < frame_height // 2:
        return 2
    elif x < frame_width // 2 and y >= frame_height // 2:
        return 3
    elif x >= frame_width // 2 and y >= frame_height // 2:
        return 4

def log_event(log, time, quadrant, color, event_type):
    log.append(f"{time}, {quadrant}, {color}, {event_type}")
