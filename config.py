import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")
    PORT = int(os.getenv("PORT", 5000))  # Default port for Azure Web Apps
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    ALLOWED_HOSTS = ["*"]  # Allow all hosts (modify if needed)
