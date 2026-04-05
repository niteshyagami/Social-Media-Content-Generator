# Social Media Content Generator - Setup Guide

Complete step-by-step guide to get the Social Media Content Generator up and running.

## 📋 System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Internet**: Required for API calls
- **RAM**: 256 MB minimum
- **Disk Space**: 50 MB for project + dependencies

## ✅ Step 1: Get Your API Key

### Option A: Google Generative AI (Recommended)

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account (create one if needed)
3. Click **"Create API Key"** button
4. Select **"Create API key in new project"**
5. Copy the generated API key (it looks like: `AIzaXXXXXXXXXXXXXXX...`)
6. ✓ Keep this key safe - you'll need it in the next step

### Option B: Alternative Services

While this guide uses Google Generative AI, you can also use:
- **OpenAI API**: https://platform.openai.com/api-keys
- **Anthropic Claude**: https://console.anthropic.com/
- **HuggingFace**: https://huggingface.co/

(Note: OpenAI requires setting up a billing account)

## 🔧 Step 2: Set Up the Environment

### Windows Users:

#### 2.1 Open PowerShell or Command Prompt

1. Press `Win + R`
2. Type `powershell` or `cmd`
3. Press Enter

#### 2.2 Navigate to Project Directory

```powershell
cd "Desktop\Social Media Content Generator"
```

#### 2.3 Create Virtual Environment

```powershell
python -m venv venv
```

If you get an error, try:
```powershell
python3 -m venv venv
```

#### 2.4 Activate Virtual Environment

```powershell
venv\Scripts\Activate.ps1
```

If you get a security error, run PowerShell as Administrator and type:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again.

### macOS/Linux Users:

#### 2.1 Open Terminal

Press `Cmd + Space` and type `terminal`

#### 2.2 Navigate to Project Directory

```bash
cd ~/Desktop/"Social Media Content Generator"
```

#### 2.3 Create Virtual Environment

```bash
python3 -m venv venv
```

#### 2.4 Activate Virtual Environment

```bash
source venv/bin/activate
```

## 📦 Step 3: Install Dependencies

With virtual environment activated, run:

```bash
pip install -r requirements.txt
```

This will install:
- `google-generativeai` - Google Generative AI SDK
- `python-dotenv` - Environment variable management

Wait for installation to complete.

## 🔑 Step 4: Configure API Key

### 4.1 Copy Environment Template

**Windows (PowerShell):**
```powershell
Copy-Item .env.example .env
```

**Windows (Command Prompt):**
```cmd
copy .env.example .env
```

**macOS/Linux:**
```bash
cp .env.example .env
```

### 4.2 Edit the .env File

Open `.env` file with a text editor (Notepad, VS Code, etc.)

Find this line:
```
GOOGLE_API_KEY=your_google_api_key_here
```

Replace it with your actual API key:
```
GOOGLE_API_KEY=AIzaSyA1b2c3D4e5F6g7H8i9J0...
```

**Important**: 
- Do NOT share this file or your API key
- Do NOT commit this to version control
- Keep your key confidential

### 4.3 Save the File

Save and close the file.

## 🧪 Step 5: Verify Installation

### Test 1: Check Python Version

```bash
python --version
```

Expected: Python 3.8 or higher

### Test 2: Check Dependencies

```bash
pip list
```

Should show:
- google-generativeai
- python-dotenv

### Test 3: Run Configuration Check

```bash
python config.py
```

Expected output:
```
Configuration loaded successfully!
AI Model: google
Temperature: 0.7
```

## 🚀 Step 6: Run Examples

Test the setup by running examples:

```bash
python examples.py
```

This will generate several pieces of sample content and demonstrate all features.

## 📖 Step 7: Start Interactive Mode

Once everything works, run the main application:

```bash
python main.py
```

Follow the interactive menu to generate content!

## 🐛 Troubleshooting

### Problem: Python not found

**Windows:**
```powershell
# Try python3
python3 main.py

# Or add Python to PATH, then restart terminal
```

**macOS/Linux:**
```bash
python3 main.py
```

### Problem: "GOOGLE_API_KEY is not set"

**Solution:**
1. Make sure `.env` file exists in the project directory
2. Verify the API key is correctly pasted
3. Check for trailing spaces or quotes around the key
4. Restart your terminal/activate virtual environment again

### Problem: "ModuleNotFoundError: No module named 'google'"

**Solution:**
```bash
# Verify virtual environment is activated
# Then reinstall packages
pip install --upgrade google-generativeai python-dotenv
```

### Problem: API returns "PERMISSION_DENIED"

**Solution:**
1. Check your API key is valid
2. Verify the key has Generative AI API permissions
3. Check your Google Cloud project has the API enabled
4. Try generating a new API key

### Problem: Slow responses or timeouts

**Solution:**
- This is normal sometimes due to API server load
- Try again after a few seconds
- Check your internet connection
- Reduce number of variations in batch operations

### Problem: Terminal/PowerShell issues on Windows

**Solution:**
If PowerShell won't activate the virtual environment:

1. Open Command Prompt (cmd) instead of PowerShell
2. Run:
```cmd
venv\Scripts\activate.bat
```

## 🎓 Next Steps

1. **Read the README.md** for detailed feature documentation
2. **Try the interactive mode** with: `python main.py`
3. **Experiment with different themes** and content types
4. **Customize the prompts** in `config.py` for your brand
5. **Save your generated content** for use on social media

## ⚙️ Optional: Performance Tuning

### Faster Responses:
Edit `.env`:
```
MODEL_TEMPERATURE=0.3
```

### More Creative Output:
Edit `.env`:
```
MODEL_TEMPERATURE=0.9
```

### Batch Processing Optimization:

In `main.py`, batch operations now show progress.
Consider running during off-peak hours for faster processing.

## 📞 Getting Help

### Common Questions:

**Q: Is the API free?**
A: Google provides a free tier with rate limits. See pricing at makersuite.google.com

**Q: Can I use this commercially?**
A: Yes, based on your API subscription terms.

**Q: How do I update the code?**
A: The project uses standard Python, so you can edit files directly.

**Q: Can I add new content types?**
A: Yes! Edit `config.py` and add to the `PROMPTS` dictionary.

## ✨ You're All Set!

Your Social Media Content Generator is now ready to use.

```bash
python main.py
```

Start generating amazing social media content! 🚀

---

**Need more help?** Check the README.md file for detailed documentation.
