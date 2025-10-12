<!-- 1404-07-19 -->
### Federated Learning:

- Install Flower:
  - pip install flwr
  - pip install "flwr[simulation]"
  - import flwr
  - print(flwr.__version__) # 1.22.0

### Cases:
- data is not available on a centralized server
- data available on one server is not enough to train a good model
- Regulations
- User preference
- Data volume
- Privacy

### Compare:
- Centralized machine learning: move the data to the computation
- Federated (machine) Learning: move the computation to the data

### Federated learning in five steps:
- Step 0: Initialize global model
- Step 1: Send model to a number of connected organizations/devices (client nodes)
- Step 2: Train model locally on the data of each organization/device (client node)
- Step 3: Return model updates back to the server
- Step 4: Aggregate model updates into a new global model
  - Federated Averaging (McMahan et al., 2016), often abbreviated as FedAvg
- Step 5: Repeat steps 1 to 4 until the model converges

### cross-silo
- We simulate having multiple datasets from multiple organizations (also called the “cross-silo” setting in federated learning) by splitting the original CIFAR-10 dataset into multiple partitions.
