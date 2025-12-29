# image_classifier_CNN
A 10 class image classifier using cifar10 dataset

📝 One-Line Summary

A Convolutional Neural Network (CNN) based image classification system trained on the CIFAR-10 dataset to classify real-world images into one of ten object categories.

📊 Dataset

- CIFAR-10 Dataset

Total images: 24,000

Training images: 20,000

Testing images: 4,000

- Image size: 32 × 32 × 3 (RGB)

- Number of classes: 10

- Classes:

Plane
Car
Bird
cat
Deer
Dog
Frog
Horse
Ship
Truck

- Dataset loaded using:

datasets.cifar10.load_data()

🛠️ Tools and Technologies

- Programming Language: Python

- Deep Learning Framework: TensorFlow (Keras API)

- Image Processing: OpenCV

- Numerical Computing: NumPy

- Visualization: Matplotlib

- Dataset: CIFAR-10

🧠 Model / Output
CNN Architecture:

- Convolution Layer (32 filters, 3×3)

- Max Pooling Layer

- Convolution Layer (64 filters, 3×3)

- Max Pooling Layer

- Convolution Layer (64 filters, 3×3)

- Flatten Layer

- Fully Connected Dense Layer (64 neurons)

- Output Layer (10 neurons with Softmax)

Model Output:

- Predicts the class of an input image

- Displays the predicted category name (e.g., Truck, Car, Dog)

Example output:
Prediction is Truck

✅ Result and Conclusion

- The CNN successfully learns visual patterns from the CIFAR-10 dataset.

- The trained model can accurately classify real-world images after resizing and normalization.

- The project demonstrates the effectiveness of CNNs for image recognition tasks.

- This system can be extended to larger datasets or real-time applications.

- Loss: 1.1529992818832397
- Accuracy: 0.6159999966621399

▶️ How to Run This Project
- Step 1: Clone the repository

- Step 2: Install required libraries
pip install tensorflow numpy matplotlib opencv-python

- Step 3: Place an image
Add a test image (e.g., truck.jpg) inside the project folder and put the relative path inside img=cv.imread(here)
eg: img=cv.imread('truck.jpg')

- Step 4: Run the program
python main.py

👩‍💻 Author

Anushka Chauhan
