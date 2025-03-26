# UAV Building Detection

## Dataset Access
You can access the data on following link:
>https://drive.google.com/file/d/1emLAe7002_syWNxsTO0MgVg4knokFVlQ/view

## Research Paper
For detailed methodology and results, please refer to:
>https://www.sciencedirect.com/science/article/pii/S1569843222001595

## Documentation
Detailed project documentation is available here:
> [documentation](https://github.com/dolphinium/uav-building-detection/blob/main/documentation/documentation.pdf)

## Tools and Technologies Used

### Deep Learning Frameworks
- YOLOv8 (Nano, Small, and X variants)
- YOLOv10 (Nano, Small, and Medium variants)
- Ultralytics Framework

### Development Tools
- Python 3.x
- Gradio (for web interface deployment)
- PIL (Python Imaging Library)
- XML parsing libraries (for dataset preprocessing)

### Dataset Processing
- Custom preprocessing scripts for:
  - PASCAL VOC to YOLO format conversion
  - Dataset splitting (train/val/test)
- Support for multiple datasets:
  - RescueNet dataset
  - UAVOD-10 dataset

### Model Training Infrastructure
- Comet ML (for experiment tracking)
- Custom training configurations:
  - Batch size: 16
  - Epochs: 30
  - Multiple model variants comparison

### Deployment
- HuggingFace Spaces (planned)
- Gradio web interface for model inference

## Project Structure
```
.
├── documentation/     # Project documentation
├── preprocess/       # Data preprocessing scripts
├── weights/          # Trained model weights
├── yolos/           # YOLO model configurations
└── gradio_uav_test.py  # Web interface deployment
```

## TODOs:
* Create requirements.txt
* Host the model on HuggingFace Spaces

## Model Performance
The project includes comprehensive comparisons between:
- YOLOv8 variants (Nano, Small, X)
- YOLOv10 variants (Nano, Small, Medium)
- Training vs Validation loss analysis
- Output quality comparisons

For detailed performance metrics and comparisons, please refer to the documentation.
