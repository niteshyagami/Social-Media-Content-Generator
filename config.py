"""
Configuration module for the Social Media Content Generator.
Manages API keys, model selection, and generation parameters.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for AI and content generation settings."""
    
    # API Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    
    # Model Selection
    AI_MODEL = os.getenv("AI_MODEL", "google").lower()  # "google" or "openai"
    
    # Generation Parameters
    TEMPERATURE = float(os.getenv("MODEL_TEMPERATURE", "0.7"))
    MAX_TOKENS = 500
    
    # Content Generation Prompts
    PROMPTS = {
        "instagram_post": """Generate an engaging Instagram post about {theme}. 
        Include a compelling caption (50-150 characters) that hooks users, 
        and 5 relevant hashtags. Format the response as:
        Caption: [caption here]
        Hashtags: [hashtags here]""",
        
        "twitter_post": """Create a catchy Twitter/X post about {theme}.
        The post should be 280 characters max and include 1-2 relevant hashtags.
        Make it engaging and shareable.""",
        
        "facebook_post": """Write a Facebook post about {theme}.
        Include an engaging opening, main content (2-3 sentences), 
        and a call-to-action. Add 3-4 relevant hashtags at the end.""",
        
        "linkedin_post": """Craft a professional LinkedIn post about {theme}.
        Make it informative and valuable for professionals.
        Include a strong opening, insights, and a call-to-action.""",
        
        "tiktok_caption": """Generate a fun TikTok video caption about {theme}.
        Keep it trendy, playful, and include relevant hashtags (5-10).
        Make it youth-friendly and engaging.""",
        
        "email_subject": """Create 3 engaging email subject lines about {theme}.
        Each should be compelling and increase open rates.
        Format: 1. [subject line], 2. [subject line], 3. [subject line]""",
        
        "general_content": """Generate creative social media content about {theme}.
        Provide:
        - A catchy headline
        - Main message (2-3 sentences)
        - Call-to-action
        - 5 hashtags"""
    }
    
    @staticmethod
    def validate_config():
        """Validate that necessary configuration is set."""
        if Config.AI_MODEL == "google" and not Config.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY is not set. Please set it in .env file.")
        elif Config.AI_MODEL == "openai" and not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set. Please set it in .env file.")
        return True


if __name__ == "__main__":
    print("Configuration loaded successfully!")
    print(f"AI Model: {Config.AI_MODEL}")
    print(f"Temperature: {Config.TEMPERATURE}")
