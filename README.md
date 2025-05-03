# MLOP Pipeline Implementation

This project represents my implementation of a machine learning operations (MLOP) pipeline, combining ML model development with DevOps practices. It's designed to demonstrate how to effectively deploy and manage ML models in a production environment.

## Project Overview

Here's the structure of my MLOP pipeline implementation:

```
.
├── app.py              # Production API endpoint
├── train.py           # Model training pipeline
├── model.pkl          # Serialized production model
├── requirements.txt   # Environment dependencies
├── Dockerfile         # Containerization setup
└── data/             # Training and validation datasets
```

## Implementation Stack

- **API Framework**: Flask
- **ML Framework**: scikit-learn
- **Model Serialization**: joblib
- **Data Processing**: NumPy
- **Containerization**: Docker
- **CI/CD**: GitHub Actions (planned)

## System Requirements

To run this pipeline, you'll need:
- Python 3.8+
- pip package manager
- Git
- Docker (for containerized deployment)

## Pipeline Setup

### 1. Repository Setup
```bash
# First, open your terminal or command prompt
# Navigate to where you want to store the project
# Then run these commands:

git clone https://github.com/ralphtorrejos-devops/pipeline-mlops-test.git
```

### 2. Install Dependencies
```bash
# Make sure you're in the project directory
# Then install all required packages:

pip install -r requirements.txt
```

## Pipeline Components

### Model Training
The `train.py` script handles:
- Loading training and test data from CSV files
- Training a Random Forest Classifier
- Evaluating model performance using accuracy and classification report
- Saving the trained model to `model.pkl`
- Verifying the saved model's feature requirements

### API Deployment
The `app.py` implements:
- A single POST endpoint at `/predict`
- Loads the trained model from `model.pkl`
- Accepts JSON input with 8 features
- Returns prediction (0 or 1) with HTTP 200 on success
- Returns error message with HTTP 400 on failure
- Runs on host 0.0.0.0 and port 5000

### Containerization
The `Dockerfile` sets up:
- Python 3.10 slim base image
- Working directory at `/app`
- Installs dependencies from requirements.txt
- Copies all project files
- Exposes port 5000
- Runs app.py as the container command

### Docker Build
```bash
# Build the Docker image
docker build -t ml-flask-api:latest .


## API Implementation

### API Overview
The API is a Flask-based web service that provides diabetes prediction using a trained Random Forest model. It exposes a single POST endpoint at `/predict` that accepts 8 health measurements and returns a binary prediction (0 or 1).

The API runs on:
- Host: 0.0.0.0
- Port: 5000
- Endpoint: POST /predict

## Testing the API

### Quick Start
1. Start the server:
   - Open a terminal window
   - Navigate to the project directory
   - Run the following command:
   ```bash
   python app.py
   ```
   - Keep this terminal window open as the server needs to keep running
   - The server will be available at http://localhost:5000

2. Test the API:
   - Open a new terminal window
   - Execute the following command:
   ```bash
   curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"features\": [4, 127, 88, 11, 155, 34.5, 0.598, 28]}"
   ```

## Features
The model expects these 8 features in order:
1. Pregnancies
2. Glucose
3. BloodPressure
4. SkinThickness
5. Insulin
6. BMI
7. DiabetesPedigreeFunction
8. Age

## API Documentation

### What is this API?
This API is a simple web service that helps predict whether someone might have diabetes based on 8 health measurements.

### How to Use the API

#### 1. Basic Information
- **Where to Send Requests**: `http://localhost:5000/predict`
- **Type of Request**: POST
- **Format**: JSON

#### 2. What Data to Send
Send 8 health measurements in this order:
```json
{
    "features": [
        pregnancies,      // Number of pregnancies
        glucose,         // Glucose level in blood
        blood_pressure,  // Blood pressure measurement
        skin_thickness,  // Skin fold thickness
        insulin,         // Insulin level
        bmi,            // Body Mass Index
        pedigree,       // Diabetes pedigree function
        age            // Age in years
    ]
}
```

#### 3. Example Request
```json
{
    "features": [4, 127, 88, 11, 155, 34.5, 0.598, 28]
}
```

#### 4. What You'll Get Back
If successful:
```json
{
    "prediction": 0
}
```
- `0` means "No diabetes predicted"
- `1` means "Diabetes predicted"

#### 5. If Something Goes Wrong
You'll get an error message:
```json
{
    "error": "Please provide all 8 features"
}
```



## Pipeline Configuration

### GitHub Actions Pipeline
The project uses GitHub Actions for CI/CD, configured in `.github/workflows/deploy.yml`. The pipeline automatically runs when code is pushed to the main branch.

#### Pipeline Stages
1. **Build and Test**
   - Sets up Python 3.10 environment
   - Installs project dependencies
   - Retrains the ML model with latest data
   - Builds the Docker image

2. **Deployment** (Automated)
   - The pipeline automatically:
     - Sets up Python 3.10 environment
     - Installs project dependencies
     - Retrains the ML model with latest data
     - Builds the Docker image with tag `alapdevops/mlops-repo:latest`
     - Pushes the image to Docker Hub for distribution

#### Pipeline Configuration
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]  # This workflow runs when you push to the main branch

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest  # Use a Linux server in the cloud for the job
    steps:
      - uses: actions/checkout@v3  # Step 1: Download your code from GitHub

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'  # Step 2: Install Python 3.10

      - name: Install dependencies
        run: pip install -r requirements.txt  # Step 3: Install your Python libraries

      - name: Retrain Model
        run: python train.py  # Step 4: Retrain your model with the latest data

      - name: Build Docker image
        run: docker build -t alapdevops/mlops-repo:latest .  # Step 5: Build a new Docker image

      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Push to Docker Hub
        run: |
          docker push alapdevops/mlops-repo:latest
```

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request 

