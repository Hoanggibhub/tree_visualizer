// Path handling
function setupPathSuggestions() {
    const input = document.getElementById('search-input');
    const suggestions = document.getElementById('path-suggestions');
    
    input.addEventListener('input', () => {
        const searchTerm = input.value.toLowerCase();
        suggestions.innerHTML = '';
        
        if (searchTerm.length > 1) {
            const matches = window.pathSuggestions.filter(path => 
                path.toLowerCase().includes(searchTerm)
            ).slice(0, 5);
            
            matches.forEach(path => {
                const div = document.createElement('div');
                div.className = 'suggestion-item';
                div.textContent = path;
                div.onclick = () => {
                    input.value = path;
                    highlightPath(path);
                };
                suggestions.appendChild(div);
            });
        }
    });
}

// Copy path functionality
function setupCopyButtons() {
    document.querySelectorAll('.node-path').forEach(el => {
        el.addEventListener('click', (e) => {
            navigator.clipboard.writeText(e.target.dataset.path)
                .then(() => {
                    const tooltip = document.createElement('div');
                    tooltip.className = 'copy-tooltip';
                    tooltip.textContent = 'Copied!';
                    e.target.appendChild(tooltip);
                    setTimeout(() => tooltip.remove(), 1000);
                });
        });
    });
}