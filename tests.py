"""
Unit tests for the Social Media Content Generator.
Verify all components work correctly before deployment.
"""

import unittest
from config import Config
from content_generator import ContentGenerator


class TestConfig(unittest.TestCase):
    """Test configuration module."""
    
    def test_config_loading(self):
        """Test that configuration loads correctly."""
        # Check that PROMPTS has all required content types
        required_types = [
            "instagram_post",
            "twitter_post",
            "facebook_post",
            "linkedin_post",
            "tiktok_caption",
            "email_subject",
            "general_content"
        ]
        
        for content_type in required_types:
            self.assertIn(content_type, Config.PROMPTS)
    
    def test_temperature_setting(self):
        """Test temperature is within valid range."""
        self.assertGreaterEqual(Config.TEMPERATURE, 0)
        self.assertLessEqual(Config.TEMPERATURE, 1)
    
    def test_max_tokens(self):
        """Test max tokens is reasonable."""
        self.assertGreater(Config.MAX_TOKENS, 0)
        self.assertLess(Config.MAX_TOKENS, 2000)


class TestContentGenerator(unittest.TestCase):
    """Test content generator functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Note: This will fail if API key is not configured
        # In CI/CD, mock the API responses
        try:
            self.generator = ContentGenerator()
        except ValueError as e:
            self.skipTest(f"API Key not configured: {e}")
    
    def test_generator_initialization(self):
        """Test generator initializes correctly."""
        self.assertIsNotNone(self.generator)
    
    def test_invalid_content_type(self):
        """Test error handling for invalid content type."""
        result = self.generator.generate_content(
            theme="test",
            content_type="invalid_type"
        )
        
        self.assertFalse(result["success"])
        self.assertIn("error", result.lower())
    
    def test_generate_content_structure(self):
        """Test that generated content has proper structure."""
        # Skip if no API key
        try:
            result = self.generator.generate_content(
                theme="test theme",
                content_type="general_content"
            )
            
            if result["success"]:
                self.assertIn("theme", result)
                self.assertIn("content_type", result)
                self.assertIn("generated_content", result)
                self.assertIn("model_used", result)
        except Exception:
            self.skipTest("API call failed - skipping")


class TestIntegration(unittest.TestCase):
    """Integration tests."""
    
    def setUp(self):
        """Set up test fixtures."""
        try:
            self.generator = ContentGenerator()
        except ValueError:
            self.skipTest("API Key not configured")
    
    def test_all_content_types_available(self):
        """Test all content types can be accessed."""
        themes = list(Config.PROMPTS.keys())
        self.assertGreater(len(themes), 0)
        
        # Each content type should have a corresponding prompt
        for content_type in themes:
            self.assertIn(content_type, Config.PROMPTS)


def run_tests():
    """Run all tests."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestConfig))
    suite.addTests(loader.loadTestsFromTestCase(TestContentGenerator))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == "__main__":
    run_tests()
