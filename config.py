import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "a3f6e7c5b2d8a9f0e1c4d3b6a7e8f9d0c2b5a6d3e4f7a9b0c1d2e3f4a5b6c7d8")
    PORT = int(os.getenv("PORT", 5000))  # Default port for Azure Web Apps
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    ALLOWED_HOSTS = ["*"]  # Allow all hosts (modify if needed)
