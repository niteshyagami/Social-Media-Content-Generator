"""
Content Generator module for Social Media Content Generator.
Handles communication with AI models and content generation.
"""

import google.generativeai as genai
from config import Config
from typing import Dict, List, Optional


class ContentGenerator:
    """Main class for generating social media content using AI."""
    
    def __init__(self):
        """
        Initialize the ContentGenerator.
        Sets up the AI model based on configuration.
        """
        Config.validate_config()
        
        if Config.AI_MODEL == "google":
            # Configure Google Generative AI
            genai.configure(api_key=Config.GOOGLE_API_KEY)
            # Try to use the latest available model
            try:
                # List available models and use the first generative one
                models = genai.list_models()
                generative_models = [m for m in models if 'generateContent' in m.supported_generation_methods]
                if generative_models:
                    self.model = genai.GenerativeModel(generative_models[0].name)
                else:
                    # Fallback to a known model
                    self.model = genai.GenerativeModel("gemini-pro")
            except Exception:
                # If listing fails, use default model
                self.model = genai.GenerativeModel("gemini-pro")
        else:
            raise ValueError(f"Unsupported AI model: {Config.AI_MODEL}")
    
    def generate_content(
        self, 
        theme: str, 
        content_type: str = "general_content",
        num_variations: int = 1
    ) -> Dict[str, any]:
        """
        Generate social media content based on theme and content type.
        
        Args:
            theme (str): The topic or keyword for content generation
            content_type (str): Type of content (instagram_post, twitter_post, etc.)
            num_variations (int): Number of content variations to generate
        
        Returns:
            Dict: Generated content with metadata
        """
        if content_type not in Config.PROMPTS:
            raise ValueError(
                f"Invalid content type: {content_type}. "
                f"Available types: {', '.join(Config.PROMPTS.keys())}"
            )
        
        # Prepare the prompt
        base_prompt = Config.PROMPTS[content_type]
        full_prompt = base_prompt.format(theme=theme)
        
        # Add variation instruction if needed
        if num_variations > 1:
            full_prompt += f"\n\nGenerate {num_variations} different versions of this content."
        
        try:
            # Generate content using Google Generative AI
            response = self.model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=Config.TEMPERATURE,
                    max_output_tokens=Config.MAX_TOKENS,
                )
            )
            
            # Extract text from response
            generated_text = response.text
            
            return {
                "success": True,
                "theme": theme,
                "content_type": content_type,
                "generated_content": generated_text,
                "model_used": Config.AI_MODEL,
                "variations": num_variations
            }
        
        except TimeoutError:
            return {
                "success": False,
                "error": "Request timed out. Please try again.",
                "theme": theme,
                "content_type": content_type
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "theme": theme,
                "content_type": content_type
            }
    
    def generate_multiple_platforms(
        self, 
        theme: str, 
        platforms: Optional[List[str]] = None
    ) -> Dict[str, any]:
        """
        Generate content optimized for multiple social media platforms.
        
        Args:
            theme (str): The topic or keyword for content generation
            platforms (List[str]): List of platforms to generate content for
                                    (instagram, twitter, facebook, linkedin, tiktok, email)
        
        Returns:
            Dict: Generated content for each platform
        """
        if platforms is None:
            platforms = ["instagram_post", "twitter_post", "facebook_post", "linkedin_post"]
        
        results = {
            "theme": theme,
            "platforms": {},
            "success": True
        }
        
        for platform in platforms:
            # Handle platform naming - some already have suffixes
            if "_post" in platform or "_caption" in platform or "_subject" in platform:
                content_type = platform
            else:
                content_type = f"{platform}_post" if platform != "email" else f"{platform}_subject"
            
            result = self.generate_content(theme, content_type, num_variations=1)
            
            if result["success"]:
                results["platforms"][platform] = result["generated_content"]
            else:
                results["success"] = False
                results["platforms"][platform] = f"Error: {result['error']}"
        
        return results
    
    def generate_hashtag_set(self, theme: str, count: int = 10) -> Dict[str, any]:
        """
        Generate a set of relevant hashtags for a given theme.
        
        Args:
            theme (str): The topic for which to generate hashtags
            count (int): Number of hashtags to generate
        
        Returns:
            Dict: Generated hashtags with metadata
        """
        prompt = f"""Generate {count} relevant and trending hashtags for posts about: {theme}
        
        Requirements:
        - Mix of popular hashtags and niche hashtags
        - Should be relevant to the topic
        - Include both short and medium-length hashtags
        
        Format the response as a simple list with # symbols."""
        
        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.5,
                    max_output_tokens=200,
                )
            )
            
            hashtags = response.text
            
            return {
                "success": True,
                "theme": theme,
                "hashtags": hashtags,
                "count": count
            }
        
        except TimeoutError:
            return {
                "success": False,
                "error": "Request timed out. Please try again.",
                "theme": theme
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "theme": theme
            }
    
    def batch_generate(
        self, 
        themes: List[str], 
        content_type: str = "general_content"
    ) -> List[Dict]:
        """
        Generate content for multiple themes in batch.
        
        Args:
            themes (List[str]): List of themes to generate content for
            content_type (str): Type of content to generate for all themes
        
        Returns:
            List[Dict]: List of generated content for each theme
        """
        results = []
        
        for i, theme in enumerate(themes):
            print(f"Generating content {i+1}/{len(themes)} for theme: {theme}")
            result = self.generate_content(theme, content_type)
            results.append(result)
        
        return results


def main():
    """Example usage of ContentGenerator."""
    try:
        # Initialize generator
        generator = ContentGenerator()
        
        # Example 1: Generate Instagram post
        print("\n" + "="*60)
        print("Example 1: Instagram Post")
        print("="*60)
        result = generator.generate_content(
            theme="sustainable fashion",
            content_type="instagram_post"
        )
        if result["success"]:
            print(result["generated_content"])
        else:
            print(f"Error: {result['error']}")
        
        # Example 2: Generate content for multiple platforms
        print("\n" + "="*60)
        print("Example 2: Multi-Platform Content")
        print("="*60)
        multi_result = generator.generate_multiple_platforms(
            theme="artificial intelligence",
            platforms=["instagram_post", "twitter_post", "linkedin_post"]
        )
        
        if multi_result["success"]:
            for platform, content in multi_result["platforms"].items():
                print(f"\n{platform.upper()}:")
                print(content)
        
        # Example 3: Generate hashtags
        print("\n" + "="*60)
        print("Example 3: Hashtag Generation")
        print("="*60)
        hashtag_result = generator.generate_hashtag_set(
            theme="digital marketing",
            count=8
        )
        if hashtag_result["success"]:
            print(hashtag_result["hashtags"])
        
    except ValueError as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
