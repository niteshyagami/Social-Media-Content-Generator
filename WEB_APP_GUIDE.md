# Web Application Guide

The Social Media Content Generator includes a modern web application interface for easy access and content generation.

## 🚀 Starting the Web App

### 1. Update Dependencies

If this is your first time, install Flask:

```bash
pip install -r requirements.txt
```

### 2. Run the Web App

```bash
python webapp.py
```

You'll see:
```
🚀 Social Media Content Generator Web App
📍 Starting server on http://localhost:5000
```

### 3. Open in Browser

Click or copy: **http://localhost:5000**

## 📱 Features

### Single Platform Content
Generate optimized content for one social media platform:
- Choose a platform (Instagram, Twitter, Facebook, LinkedIn, TikTok, Email)
- Enter your theme
- Select number of variations (1-3)
- Click "Generate Content"

### Multi-Platform Content
Create content for multiple platforms at once:
- Enter your theme
- Select which platforms to include
- Get optimized content for each platform simultaneously

### Hashtag Generator
Create relevant hashtags for any topic:
- Enter your theme
- Choose number of hashtags (5-30)
- Get trending and niche hashtags

### Batch Generate
Process multiple themes in one go:
- Enter themes (comma-separated or line-by-line)
- Choose content type
- Generate all at once

## 💾 Exporting Content

All generated content can be:
- **Copied** - Click the copy button to copy to clipboard
- **Downloaded** - Save as JSON file for later use

## 🎨 Web Interface Features

✨ **Modern Design**
- Clean, intuitive layout
- Responsive design (works on mobile, tablet, desktop)
- Dark gradient background

🎯 **Easy Navigation**
- Tab-based interface for different modes
- Clear form labels and instructions
- Real-time loading feedback

💬 **Notifications**
- Success/error messages
- Copy-to-clipboard feedback
- Generation status updates

## 🔧 Advanced Configuration

### Development Mode

The webapp runs in debug mode by default:
- Auto-reloads on code changes
- Detailed error messages
- Access to debug toolbar (if installed)

### Production Mode

To disable debug mode (for production):

Edit `webapp.py` and change:
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Configuration

All settings from `.env` are used:
- API key from `GOOGLE_API_KEY`
- Model type from `AI_MODEL`
- Temperature from `MODEL_TEMPERATURE`

## 📊 API Endpoints

The web app also provides REST API endpoints:

### Generate Content
```
POST /api/generate
{
    "theme": "sustainable fashion",
    "content_type": "instagram_post",
    "variations": 1
}
```

### Multi-Platform
```
POST /api/multi-platform
{
    "theme": "AI technology",
    "platforms": ["instagram_post", "twitter_post", "linkedin_post"]
}
```

### Hashtags
```
POST /api/hashtags
{
    "theme": "digital marketing",
    "count": 10
}
```

### Batch Generate
```
POST /api/batch
{
    "themes": ["social media", "digital marketing"],
    "content_type": "general_content"
}
```

### Get Content Types
```
GET /api/content-types
```

### Get Platforms
```
GET /api/platforms
```

### Health Check
```
GET /api/health
```

## 🌐 Sharing Your Web App

### Share Locally
If you want to access from another computer on your network:

Edit `webapp.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

Then access: `http://your_computer_ip:5000`

### Deploy Online
To deploy the web app online:

1. **Heroku**
   - Add `Procfile`: `web: python webapp.py`
   - Deploy with Git

2. **AWS/Azure/GCP**
   - Use cloud deployment services
   - Ensure API key is in environment variables

3. **Docker**
   - Create a Dockerfile
   - Build and run container

## 🔒 Security Notes

- Keep your `.env` file with API keys safe
- Don't share your API key publicly
- For public deployment, use environment variables
- Implement authentication if exposing publicly

## ⚡ Performance Tips

- Run on a fast internet connection
- Use reasonable batch sizes (5-10 themes)
- Wait 5 seconds between large batch operations (API rate limits)

## 📱 Browser Compatibility

- Chrome/Chromium ✅
- Firefox ✅
- Safari ✅
- Edge ✅
- Mobile browsers ✅

## 🐛 Troubleshooting

### "Cannot connect to localhost:5000"
- Make sure the app is running
- Try refreshing the page
- Check for port conflicts

### "API Key error"
- Verify `.env` file exists
- Check your API key is correct
- Restart the app after updating `.env`

### "Rate limit exceeded"
- Google API has free tier limits (5 requests/minute)
- Wait a few seconds and try again
- Consider upgrading to paid tier

### "Page loads but nothing happens"
- Check browser console for errors (F12)
- Verify `/api/generate` returns 200 status
- Check network tab for failed requests

## 📞 Support

For issues:
1. Check API key configuration
2. Test with examples.py
3. Check network requests in browser (F12)
4. Review error messages in terminal

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Google Generative AI](https://ai.google.dev/)

---

**Enjoy creating amazing content with the web interface! 🎉**
