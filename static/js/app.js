/**
 * Social Media Content Generator - JavaScript
 * Handles UI interactions and API calls
 */

let currentAbortController = null;
let longWaitTimer = null;

// ============ Loading & UI ============
const showLoading = (message = 'Generating your content...') => {
    const spinner = document.getElementById('loadingSpinner');
    const textEl = document.getElementById('loadingText');
    const forceReloadBtn = document.getElementById('forceReloadBtn');
    
    if (spinner && textEl) {
        spinner.classList.add('active');
        textEl.textContent = message;
        if (forceReloadBtn) forceReloadBtn.style.display = 'none';
    }
    
    // Show "Force Reload" button after 45 seconds
    longWaitTimer = setTimeout(() => {
        if (forceReloadBtn && spinner && spinner.classList.contains('active')) {
            forceReloadBtn.style.display = 'block';
        }
    }, 45000);
};

const hideLoading = () => {
    const spinner = document.getElementById('loadingSpinner');
    if (spinner) {
        spinner.classList.remove('active');
    }
    if (currentAbortController) {
        currentAbortController.abort();
    }
    currentAbortController = null;
    if (longWaitTimer) {
        clearTimeout(longWaitTimer);
    }
};

const cancelGeneration = () => {
    console.log('Cancel button clicked');
    hideLoading();
    showToast('⏸️ Generation cancelled', 'warning');
};

const showToast = (message, type = 'success') => {
    const container = document.getElementById('toastContainer');
    if (!container) return;
    
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    const icons = {
        'success': 'fa-check-circle',
        'error': 'fa-exclamation-circle',
        'warning': 'fa-info-circle'
    };
    
    const icon = icons[type] || 'fa-info-circle';
    toast.innerHTML = `<i class="fas ${icon}"></i><span>${message}</span>`;
    
    container.appendChild(toast);
    
    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }, 4000);
};

const escapeHtml = (text) => {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
};

// ============ Copy & Export ============
const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text).then(() => {
        showToast('✓ Copied to clipboard', 'success');
    }).catch(err => {
        showToast('Error copying to clipboard', 'error');
    });
};

// ============ Navigation ============
const switchMode = (mode) => {
    document.querySelectorAll('.mode-section').forEach(section => {
        section.classList.remove('active');
    });
    
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    const modeSection = document.querySelector(`[data-mode="${mode}"]`);
    const navBtn = document.querySelector(`.nav-btn[data-mode="${mode}"]`);
    
    if (modeSection) modeSection.classList.add('active');
    if (navBtn) navBtn.classList.add('active');
};

// ============ Generate Single ============
const generateSingle = async () => {
    const theme = document.getElementById('singleTheme')?.value.trim();
    
    if (!theme) {
        showToast('Please enter a theme', 'error');
        return;
    }
    
    const contentType = document.getElementById('singleContentType')?.value || 'general_content';
    const variations = parseInt(document.getElementById('singleVariations')?.value || 1);
    
    currentAbortController = new AbortController();
    showLoading('🔄 Generating content...');
    
    try {
        const response = await Promise.race([
            fetch('/api/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ theme, content_type: contentType, variations }),
                signal: currentAbortController.signal
            }),
            new Promise((_, reject) => 
                setTimeout(() => reject(new Error('Request timeout')), 60000)
            )
        ]);
        
        if (!response.ok) {
            throw new Error('Server error: ' + response.status);
        }
        
        const data = await response.json();
        
        if (data.success) {
            displaySingleResult(data);
            showToast('✓ Content generated!', 'success');
        } else {
            showToast('Error: ' + (data.error || 'Unknown error'), 'error');
        }
    } catch (error) {
        if (error.name !== 'AbortError') {
            showToast('Error: ' + error.message, 'error');
        }
    } finally {
        hideLoading();
    }
};

