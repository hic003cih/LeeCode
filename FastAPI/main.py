from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

app = FastAPI()

# 載入模型
model = load_model("mnist_model.h5")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # 讀取圖片
    image = Image.open(file.file).convert("L").resize((28, 28))
    image_array = np.array(image) / 255.0  # 正規化
    image_array = image_array.reshape(1, 28, 28)  # 加 batch 維度

    # 預測
    prediction = model.predict(image_array)
    predicted_label = int(np.argmax(prediction))

    return {"prediction": predicted_label}
