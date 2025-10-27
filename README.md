# UX to UI Slider

An interactive web application demonstrating the transition from UX (User Experience) to UI (User Interface) through an intuitive slider control.

## Features

- 🎨 Interactive slider control (UX ↔ UI)
- 🖼️ Smooth image/GIF transitions
- 📱 Fully responsive design
- ⚡ Fast loading with preloaded assets
- 🎭 Beautiful loading animation

## Demo

Visit the live version: [Your GitHub Pages URL]

## How It Works

The slider has 7 positions representing the progression from UX (left) to UI (right):
- **UX Side** (Position 0): Initial user experience concepts
- **Middle Positions** (1-5): Transitional states
- **UI Side** (Position 6): Final user interface implementation

## Local Development

### Web Version (Recommended for GitHub Pages)

Simply open `index.html` in your web browser or serve it with a local server:

```bash
# Using Python
python3 -m http.server 8000

# Using Node.js
npx serve
```

Then open http://localhost:8000 in your browser.

### Python/Flet Version

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python3 main.py
```

## Deployment to GitHub Pages

1. Push your repository to GitHub
2. Go to Settings → Pages
3. Select your branch (usually `main` or `master`)
4. Save and wait a few minutes
5. Your site will be live at `https://yourusername.github.io/repository-name/`

## Project Structure

```
.
├── index.html          # Web version (for GitHub Pages)
├── main.py            # Python/Flet version
├── requirements.txt    # Python dependencies
├── Assets/            # Images and GIFs
│   ├── 1-4.png       # Static images
│   ├── 5-7.gif       # Animated GIFs
│   └── Loading Animation.gif
└── README.md          # This file
```

## Technologies

- **Web Version**: HTML5, CSS3, JavaScript
- **Desktop Version**: Python, Flet

## License

MIT
