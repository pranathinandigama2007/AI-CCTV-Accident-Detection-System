# Automated AI CCTV Accident Detection & Emergency Alert System

An intelligent traffic monitoring application built with Python, YOLOv8, and OpenCV. The system dynamically processes live CCTV feeds to automatically detect vehicular collisions, switch dashboard layouts, and instantly deploy a native system dispatch notification.

##  Key Features
- **Automated Collision Analysis:** Utilizes bounding box overlap logic to identify high-risk traffic events automatically without user input.
- **Dynamic UI State Switching:** Instantly shifts dashboard rendering from a green monitoring state to a fixed red emergency state upon vehicle impact.
- **Fail-Safe Continuous Playback:** Automatically resumes post-alert video streaming to track traffic aftermath seamlessly after the user dismisses the alert dialog.
- **One-Click Presentation Launcher:** Includes a Windows batch script wrapper (`run_project.bat`) for quick, seamless deployment during live demonstrations.

## Tech Stack
- **Language:** Python
- **Computer Vision:** OpenCV (`cv2`)
- **AI Framework:** Ultralytics YOLOv8
- **OS Subsystem Layer:** Windows `ctypes` API

##  How to Run
1. Clone this repository to your local machine.
2. Ensure your demo video `accident_demo.mp4` is placed inside the `videos` folder.
3. Install the required dependencies: `pip install ultralytics opencv-python`.
4. Double-click the `run_project.bat` file to launch the full-screen simulation dashboard instantly.
