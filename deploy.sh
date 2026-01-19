#!/bin/bash
# Lidice's Cleaning Services - Deploy Script

echo "Lidice's Cleaning Services - Deployment"
echo "========================================"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
    git add .
    git commit -m "Lidice's Cleaning Services - Initial commit"
    git branch -M main
fi

echo ""
echo "Choose deployment platform:"
echo "1) GitHub Pages (recommended - free)"
echo "2) Local preview only"
echo ""
read -p "Enter choice [1-2]: " choice

case $choice in
    1)
        echo ""
        read -p "Enter your GitHub username: " username
        repo_name="lidice-cleaning"

        echo "Creating GitHub repo..."
        gh repo create $repo_name --public --source=. --push 2>/dev/null || {
            echo "Note: If repo exists, pushing to it..."
            git remote add origin "https://github.com/$username/$repo_name.git" 2>/dev/null
            git push -u origin main
        }

        echo ""
        echo "Code pushed! Now enable GitHub Pages:"
        echo "   1. Go to: https://github.com/$username/$repo_name/settings/pages"
        echo "   2. Source: Deploy from branch"
        echo "   3. Branch: main, Folder: /docs"
        echo "   4. Save"
        echo ""
        echo "Your site will be at: https://$username.github.io/$repo_name/"
        ;;
    2)
        echo ""
        echo "Starting local server..."
        echo "Open http://localhost:8000 in your browser"
        echo "Press Ctrl+C to stop"
        echo ""
        cd docs && python3 -m http.server 8000
        ;;
esac
