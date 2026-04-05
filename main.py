"""
Main entry point for Social Media Content Generator.
Provides an interactive interface for users to generate social media content.
"""

from content_generator import ContentGenerator
from config import Config
import json
from typing import Optional


class InteractiveGenerator:
    """Interactive interface for the Social Media Content Generator."""
    
    CONTENT_TYPES = {
        "1": ("instagram_post", "Instagram Post"),
        "2": ("twitter_post", "Twitter/X Post"),
        "3": ("facebook_post", "Facebook Post"),
        "4": ("linkedin_post", "LinkedIn Post"),
        "5": ("tiktok_caption", "TikTok Caption"),
        "6": ("email_subject", "Email Subject Lines"),
        "7": ("general_content", "General Social Content"),
    }
    
    def __init__(self):
        """Initialize the interactive generator."""
        try:
            self.generator = ContentGenerator()
            print("\n✓ ContentGenerator initialized successfully!")
        except ValueError as e:
            print(f"\n✗ Configuration Error: {e}")
            print("Please set up your API key in the .env file")
            exit(1)
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*60)
        print("SOCIAL MEDIA CONTENT GENERATOR")
        print("="*60)
        print("\nSelect an option:")
        print("\n1. Generate Single Platform Content")
        print("2. Generate Multi-Platform Content")
        print("3. Generate Hashtags")
        print("4. Batch Generate Content")
        print("5. View Content Types")
        print("6. Exit")
        print("\n" + "-"*60)
        return input("Enter your choice (1-6): ").strip()
    
    def display_content_types(self):
        """Display available content types."""
        print("\n" + "-"*60)
        print("AVAILABLE CONTENT TYPES:")
        print("-"*60)
        for key, (_, description) in self.CONTENT_TYPES.items():
            print(f"{key}. {description}")
        print("-"*60)
    
    def generate_single_platform(self):
        """Generate content for a single platform."""
        print("\n" + "-"*60)
        print("SINGLE PLATFORM CONTENT GENERATION")
        print("-"*60)
        
        # Display content types
        self.display_content_types()
        
        # Get user selection
        choice = input("\nSelect content type (1-7): ").strip()
        if choice not in self.CONTENT_TYPES:
            print("✗ Invalid selection. Please try again.")
            return
        
        content_type, description = self.CONTENT_TYPES[choice]
        
        # Get theme
        theme = input(f"\nEnter the theme for {description}: ").strip()
        if not theme:
            print("✗ Theme cannot be empty.")
            return
        
        # Get number of variations
        try:
            variations = int(input("Number of variations (1-3, default 1): ") or "1")
            if variations < 1 or variations > 3:
                print("✗ Please enter a number between 1 and 3.")
                return
        except ValueError:
            print("✗ Invalid input. Using default (1 variation).")
            variations = 1
        
        # Generate content
        print(f"\nGenerating {description} for: '{theme}'...")
        result = self.generator.generate_content(theme, content_type, variations)
        
        if result["success"]:
            print("\n" + "="*60)
            print(f"✓ GENERATED {description.upper()}")
            print("="*60)
            print(result["generated_content"])
            print("="*60)
            
            # Option to save
            self._save_content_prompt(result)
        else:
            print(f"✗ Error: {result.get('error', 'Unknown error')}")
    
    def generate_multi_platform(self):
        """Generate content for multiple platforms."""
        print("\n" + "-"*60)
        print("MULTI-PLATFORM CONTENT GENERATION")
        print("-"*60)
        
        # Get theme
        theme = input("Enter the theme for content generation: ").strip()
        if not theme:
            print("✗ Theme cannot be empty.")
            return
        
        # Default platforms
        platforms = ["instagram_post", "twitter_post", "facebook_post", "linkedin_post"]
        
        print(f"\nGenerating content for multiple platforms: {', '.join(['Instagram', 'Twitter', 'Facebook', 'LinkedIn'])}")
        print(f"Theme: '{theme}'\n")
        
        result = self.generator.generate_multiple_platforms(theme, platforms)
        
        if result["success"]:
            print("\n" + "="*60)
            print("✓ MULTI-PLATFORM CONTENT GENERATED")
            print("="*60)
            
            for platform, content in result["platforms"].items():
                print(f"\n{platform.upper().replace('_', ' ')}:")
                print("-" * 40)
                print(content)
            
            print("\n" + "="*60)
            self._save_content_prompt(result)
        else:
            print("✗ Error generating multi-platform content")
    
    def generate_hashtags(self):
        """Generate hashtags for a theme."""
        print("\n" + "-"*60)
        print("HASHTAG GENERATION")
        print("-"*60)
        
        theme = input("Enter the theme for hashtag generation: ").strip()
        if not theme:
            print("✗ Theme cannot be empty.")
            return
        
        try:
            count = int(input("Number of hashtags to generate (default 10): ") or "10")
            if count < 5 or count > 30:
                print("✗ Please enter a number between 5 and 30.")
                return
        except ValueError:
            print("✗ Invalid input. Using default (10 hashtags).")
            count = 10
        
        print(f"\nGenerating {count} hashtags for: '{theme}'...")
        result = self.generator.generate_hashtag_set(theme, count)
        
        if result["success"]:
            print("\n" + "="*60)
            print("✓ GENERATED HASHTAGS")
            print("="*60)
            print(result["hashtags"])
            print("="*60)
            self._save_content_prompt(result)
        else:
            print(f"✗ Error: {result.get('error', 'Unknown error')}")
    
    def batch_generate(self):
        """Batch generate content for multiple themes."""
        print("\n" + "-"*60)
        print("BATCH CONTENT GENERATION")
        print("-"*60)
        
        # Get themes
        print("Enter themes (separated by commas):")
        print("Example: social media, digital marketing, AI technology")
        themes_input = input("\nThemes: ").strip()
        
        themes = [t.strip() for t in themes_input.split(",") if t.strip()]
        if not themes:
            print("✗ No themes provided.")
            return
        
        # Get content type
        self.display_content_types()
        choice = input("\nSelect content type (1-7): ").strip()
        
        if choice not in self.CONTENT_TYPES:
            print("✗ Invalid selection.")
            return
        
        content_type, description = self.CONTENT_TYPES[choice]
        
        print(f"\nGenerating {description} for {len(themes)} themes...")
        print("-" * 40)
        
        results = self.generator.batch_generate(themes, content_type)
        
        print("\n" + "="*60)
        print("✓ BATCH GENERATION COMPLETE")
        print("="*60)
        
        for i, result in enumerate(results, 1):
            if result["success"]:
                print(f"\n{i}. Theme: {result['theme']}")
                print("-" * 40)
                print(result["generated_content"])
            else:
                print(f"\n{i}. Theme: {result['theme']} - Error: {result.get('error')}")
        
        print("\n" + "="*60)
        self._save_content_prompt(results)
    
    def _save_content_prompt(self, content_data):
        """Prompt user to save generated content."""
        save = input("\nSave content to file? (y/n): ").strip().lower()
        if save == "y":
            filename = input("Enter filename (without extension): ").strip()
            if filename:
                try:
                    self._save_to_file(filename, content_data)
                    print(f"✓ Content saved to {filename}.json")
                except Exception as e:
                    print(f"✗ Error saving file: {e}")
    
    def _save_to_file(self, filename: str, content_data):
        """Save content to a JSON file."""
        filepath = f"{filename}.json"
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(content_data, f, indent=2, ensure_ascii=False)
    
    def run(self):
        """Run the interactive generator."""
        while True:
            choice = self.display_menu()
            
            if choice == "1":
                self.generate_single_platform()
            elif choice == "2":
                self.generate_multi_platform()
            elif choice == "3":
                self.generate_hashtags()
            elif choice == "4":
                self.batch_generate()
            elif choice == "5":
                self.display_content_types()
            elif choice == "6":
                print("\n✓ Thank you for using Social Media Content Generator!")
                print("Goodbye!\n")
                break
            else:
                print("✗ Invalid choice. Please try again.")


def main():
    """Main entry point."""
    try:
        generator = InteractiveGenerator()
        generator.run()
    except KeyboardInterrupt:
        print("\n\n✗ Program interrupted by user.")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")


if __name__ == "__main__":
    main()