const displaySingleResult = (data) => {
    const container = document.getElementById('singleResults');
    if (!container) return;
    
    container.innerHTML = '';
    
    const card = document.createElement('div');
    card.className = 'result-card';
    
    const escapedContent = data.generated_content.replace(/'/g, "\\'");
    
    card.innerHTML = `
        <div class="result-header">
            <div class="result-title">${escapeHtml(data.content_type.replace(/_/g, ' ').toUpperCase())}</div>
            <button class="btn btn-copy" onclick="copyToClipboard('${escapedContent}')">
                <i class="fas fa-copy"></i> Copy
            </button>
        </div>
        <div class="result-content">${escapeHtml(data.generated_content)}</div>
    `;
    
    container.appendChild(card);
};

// ============ Generate Multi-Platform ============
const generateMultiPlatform = async () => {
    const theme = document.getElementById('multiTheme')?.value.trim();
    
    if (!theme) {
        showToast('Please enter a theme', 'error');
        return;
    }
    
    const platformCheckboxes = document.querySelectorAll('#multiForm .checkbox input:checked');
    const platforms = Array.from(platformCheckboxes).map(cb => cb.value);
    
    if (platforms.length === 0) {
        showToast('Please select at least one platform', 'error');
        return;
    }
    
    currentAbortController = new AbortController();
    showLoading(`📱 Generating for ${platforms.length} platform(s)...`);
    
    try {
        const response = await Promise.race([
            fetch('/api/multi-platform', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ theme, platforms }),
                signal: currentAbortController.signal
            }),
            new Promise((_, reject) => 
                setTimeout(() => reject(new Error('Request timeout')), 120000)
            )
        ]);
        
        if (!response.ok) {
            throw new Error('Server error: ' + response.status);
        }
        
        const data = await response.json();
        
        if (data.success) {
            displayMultiPlatformResult(data);
            showToast('✓ Content generated!', 'success');
        } else {
            showToast('Error: ' + (data.error || 'Unknown error'), 'error');
        }
    } catch (error) {
        if (error.name !== 'AbortError') {
            showToast('Error: ' + error.message, 'error');
        }
    } finally {
        hideLoading();
    }
};

const displayMultiPlatformResult = (data) => {
    const container = document.getElementById('multiResults');
    if (!container) return;
    
    container.innerHTML = '';
    
    const platformsHtml = Object.entries(data.platforms || {}).map(([platform, content]) => {
        const escapedContent = content.replace(/'/g, "\\'");
        return `
            <div class="platform-card">
                <div class="platform-name">${escapeHtml(platform.replace(/_/g, ' ').toUpperCase())}</div>
                <div class="platform-content">${escapeHtml(content)}</div>
                <button class="btn btn-copy" onclick="copyToClipboard('${escapedContent}')">
                    <i class="fas fa-copy"></i> Copy
                </button>
            </div>
        `;
    }).join('');
    
    container.innerHTML = `<div class="platform-results">${platformsHtml}</div>`;
};

// ============ Generate Hashtags ============
const generateHashtags = async () => {
    const theme = document.getElementById('hashtagTheme')?.value.trim();
    
    if (!theme) {
        showToast('Please enter a theme', 'error');
        return;
    }
    
    const count = parseInt(document.getElementById('hashtagCount')?.value || 10);
    
    currentAbortController = new AbortController();
    showLoading(`#️⃣ Generating hashtags...`);
    
    try {
        const response = await Promise.race([
            fetch('/api/hashtags', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ theme, count }),
                signal: currentAbortController.signal
            }),
            new Promise((_, reject) => 
                setTimeout(() => reject(new Error('Request timeout')), 60000)
            )
        ]);
        
        if (!response.ok) {
            throw new Error('Server error: ' + response.status);
        }
        
        const data = await response.json();
        
        if (data.success) {
            displayHashtagResult(data);
            showToast('✓ Hashtags generated!', 'success');
        } else {
            showToast('Error: ' + (data.error || 'Unknown error'), 'error');
        }
    } catch (error) {
        if (error.name !== 'AbortError') {
            showToast('Error: ' + error.message, 'error');
        }
    } finally {
        hideLoading();
    }
};

