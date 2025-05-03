# MLOPS Pipeline Implementation

This project represents my implementation of a machine learning operations (MLOPS) pipeline, combining ML model development with DevOps practices. It's designed to demonstrate how to effectively deploy and manage ML models in a production environment.

## Project Overview

Here's the structure of my MLOPS pipeline implementation:

```
.
├── app.py              # Production API endpoint
├── train.py           # Model training pipeline
├── model.pkl          # Serialized production model
├── requirements.txt   # Environment dependencies
├── Dockerfile         # Containerization setup
└── data/             # Training and validation datasets
```

## Tech Stuff I Used

- **Backend**: Flask (simple and works great for APIs)
- **ML**: scikit-learn (for the Random Forest model)
- **Data**: NumPy (for handling the numbers)
- **Container**: Docker (to make deployment easy)

## What You Need to Run This

Before you start playing with this, make sure you have:
- Docker (to run it in containers) - [Install Docker Desktop](https://www.docker.com/products/docker-desktop)
- A Docker Hub account (for pulling the latest image)


## How the API Works

The API is pretty straightforward - it takes 8 health measurements and tells you if someone might have diabetes. Here's what you need to send:

1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI
7. Diabetes Pedigree Function
8. Age

Just send these numbers in order, and you'll get back a 0 (no diabetes) or 1 (diabetes predicted).

## Let's Get Started!

### Testing the API

The easiest way to run this is using the pre-built image from Docker Hub:

1. Pull the latest image:
```bash
# Make sure Docker Desktop is running
# Log in to Docker Hub first
# This will pull latest image available
docker pull alapdevops/mlops-repo:latest
```

Important: You'll need two terminal windows for this!

2. First Terminal (Keep this running):
```bash
docker run -p 5000:5000 alapdevops/mlops-repo:latest
```
Don't close this terminal - it needs to keep running to serve the API.

3. Second Terminal (For testing):
Open a new terminal window and run this command:
```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\"features\": [4, 127, 88, 11, 155, 34.5, 0.598, 28]}"
```

You can replace the numbers in the features array with your own values. Just make sure to keep the same order:
1. Pregnancies (e.g., 4)
2. Glucose (e.g., 127)
3. Blood Pressure (e.g., 88)
4. Skin Thickness (e.g., 11)
5. Insulin (e.g., 155)
6. BMI (e.g., 34.5)
7. Diabetes Pedigree Function (e.g., 0.598)
8. Age (e.g., 28)

You should see something like:
```json
{
    "prediction": 0
}
```

## For Local Development

Here's how to get started:

1. **Clone the Repository**:
```bash
# Create a new directory for the project
mkdir mlops-project
cd mlops-project

# Clone the repository
git clone https://github.com/ralphtorrejos-devops/pipeline-mlops-test.git
cd pipeline-mlops-test

# Install required Python packages from requirements.txt
# This will install Flask, scikit-learn, joblib, and other dependencies
pip install -r requirements.txt
```

2. **Create a New Branch**:
```bash
# Create and switch to a new branch
git checkout -b feature/your-feature-name
```

3. Make your changes and send a pull request

### What Happens After Your Pull Request is Approved

Once your pull request is approved and merged:
1. The MLOPs pipeline automatically triggers
2. A new Docker image is built with your changes
3. The image is automatically pushed to Docker Hub Repo (https://hub.docker.com/repository/docker/alapdevops/mlops-repo/general)
4. The latest version becomes available for everyone to use

This automated process ensures that:
- Your changes are quickly available
- The deployment is consistent
- Everything is properly tested before going live


## Pipeline Config Documentation

This project implements modern DevOps practices through automated CI/CD pipelines. The entire process from code changes to deployment is automated, ensuring consistent and reliable updates to the production environment.

The `.github/workflows/deploy.yml` file is like a recipe that tells GitHub Actions what to do whenever you make changes to your code. Here's what it does:

1. **When to Run**: It automatically starts whenever you push changes to your main branch.

2. **Environment Setup**: 
   - Sets up a fresh Ubuntu server
   - Installs Python 3.10
   - Gets all your project files

3. **Dependencies**: 
   - Installs all the Python packages your project needs
   - Makes sure everything is ready to run

4. **Model Training**:
   - Runs your training script
   - Creates a fresh model with the latest data
   - Makes sure the model is ready for predictions

5. **Docker Image Management**:
   - Builds a new Docker image with your latest code
   - Tags it with your Docker Hub username
   - Pushes it to Docker Hub so it's ready to use

6. **Security**:
   - Uses secure tokens to log into Docker Hub
   - Keeps your credentials safe
   - Makes sure only authorized pushes happen

This setup means you don't have to worry about manually building and pushing your Docker image - it happens automatically whenever you update your code!