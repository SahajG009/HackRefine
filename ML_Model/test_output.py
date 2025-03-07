from PIL import Image
import numpy as np
from keras.preprocessing import image
from keras.models import model_from_json
import os

def load_model():
    # Load the model architecture from the JSON file
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    
    # Create the model from the JSON file
    loaded_model = model_from_json(loaded_model_json)
    
    # Load the weights into the model
    loaded_model.load_weights("model.h5")
    
    print("Model loaded successfully.")
    
    return loaded_model

def predict_disease(model, image_path):
    # Load and preprocess the input image using Pillow;lplkpop
    img = Image.open(image_path)
    img = img.resize((128, 128))  # Resize the image if needed
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Make a prediction
    result = model.predict(img_array)
    
    # Map the prediction to a human-readable label
    labels = ["Potato___Early_blight",
    "Potato___Healthy",
    "Potato___Late_blight use Pest-Abtec Bio Neem Plant Pesticide-Neem Oil(Azadirachtin)-Control Aphids",
    "Tomato___Target_Spot use pest-agro pure water",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus use pest-agro fertilize to keep healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Healthy",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold use Pest-Agro Plus AM003_1 Pesticide",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Tomato_mosaic_virus use Pest-Agro Plus AM003_1 Pesticide"]
    
    predicted_class = labels[np.argmax(result)]
    
    return predicted_class

def get_image_path():
    # Take input from the user for the image path
    image_path = input("Enter the path to the input image: ")

    return image_path

if __name__ == "__main__":
    # Load the pre-trained model
    model = load_model()

    if model:
        # Take input image address from the user
        image_path = get_image_path()

        try:
            # Make a prediction
            result = predict_disease(model, image_path)
            
            # Display the result
            print("Predicted disease: ", result)
        except Exception as e:
            print("Error: ", str(e))
