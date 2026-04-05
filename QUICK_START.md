# Social Media Content Generator - Quick Start

## 🚀 Get Started in 3 Minutes

### 1. **Get Your API Key** (1 minute)
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Click "Create API Key"
   - Copy your key

### 2. **Configure the Project** (1 minute)
   ```bash
   # Copy the example config
   cp .env.example .env
   
   # Edit .env and paste your API key:
   # GOOGLE_API_KEY=your_key_here
   ```

### 3. **Install & Run** (1 minute)
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   
   # Run the tool
   python main.py
   ```

---

## 📁 Project Files

```
├── main.py                    ← Run this for interactive mode
├── examples.py                ← Run this to see demos
├── content_generator.py       ← Core AI engine
├── config.py                  ← Settings & prompts
├── tests.py                   ← Unit tests
├── requirements.txt           ← Dependencies
├── .env.example              ← Config template
├── README.md                 ← Full documentation
├── SETUP_GUIDE.md            ← Detailed setup
└── QUICK_START.md            ← This file
```

---

## 💡 Quick Examples

### Interactive Mode
```bash
python main.py
```

### See Demos
```bash
python examples.py
```

### Python Code
```python
from content_generator import ContentGenerator

generator = ContentGenerator()

# Generate Instagram post
result = generator.generate_content(
    theme="sustainable fashion",
    content_type="instagram_post"
)
print(result["generated_content"])
```

---

## 🎯 Main Features

| Feature | Command |
|---------|---------|
| **Single Platform** | Choose platform in menu → Enter theme |
| **Multi-Platform** | Option 2 → Enter theme (generates for all platforms) |
| **Hashtags** | Option 3 → Enter theme and count |
| **Batch Process** | Option 4 → Enter multiple themes separated by commas |

---

## 📱 Supported Platforms

- Instagram (with captions & hashtags)
- Twitter/X (280 character max)
- Facebook (longer form)
- LinkedIn (professional)
- TikTok (trendy & fun)
- Email (subject lines)
- General (multi-purpose)

---

## ⚙️ Customize

### Change Creativity Level
Edit `.env`:
```
MODEL_TEMPERATURE=0.3   # Conservative
MODEL_TEMPERATURE=0.7   # Balanced (default)
MODEL_TEMPERATURE=1.0   # Creative
```

### Add Custom Prompts
Edit `config.py` → Add to `PROMPTS` dictionary:
```python
"my_platform": """Your custom prompt with {theme}"""
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "API key not set" | Edit `.env` with your API key |
| "Module not found" | Run `pip install -r requirements.txt` |
| "Permission denied" | Check your API key is valid |
| Slow responses | Normal - wait or try again later |

---

## 📊 Example Output

**Instagram Caption:**
> Transform your wardrobe sustainably! 🌿 Discover timeless pieces that last. #SustainableFashion #EcoFriendly

**Twitter Post:**
> Just shipped our latest AI model 🚀 It's faster, smarter, and more accessible. Try it today! #AI #ML

**LinkedIn Post:**
> Today marks a milestone in our digital transformation journey... [professional long-form content continues]

---

## 🔐 Security

- Protect your `.env` file - don't share it
- Never commit `.env` to version control
- Keep your API key confidential

---

## 💬 Common Use Cases

### 1. **Content Calendar Planning**
```bash
# Generate for multiple themes
python main.py → Option 4 → Batch generate
```

### 2. **Platform-Specific Content**
```bash
# Generate optimized for each platform
python main.py → Option 2 → Multi-platform
```

### 3. **Hashtag Research**
```bash
# Get trending hashtags
python main.py → Option 3 → Generate hashtags
```

### 4. **Email Campaign**
```bash
# Create compelling subject lines
python main.py → Option 1 → Email Subject → Generate 3 variations
```

---

## 📈 Tips for Best Results

✅ **Be specific**: "eco-friendly coffee brewing in Japan" → Better than "coffee"
✅ **Use variations**: Generate 2-3 versions and pick the best
✅ **Mix platforms**: Different platforms need different tones
✅ **Save results**: Export to JSON for easy integration

---

## 📚 Learn More

- Full docs: See `README.md`
- Setup help: See `SETUP_GUIDE.md`
- Examples: `python examples.py`

---

## 🎓 What You Can Do

After setup, you can:
- ✅ Generate engaging social media posts
- ✅ Create platform-specific content
- ✅ Generate relevant hashtags
- ✅ Batch process multiple themes
- ✅ Export content as JSON
- ✅ A/B test different variations

---

## ⭐ Next Steps

1. **Run examples**: `python examples.py`
2. **Try interactive**: `python main.py`
3. **Customize for your brand** in `config.py`
4. **Integrate into your workflow**

---

**Happy creating! 🚀**

For questions, see `README.md` or `SETUP_GUIDE.md`

*Last Updated: April 2026*
