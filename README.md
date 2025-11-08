# Virtual Background

Real-time webcam background replacement using AI-powered segmentation. Remove your background and replace it with any image.

## What It Does

- Captures video from your webcam
- Removes the background using AI segmentation
- Replaces it with images from the `images/` folder
- Switch backgrounds on the fly with keyboard controls

Controls:
   - `a` - Previous background
   - `d` - Next background
   - `q` - Quit

## How It Works

1. **Video Capture**: Uses OpenCV to capture frames from webcam (640x480)
2. **Segmentation**: cvzone's SelfiSegmentation uses MediaPipe to detect and segment the person
3. **Background Replacement**: The segmented person is composited onto the selected background image
4. **Display**: Real-time preview window shows the result

## Dependencies

- `opencv-python` - Video capture and image processing
- `cvzone` - AI segmentation models
- `numpy` - Array operations

## Technical Details
- Resolution: 640x480
- Frame rate: Depends on your system performance
- Segmentation model: MediaPipe Selfie Segmentation (via cvzone)
