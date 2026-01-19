# Lidice's Cleaning Services

Professional cleaning services website for Stockholm, Sweden. Bilingual (English/Swedish) static site built with Python and hosted on GitHub Pages.

## 🏠 Services

- **Residential Cleaning**: Regular, deep cleaning, move-in/out, windows
- **School Cleaning**: Kindergarten to secondary school, daily & deep cleaning

## 🚀 Quick Start

### Generate the Site

```bash
# No dependencies required - uses Python standard library
python3 generate_site.py
```

### View Locally

Open `docs/index.html` in your browser, or use Python's built-in server:

```bash
cd docs
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Deploy to GitHub Pages

1. Push to GitHub
2. Go to Settings → Pages
3. Source: Deploy from branch `main`, folder `/docs`
4. Your site will be live at `https://USERNAME.github.io/lidice-cleaning/`

## 📁 Project Structure

```
lidice-cleaning/
├── generate_site.py      # Static site generator
├── requirements.txt      # Dependencies (minimal)
├── README.md            # This file
├── .gitignore
└── docs/                # Generated output (GitHub Pages)
    ├── index.html       # Landing (language detection)
    ├── en/              # English version
    │   ├── index.html   # Home
    │   ├── services.html
    │   ├── quote.html
    │   └── about.html
    ├── sv/              # Swedish version
    │   ├── index.html
    │   ├── tjanster.html
    │   ├── offert.html
    │   └── om-oss.html
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

## 🎨 Design

- **Colors**: Professional blue (#2563EB) + Fresh green (#10B981)
- **Typography**: Inter font (Google Fonts)
- **Style**: Clean, modern, lots of white space
- **Responsive**: Mobile-first design

## 📞 Contact

- **Phone**: +46 73 534 4533
- **Email**: lidice.cleaning@gmail.com
- **Hours**: Mon-Fri 7:00-18:00
- **Location**: Stockholm, Sweden

## 🔧 Customization

Edit the `CONTENT` dictionary in `generate_site.py` to update:
- Page text and translations
- Service descriptions
- Contact information
- Testimonials

Then regenerate: `python3 generate_site.py`

## 📝 License

© 2025 Lidice's Cleaning Services. All rights reserved.
