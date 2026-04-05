"""
Examples module demonstrating various use cases for the Social Media Content Generator.
Run this file to see practical examples of the tool in action.
"""

from content_generator import ContentGenerator
from config import Config
import json


def example_1_basic_instagram_content():
    """Example 1: Generate a basic Instagram post."""
    print("\n" + "="*70)
    print("EXAMPLE 1: Generate Instagram Post")
    print("="*70)
    
    generator = ContentGenerator()
    
    # Generate Instagram content
    result = generator.generate_content(
        theme="eco-friendly coffee brewing",
        content_type="instagram_post"
    )
    
    if result["success"]:
        print("\nGenerated Instagram Content:")
        print("-"*70)
        print(result["generated_content"])
    else:
        print(f"Error: {result['error']}")


def example_2_multiple_platforms():
    """Example 2: Generate content for multiple platforms."""
    print("\n" + "="*70)
    print("EXAMPLE 2: Multi-Platform Content Generation")
    print("="*70)
    
    generator = ContentGenerator()
    theme = "AI in healthcare"
    
    # Generate for multiple platforms
    result = generator.generate_multiple_platforms(
        theme=theme,
        platforms=["instagram_post", "twitter_post", "linkedin_post", "facebook_post"]
    )
    
    if result["success"]:
        print(f"\nGenerating content for theme: '{theme}'")
        print("-"*70)
        
        for platform, content in result["platforms"].items():
            print(f"\n📱 {platform.upper().replace('_', ' ')}:")
            print(content)
            print("-"*70)
    else:
        print(f"Error: {result['error']}")


def example_3_hashtag_generation():
    """Example 3: Generate relevant hashtags."""
    print("\n" + "="*70)
    print("EXAMPLE 3: Hashtag Generation")
    print("="*70)
    
    generator = ContentGenerator()
    theme = "digital transformation"
    
    # Generate hashtags
    result = generator.generate_hashtag_set(
        theme=theme,
        count=15
    )
    
    if result["success"]:
        print(f"\nGenerated hashtags for: '{theme}'")
        print("-"*70)
        print(result["hashtags"])
    else:
        print(f"Error: {result['error']}")


def example_4_multiple_variations():
    """Example 4: Generate multiple variations of content."""
    print("\n" + "="*70)
    print("EXAMPLE 4: Multiple Content Variations")
    print("="*70)
    
    generator = ContentGenerator()
    theme = "summer collection launch"
    
    # Generate 3 variations
    result = generator.generate_content(
        theme=theme,
        content_type="instagram_post",
        num_variations=3
    )
    
    if result["success"]:
        print(f"\nGenerated {result['variations']} variations for Instagram")
        print(f"Theme: '{theme}'")
        print("-"*70)
        print(result["generated_content"])
    else:
        print(f"Error: {result['error']}")


def example_5_batch_processing():
    """Example 5: Batch generate content for multiple themes."""
    print("\n" + "="*70)
    print("EXAMPLE 5: Batch Content Generation")
    print("="*70)
    
    generator = ContentGenerator()
    
    # Multiple themes to process
    themes = [
        "machine learning applications",
        "sustainable business practices",
        "customer service excellence"
    ]
    
    print(f"\nGenerating content for {len(themes)} themes...")
    print("-"*70)
    
    results = generator.batch_generate(
        themes=themes,
        content_type="linkedin_post"
    )
    
    for i, result in enumerate(results, 1):
        if result["success"]:
            print(f"\n✓ Theme {i}: {result['theme']}")
            print(result["generated_content"][:200] + "..." if len(result["generated_content"]) > 200 else result["generated_content"])
        else:
            print(f"\n✗ Theme {i}: Error - {result.get('error')}")


def example_6_email_subject_lines():
    """Example 6: Generate email subject lines."""
    print("\n" + "="*70)
    print("EXAMPLE 6: Email Subject Line Generation")
    print("="*70)
    
    generator = ContentGenerator()
    theme = "new product launch webinar"
    
    # Generate email subject lines
    result = generator.generate_content(
        theme=theme,
        content_type="email_subject"
    )
    
    if result["success"]:
        print(f"\nGenerated email subject lines for: '{theme}'")
        print("-"*70)
        print(result["generated_content"])
    else:
        print(f"Error: {result['error']}")


