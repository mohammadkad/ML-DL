from ultralytics import YOLO

model = YOLO("yolo26n.pt")
print(model.ckpt["train_args"])
