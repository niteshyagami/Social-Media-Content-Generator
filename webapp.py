"""
Flask web application for Social Media Content Generator.
Provides a user-friendly web interface for content generation.
"""

from flask import Flask, render_template, request, jsonify, send_file
from content_generator import ContentGenerator
from config import Config
import json
from io import StringIO
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize the content generator
try:
    generator = ContentGenerator()
except ValueError as e:
    print(f"Warning: {e}")
    generator = None


@app.route('/')
def index():
    """Home page."""
    return render_template('index.html')


@app.route('/api/generate', methods=['POST'])
def generate_content():
    """API endpoint for generating content."""
    try:
        data = request.json
        theme = data.get('theme', '').strip()
        content_type = data.get('content_type', 'general_content')
        variations = int(data.get('variations', 1))
        
        if not theme:
            return jsonify({'success': False, 'error': 'Theme is required'}), 400
        
        if not generator:
            return jsonify({'success': False, 'error': 'Generator not configured'}), 500
        
        # Validate variations
        variations = max(1, min(variations, 3))
        
        result = generator.generate_content(theme, content_type, variations)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/multi-platform', methods=['POST'])
def multi_platform():
    """API endpoint for multi-platform content generation."""
    try:
        data = request.json
        theme = data.get('theme', '').strip()
        platforms = data.get('platforms', ['instagram_post', 'twitter_post', 'facebook_post', 'linkedin_post'])
        
        if not theme:
            return jsonify({'success': False, 'error': 'Theme is required'}), 400
        
        if not generator:
            return jsonify({'success': False, 'error': 'Generator not configured'}), 500
        
        result = generator.generate_multiple_platforms(theme, platforms)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/hashtags', methods=['POST'])
def generate_hashtags():
    """API endpoint for hashtag generation."""
    try:
        data = request.json
        theme = data.get('theme', '').strip()
        count = int(data.get('count', 10))
        
        if not theme:
            return jsonify({'success': False, 'error': 'Theme is required'}), 400
        
        if not generator:
            return jsonify({'success': False, 'error': 'Generator not configured'}), 500
        
        # Validate count
        count = max(5, min(count, 30))
        
        result = generator.generate_hashtag_set(theme, count)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/batch', methods=['POST'])
def batch_generate():
    """API endpoint for batch content generation."""
    try:
        data = request.json
        themes = data.get('themes', [])
        content_type = data.get('content_type', 'general_content')
        
        if not themes:
            return jsonify({'success': False, 'error': 'At least one theme is required'}), 400
        
        if not generator:
            return jsonify({'success': False, 'error': 'Generator not configured'}), 500
        
        results = generator.batch_generate(themes, content_type)
        
        return jsonify({
            'success': True,
            'total': len(results),
            'results': results
        })
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/content-types', methods=['GET'])
def get_content_types():
    """Get available content types."""
    content_types = [
        {'id': 'instagram_post', 'name': 'Instagram Post', 'description': 'Optimized for Instagram with captions and hashtags'},
        {'id': 'twitter_post', 'name': 'Twitter/X Post', 'description': '280 character limited posts'},
        {'id': 'facebook_post', 'name': 'Facebook Post', 'description': 'Longer-form content for Facebook'},
        {'id': 'linkedin_post', 'name': 'LinkedIn Post', 'description': 'Professional content for LinkedIn'},
        {'id': 'tiktok_caption', 'name': 'TikTok Caption', 'description': 'Trendy, youth-friendly captions'},
        {'id': 'email_subject', 'name': 'Email Subject Lines', 'description': 'Compelling email subject lines'},
        {'id': 'general_content', 'name': 'General Content', 'description': 'All-purpose social media content'},
    ]
    return jsonify(content_types)


@app.route('/api/platforms', methods=['GET'])
def get_platforms():
    """Get available platforms."""
    platforms = [
        {'id': 'instagram_post', 'name': 'Instagram'},
        {'id': 'twitter_post', 'name': 'Twitter/X'},
        {'id': 'facebook_post', 'name': 'Facebook'},
        {'id': 'linkedin_post', 'name': 'LinkedIn'},
        {'id': 'tiktok_caption', 'name': 'TikTok'},
        {'id': 'email_subject', 'name': 'Email'},
    ]
    return jsonify(platforms)


@app.route('/api/export', methods=['POST'])
def export_content():
    """Export content as JSON."""
    try:
        data = request.json
        filename = data.get('filename', 'generated_content.json')
        content = data.get('content', {})
        
        # Ensure filename is safe
        filename = ''.join(c for c in filename if c.isalnum() or c in ('-', '_', '.'))
        if not filename.endswith('.json'):
            filename += '.json'
        
        # Create JSON string
        json_str = json.dumps(content, indent=2, ensure_ascii=False)
        
        # Return as downloadable file
        return send_file(
            StringIO(json_str).getvalue(),
            mimetype='application/json',
            as_attachment=True,
            download_name=filename
        )
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'generator_configured': generator is not None,
        'api_model': Config.AI_MODEL
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print("🚀 Social Media Content Generator Web App")
    print("📍 Starting server on http://localhost:5000")
    print("💡 Make sure your .env file is configured with your API key")
    
    # Run with debug mode for development
    app.run(debug=True, host='localhost', port=5000)
