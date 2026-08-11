### Subfields of artificial intelligence:
- Perception
- Machine learning (ML)
  - Deep learning (DL) : Using multi-layered non-linear function approximation, typically neural networks.
- Expert systems
- Planning
- Natural language processing
- Computer vision
- Robotics
- Search
- Logic

### There are three main branches of ML: 
- Supervised learning (SL)
- Unsupervised learning (UL)
- Reinforcement learning (RL)
  - Deep reinforcement learning (DRL) is the intersection of reinforcement learning and deep learning.

### Definition:
- Open Neural Network Exchange (ONNX)
 
### Tools:
- RKNN software stack can help users to quickly deploy AI models to Rockchip chips.
  - rknn-toolkit2: https://github.com/airockchip/rknn-toolkit2
  - yolo export model=yolo26s.pt format=rknn opset=19
  - python rknn_export/convert.py --model-path yolo26s.onnx --platform rk3588 --dtype i8
  - Think of .pt as the source code and .onnx as the compiled executable that's designed to run anywhere.
  - The .pt file is the standard format for saving a model in PyTorch, the deep learning framework that YOLO is built upon.
  - It's a snapshot of your model's "brain"—its learned weights and its architecture, saved in PyTorch's native format.
  - Performance: A major reason to convert to ONNX is faster inference.

 - ExecuTorch: https://github.com/pytorch/executorch
   - ExecuTorch is PyTorch's unified solution for deploying AI models on-device—from smartphones to microcontrollers—built for privacy, performance, and portability.
