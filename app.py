import cv2
import tkinter as tk
from tkinter import messagebox
from ultralytics import YOLO

def start_detection():
    # Load the pre-trained, lightweight YOLOv8 nano model
    # The first time you run this, it will automatically download 'yolov8n.pt' safely into your folder
    try:
        model = YOLO("yolov8n.pt")
    except Exception as e:
        messagebox.onerror("Error", f"Failed to load YOLO model: {e}")
        return

    # Start the video stream from your default webcam (0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access the webcam. Please check your camera settings.")
        return

    # Hide the main Tkinter setup window while camera runs to keep screen clean
    root.withdraw()

    print("Opening camera stream... Press the 'q' key on your keyboard to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab camera frame.")
            break

        # Run the YOLOv8 model tracking on the current frame
        # persist=True ensures objects are tracked with a unique ID across frames
        results = model.track(frame, persist=True)

        # Draw the bounding boxes, confidence percentages, and tracking IDs onto the live frame
        annotated_frame = results[0].plot()

        # Display the live tracked visual feed window
        cv2.imshow("CodeAlpha - Live Object Detection & Tracking", annotated_frame)

        # Break the loop immediately if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all pop-up windows cleanly
    cap.release()
    cv2.destroyAllWindows()
    
    # Bring back the Tkinter menu window
    root.deiconify()

# ==========================================
# Designing the Control Interface (UI)
# ==========================================
root = tk.Tk()
root.title("CodeAlpha - Computer Vision Engine")
root.geometry("450x250")
root.configure(bg="#f4f4f6")

# App Title Header
lbl_title = tk.Label(root, text="AI Object Detection & Tracking", font=("Arial", 16, "bold"), bg="#f4f4f6", fg="#333333")
lbl_title.pack(pady=25)

# Explanatory prompt label
lbl_desc = tk.Label(root, text="Click below to open your camera.\nShow items like your phone, a cup, or a book to the camera!", font=("Arial", 10), bg="#f4f4f6", fg="#666666")
lbl_desc.pack(pady=10)

# Action button styled with CodeAlpha signature color
btn_start = tk.Button(root, text="Launch Camera Stream", bg="#e0115f", fg="white", font=("Arial", 11, "bold"), width=22, height=2, command=start_detection)
btn_start.pack(pady=15)

root.mainloop()
