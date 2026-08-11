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
