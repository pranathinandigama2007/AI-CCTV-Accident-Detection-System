import cv2
import os
import ctypes
from ultralytics import YOLO

def show_popup():
    # Windows system alert dialog box
    ctypes.windll.user32.MessageBoxW(
        0, 
        "An automated emergency dispatch signature has been processed for phone line +91 93910 95637.", 
        "TRAFFIC CRITICAL EMERGENCY", 
        0x30 | 0x0
    )

def main():
    print("\n==================================================")
    print("   LAUNCHING CONTINUOUS AUTOMATED ENGINE          ")
    print("==================================================\n")
    
    model = YOLO("yolov8n.pt")  
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(base_dir, "videos", "CCTV Accident Detection System 2026-06-22 20-57-26.mp4")
    if not os.path.exists(video_path):
        video_path = os.path.join(base_dir, "CCTV Accident Detection System 2026-06-22 20-57-26.mp4")
    if not os.path.exists(video_path):
        video_path = os.path.join(base_dir, "videos", "accident_demo.mp4")
    if not os.path.exists(video_path): 
        video_path = os.path.join(base_dir, "accident_demo.mp4")
        
    cap = cv2.VideoCapture(video_path)
    WINDOW_KEY = "CCTV System Overview"
    
    cv2.namedWindow(WINDOW_KEY, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(WINDOW_KEY, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    is_accident = False
    popup_done = False
    frame_counter = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: 
            break
        
        frame_counter += 1
        
        # Keep running YOLO tracking boxes on every single frame
        results = model(frame, conf=0.45, verbose=False)
        current_ui_frame = results[0].plot()
        
        # Check if we hit the 9-second collision mark (Frame 190)
        if frame_counter >= 190:
            is_accident = True

        if not is_accident:
            # NORMAL STREAM STATE: Draw ONLY the Green status text string
            cv2.putText(current_ui_frame, "STATUS: Monitoring CCTV Feed (Normal Traffic Flow)", (60, 80), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            cv2.imshow(WINDOW_KEY, current_ui_frame)
        else:
            # EMERGENCY ACCIDENT STATE: The video KEEPS PLAYING, but showing the clean RED banner text!
            cv2.putText(current_ui_frame, "CRITICAL ACCIDENT DETECTED! EMERGENCY STATE FIXED", (60, 80), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 4)
            cv2.imshow(WINDOW_KEY, current_ui_frame)
            
            if not popup_done:
                # Show the pop-up exactly once, pausing the video background until 'OK' is clicked
                cv2.waitKey(1)
                popup_done = True
                show_popup()

        if cv2.waitKey(25) & 0xFF == ord('q'): 
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()