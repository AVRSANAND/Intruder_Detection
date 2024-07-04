# Intruder Detector

A Python-based intruder detection system that captures video from a webcam, detects objects in real-time, and sends an email notification with an image attachment when an object is detected.

## Key Features

- **Real-Time Object Detection:** Captures video from a webcam and processes it to detect objects.
- **Email Notification:** Sends an email with an image attachment when an object is detected.
- **Image Storage and Cleanup:** Saves detected object images and periodically cleans the storage folder.
- **Multithreading:** Uses threading to handle email sending and folder cleanup without interrupting the main detection process.

## How It Works

1. **Capture Video:** The script captures video frames from the default webcam using OpenCV.
2. **Process Frames:** Each frame is converted to grayscale and blurred to reduce noise. The first frame is used as a reference for detecting changes.
3. **Detect Motion:** The difference between the current frame and the reference frame is computed. Thresholding and dilation are applied to highlight regions with motion.
4. **Identify Objects:** Contours are detected in the processed frame. If a contour's area exceeds a certain threshold, it is considered an object.
5. **Save and Email Image:** When an object is detected, the frame is saved as an image, and an email with the image attachment is sent.
6. **Clean Up:** The images folder is periodically cleaned to remove old images.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AVRSANAND/Intruder_Detection.git
    cd Intruder_Detector
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up email credentials in `send_mail.py`:
    ```python
    email_sender = "your_email@gmail.com"
    password = "your_app_password"
    receiver = "receiver_email@gmail.com"
    ```

## Usage

1. Run the main script:
    ```bash
    python main.py
    ```

2. Press q to quit the video stream.

## Files
1. main.py: Main script for capturing video, detecting objects, and sending emails.

2. send_mail.py: Script for sending email notifications with image attachments.