def example_7_tiktok_content():
    """Example 7: Generate TikTok captions."""
    print("\n" + "="*70)
    print("EXAMPLE 7: TikTok Caption Generation")
    print("="*70)
    
    generator = ContentGenerator()
    theme = "fitness motivation challenge"
    
    # Generate TikTok content
    result = generator.generate_content(
        theme=theme,
        content_type="tiktok_caption"
    )
    
    if result["success"]:
        print(f"\nGenerated TikTok caption for: '{theme}'")
        print("-"*70)
        print(result["generated_content"])
    else:
        print(f"Error: {result['error']}")


def example_8_save_results():
    """Example 8: Generate content and save to file."""
    print("\n" + "="*70)
    print("EXAMPLE 8: Generate and Save Results")
    print("="*70)
    
    generator = ContentGenerator()
    theme = "remote work productivity tips"
    
    # Generate multi-platform content
    result = generator.generate_multiple_platforms(
        theme=theme,
        platforms=["twitter_post", "linkedin_post"]
    )
    
    # Save to file
    if result["success"]:
        filename = "generated_content_example"
        filepath = f"{filename}.json"
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Content saved to: {filepath}")
        print("\nGenerated content:")
        print("-"*70)
        
        for platform, content in result["platforms"].items():
            print(f"\n{platform.upper()}:")
            print(content)


def example_9_custom_temperature():
    """Example 9: Control creativity with temperature settings."""
    print("\n" + "="*70)
    print("EXAMPLE 9: Temperature Control (Creativity Level)")
    print("="*70)
    
    generator = ContentGenerator()
    theme = "coffee shop opening"
    
    # Show current temperature setting
    print(f"\nCurrent temperature setting: {Config.TEMPERATURE}")
    print("(Lower = more consistent, Higher = more creative)")
    print("\nNote: To change temperature, edit .env file:")
    print("  MODEL_TEMPERATURE=0.3  (conservative)")
    print("  MODEL_TEMPERATURE=0.7  (balanced)")
    print("  MODEL_TEMPERATURE=1.0  (creative)")
    print("-"*70)
    
    # Generate with current settings
    result = generator.generate_content(
        theme=theme,
        content_type="facebook_post"
    )
    
    if result["success"]:
        print(f"\nGenerated Facebook content (temperature: {Config.TEMPERATURE}):")
        print(result["generated_content"])


def example_10_all_content_types():
    """Example 10: Demonstrate all available content types."""
    print("\n" + "="*70)
    print("EXAMPLE 10: All Content Types Showcase")
    print("="*70)
    
    generator = ContentGenerator()
    theme = "digital wellness"
    
    content_types = [
        ("instagram_post", "Instagram"),
        ("twitter_post", "Twitter"),
        ("facebook_post", "Facebook"),
        ("linkedin_post", "LinkedIn"),
        ("tiktok_caption", "TikTok"),
        ("email_subject", "Email"),
        ("general_content", "General")
    ]
    
    print(f"\nGenerating all content types for theme: '{theme}'")
    print("-"*70)
    
    for content_type, label in content_types:
        result = generator.generate_content(theme, content_type)
        
        if result["success"]:
            print(f"\n✓ {label}:")
            content_preview = result["generated_content"][:100] + "..." if len(result["generated_content"]) > 100 else result["generated_content"]
            print(f"  {content_preview}")
        else:
            print(f"\n✗ {label}: Error - {result.get('error')}")


def main():
    """Run all examples."""
    try:
        print("\n" + "█"*70)
        print("█  SOCIAL MEDIA CONTENT GENERATOR - EXAMPLES")
        print("█"*70)
        
        print("\nRunning examples...")
        
        # Run examples
        example_1_basic_instagram_content()
        example_2_multiple_platforms()
        example_3_hashtag_generation()
        example_4_multiple_variations()
        example_5_batch_processing()
        example_6_email_subject_lines()
        example_7_tiktok_content()
        example_8_save_results()
        example_9_custom_temperature()
        example_10_all_content_types()
        
        print("\n" + "█"*70)
        print("█  ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("█"*70)
        print("\nFor interactive use, run: python main.py")
        print("For configuration help, see: README.md\n")
        
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("\nPlease follow these steps:")
        print("1. Copy .env.example to .env")
        print("2. Add your Google API key to .env")
        print("3. Re-run this script")
    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
