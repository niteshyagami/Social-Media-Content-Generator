# Social Media Content Generator

A powerful tool that leverages Generative AI to create engaging social media content, captions, and hashtags for multiple platforms.

## 🎯 Features

- **Multi-Platform Support**: Generate optimized content for Instagram, Twitter, Facebook, LinkedIn, TikTok, and Email
- **Content Variations**: Create multiple versions of content for A/B testing
- **Hashtag Generation**: Generate trending and relevant hashtags for any topic
- **Batch Processing**: Generate content for multiple themes at once
- **Interactive Interface**: User-friendly menu-driven interface
- **Content Saving**: Export generated content to JSON files
- **Clean & Documented Code**: Well-commented codebase for easy understanding

## 📋 Prerequisites

- Python 3.8 or higher
- Google Generative AI API key (free with Google Cloud account)
- Internet connection for API calls

## 🚀 Installation

### 1. Clone/Extract the Project

Navigate to the project directory:
```bash
cd "Social Media Content Generator"
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Key

#### Option A: Using Google Generative AI (Recommended)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key

#### Option B: Copy .env File

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` and add your API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## 📖 Usage

### Interactive Mode (Recommended)

Run the main script:
```bash
python main.py
```

The interactive menu will guide you through:
1. **Generate Single Platform Content** - Create content for one social media platform
2. **Generate Multi-Platform Content** - Generate optimized content for multiple platforms at once
3. **Generate Hashtags** - Create relevant hashtags for your theme
4. **Batch Generate Content** - Process multiple themes in one run
5. **View Content Types** - See all available content generation options

### Direct Python Usage

```python
from content_generator import ContentGenerator

# Initialize the generator
generator = ContentGenerator()

# Example 1: Generate Instagram content
result = generator.generate_content(
    theme="sustainable fashion",
    content_type="instagram_post"
)

# Example 2: Generate for multiple platforms
multi_result = generator.generate_multiple_platforms(
    theme="artificial intelligence",
    platforms=["instagram_post", "twitter_post", "linkedin_post"]
)

# Example 3: Generate hashtags
hashtags = generator.generate_hashtag_set(
    theme="digital marketing",
    count=10
)

# Example 4: Batch processing
results = generator.batch_generate(
    themes=["social media", "digital marketing", "AI"],
    content_type="general_content"
)
```

## 📱 Available Content Types

| Code | Content Type | Platform | Best For |
|------|--------------|----------|----------|
| 1 | Instagram Post | Instagram | Visual-focused content with captions & hashtags |
| 2 | Twitter/X Post | Twitter/X | Short, punchy messages (280 chars) |
| 3 | Facebook Post | Facebook | Longer-form content with engagement hooks |
| 4 | LinkedIn Post | LinkedIn | Professional & industry insights |
| 5 | TikTok Caption | TikTok | Trendy, youth-friendly, playful content |
| 6 | Email Subject Lines | Email | Compelling subject lines for newsletters |
| 7 | General Social Content | Multiple | All-purpose social media content |

## 📁 Project Structure

```
Social Media Content Generator/
├── main.py                 # Interactive entry point
├── content_generator.py    # Core AI content generation logic
├── config.py               # Configuration and settings
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── .env                    # Your actual API keys (create this file)
└── README.md              # This file
```

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Temperature (0 = deterministic, 1 = creative)
TEMPERATURE = 0.7

# Maximum output length
MAX_TOKENS = 500

# Add your own custom prompts
PROMPTS = {...}
```

## 🔧 Advanced Features

### Custom Temperature Settings

Lower values (0.3-0.5) produce more consistent output:
```bash
MODEL_TEMPERATURE=0.3
```

Higher values (0.7-1.0) produce more creative output:
```bash
MODEL_TEMPERATURE=1.0
```

### Add Custom Prompts

Edit `config.py` and add to the `PROMPTS` dictionary:
```python
"custom_content": """Your custom prompt here with {theme} placeholder"""
```

## 💡 Tips for Best Results

1. **Be Specific**: More detailed themes produce better content
   - ❌ Bad: "technology"
   - ✅ Good: "sustainable technology solutions for small businesses"

2. **Use Multiple Variations**: Generate 2-3 versions to find the best one

3. **Hashtag Count**: 
   - Instagram: 15-30 hashtags
   - Twitter: 1-2 hashtags
   - LinkedIn: 3-5 hashtags

4. **Review & Edit**: Always review generated content for brand voice and accuracy

5. **Theme Combinations**: Try combining multiple themes for unique content
   - "sustainable fashion + technology innovation"

## 🛠️ Troubleshooting

### Error: "GOOGLE_API_KEY is not set"
- Solution: Make sure you've created a `.env` file with your API key
- Check that `AI_MODEL=google` is set in your `.env`

### Error: "API quota exceeded"
- Google provides free tier with rate limits
- Solution: Implement delays between requests or upgrade to paid tier

### Content quality is low
- Try adjusting `TEMPERATURE` in `.env`
- Provide more specific themes
- Try different content types

### Special characters or emoji issues
- The tool handles UTF-8 encoding
- Make sure your terminal supports Unicode output

## 📊 Example Output

### Instagram Post Output:
```
Caption: Transform your wardrobe sustainably! 🌿 Discover timeless pieces that last and give back. 
Hashtags: #SustainableFashion #EcoFriendly #ConsciousStyle #FashionForGood
```

### Multi-Platform Output:
```
INSTAGRAM:
Your engaging caption here with relevant hashtags

TWITTER:
280-character tweet with 1-2 hashtags

FACEBOOK:
Longer-form content with hook and CTA

LINKEDIN:
Professional insights and value proposition
```

## 📝 Output Formats

Content can be exported as:
- **JSON**: Structured data format for integration with other tools
- **Console**: Immediate viewing in the application
- **Text Files**: Copy-paste ready content

## 🔐 Security Notes

- Never commit your `.env` file to version control
- Keep your API key confidential
- Rotate API keys periodically
- Don't share generated content samples if they contain sensitive information

## 🚀 Performance Tips

- Batch generate during off-peak hours for faster processing
- Cache frequently used themes
- Use appropriate temperature settings (lower = faster)
- Consider rate limiting for batch operations

## 📄 License

This project is open-source and available for educational and commercial use.

## 🤝 Contributing

Feel free to:
- Add new content types
- Improve prompt engineering
- Support additional AI models
- Enhance the UI/UX

## 📧 Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify your `.env` configuration
3. Review generated content structure in README

## 🎓 Learning Resources

- [Google Generative AI Documentation](https://ai.google.dev/docs)
- [Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [Social Media Content Strategy](https://www.hootsuite.com/blog/social-media-content-strategy)

---

**Happy Content Creating! 🚀**

*Last Updated: April 2026*