const displayHashtagResult = (data) => {
    const container = document.getElementById('hashtagResults');
    if (!container) return;
    
    container.innerHTML = '';
    
    const hashtags = data.hashtags;
    const escapedHashtags = hashtags.replace(/'/g, "\\'");
    
    const card = document.createElement('div');
    card.className = 'result-card';
    card.innerHTML = `
        <div class="result-header">
            <div class="result-title">#️⃣ Hashtags</div>
            <button class="btn btn-copy" onclick="copyToClipboard('${escapedHashtags}')">
                <i class="fas fa-copy"></i> Copy
            </button>
        </div>
        <div class="result-content">${escapeHtml(hashtags)}</div>
    `;
    
    container.appendChild(card);
};

// ============ Generate Batch ============
const generateBatch = async () => {
    const themesText = document.getElementById('batchThemes')?.value.trim();
    
    if (!themesText) {
        showToast('Please enter at least one theme', 'error');
        return;
    }
    
    const themes = themesText.split('\n').map(t => t.trim()).filter(t => t.length > 0);
    
    if (themes.length === 0) {
        showToast('Please enter valid themes', 'error');
        return;
    }
    
    currentAbortController = new AbortController();
    const timeoutMs = Math.min(30000 + (themes.length * 5000), 180000);
    showLoading(`📋 Generating for ${themes.length} theme(s)...`);
    
    try {
        const response = await Promise.race([
            fetch('/api/batch', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ themes }),
                signal: currentAbortController.signal
            }),
            new Promise((_, reject) => 
                setTimeout(() => reject(new Error('Request timeout')), timeoutMs)
            )
        ]);
        
        if (!response.ok) {
            throw new Error('Server error: ' + response.status);
        }
        
        const data = await response.json();
        
        if (data.success) {
            displayBatchResult(data);
            showToast('✓ Batch generation complete!', 'success');
        } else {
            showToast('Error: ' + (data.error || 'Unknown error'), 'error');
        }
    } catch (error) {
        if (error.name !== 'AbortError') {
            showToast('Error: ' + error.message, 'error');
        }
    } finally {
        hideLoading();
    }
};

const displayBatchResult = (data) => {
    const container = document.getElementById('batchResults');
    if (!container) return;
    
    container.innerHTML = '';
    
    if (!data.results || data.results.length === 0) {
        container.innerHTML = '<p>No results</p>';
        return;
    }
    
    const html = data.results.map((r, i) => {
        if (r.success) {
            const preview = r.generated_content.substring(0, 150);
            const escapedContent = r.generated_content.replace(/'/g, "\\'");
            return `
                <div class="result-card">
                    <div class="result-title">${i + 1}. ${escapeHtml(r.theme)}</div>
                    <div class="result-content">${escapeHtml(preview)}...</div>
                    <button class="btn btn-copy" onclick="copyToClipboard('${escapedContent}')">
                        <i class="fas fa-copy"></i> Copy
                    </button>
                </div>
            `;
        } else {
            return `
                <div class="result-card" style="border-left: 4px solid #f56565;">
                    <div class="result-title">${i + 1}. ${escapeHtml(r.theme)}</div>
                    <div style="color: #f56565;">❌ Error: ${escapeHtml(r.error)}</div>
                </div>
            `;
        }
    }).join('');
    
    container.innerHTML = html;
};

// ============ Initialize ============
document.addEventListener('DOMContentLoaded', () => {
    console.log('✓ App loaded successfully');
    console.log('Switching to single mode...');
    switchMode('single');
    console.log('DOM mode sections:', document.querySelectorAll('.mode-section').length);
    console.log('Active sections:', document.querySelectorAll('.mode-section.active').length);
    
    // Enter key support for theme inputs
    ['singleTheme', 'multiTheme', 'hashtagTheme'].forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    if (id === 'singleTheme') generateSingle();
                    if (id === 'multiTheme') generateMultiPlatform();
                    if (id === 'hashtagTheme') generateHashtags();
                }
            });
        }
    });
    
    // Enter key support for batch textarea (Ctrl+Enter)
    const batchThemes = document.getElementById('batchThemes');
    if (batchThemes) {
        batchThemes.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'Enter') {
                generateBatch();
            }
        });
    }
});
