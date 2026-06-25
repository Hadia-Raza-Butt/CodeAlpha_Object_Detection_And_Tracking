# CodeAlpha - Live Object Detection & Tracking

A real-time computer vision application built as part of the **CodeAlpha Artificial Intelligence Internship**. This system leverages the state-of-the-art **YOLOv8** deep learning model alongside **OpenCV** to capture live webcam streams, draw bounding boxes, identify objects, and assign persistent tracking IDs seamlessly.

## Features
* **Real-Time DL Architecture**: Implements a pre-trained `yolov8n.pt` framework for high-speed frame processing.
* **Persistent Object Tracking**: Keeps tabs on individual items across the video frame layout using continuous frame matrices.
* **Control UI**: A clean Tkinter-based start control menu to initialize and cleanly close video capture streams.

## Tech Stack & Dependencies
* **Language**: Python 3.13+
* **Computer Vision / AI**: `ultralytics` (YOLOv8), `opencv-python`, `torch`
* **GUI Framework**: `Tkinter`

## Setup & Installation

1. **Install Dependencies**:
   ```bash
   pip install opencv-python ultralytics legacy-cgi
