
# pip install cachetools==4.1.1 coremltools==4.0 Keras-Preprocessing==1.1.2 joblib==0.16.0  importlib-metadata==1.7.0 numpy==1.24 cython==0.29.21 protobuf==3.20.3 tensorflow==2.13

import coremltools as ct
from tensorflow.keras.models import load_model
# Convert model to CoreML
keras_model = load_model("best_lstm_yolo_model_20240903_1854.h5")

# 获取模型配置
model_config = model.get_config()
print(model_config)

# # 保存配置为 JSON 文件
# with open("model_config.json", "w") as json_file:
#     json.dump(model_config, json_file, indent=4)

# coreml_model = ct.convert(keras_model)
# #coreml_model = ct.converters.keras.convert("best_lstm_yolo_model_20240903_1854.h5")

# # Model metadata
# coreml_model.author = 'Hello <hello@gmail.com>'
# coreml_model.short_description = 'lstm yolo model'

# # Save CoreML model
# coreml_model.save('best_lstm_yolo_model_20240903_1854.mlmodel')