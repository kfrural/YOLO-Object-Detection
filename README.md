# YOLO Object Detection

This project implements an object detection system using the YOLO (You Only Look Once) architecture, enabling real-time object detection in images and videos.

## Project Overview

The project utilizes the Darknet framework to implement YOLO object detection, with optional GPU support via CUDA for enhanced performance. The system includes tools for data labeling, model training, and inference.

## System Components

The system consists of four main components:

**Data Preparation**- Initial image labeling using LabelMe
- Conversion of JSON files to YOLO format
- Organization of data in specific directories

**Project Configuration**- Training configuration files
- YOLOv4 base model for transfer learning

**Model Training**- Darknet framework training process
- CUDA integration for GPU acceleration (optional)

**Object Detection**- Utilization of trained model for detecting objects in new images

## Prerequisites

- Darknet (main framework)
- CUDA (optional, for NVIDIA GPUs)
- Python dependencies:
```bash
pip install numpy opencv-python
```



## Installation

Clone the repository:

```bash
git clone https://github.com/kfrural/YOLO-Object-Detection.git
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Data Labeling

Open LabelMe and label your imagesRun the conversion script:

```bash
python script/convert_json_to_yolo.py --dir path_to_images
```

### Training

Configure files in `cfg/`:- `obj.data`: dataset configurations
- `yolo-obj.cfg`: network parameters

Execute training:

```bash
./darknet detector train cfg/obj.data cfg/yolo-obj.cfg yolov4.conv.137 -dont_show -map
```

### Detection

To perform detection on an image:

```bash
./darknet detector test cfg/obj.data cfg/yolo-obj.cfg backup/yolov4-custom_last.weights -thresh 0.25 image_path.jpg
```

## Technical Details

- The model utilizes YOLOv4 as base architecture, achieving 55.8% AP on COCO test-dev dataset
- CUDA-enabled training significantly accelerates processing
- The system supports real-time detection with optimized performance
