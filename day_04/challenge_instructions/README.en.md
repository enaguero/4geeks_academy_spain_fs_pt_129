[🇪🇸 Español](README.md) | 🇬🇧 **English**

# 🖥️ The Terminal Challenge - CMD Challenge

Interactive presentation built with Reveal.js to teach basic terminal commands through a hands-on challenge.

## 📋 Description

This presentation contains **22 slides** with progressive instructions so students can practice terminal commands in a fun, competitive way.

## 🚀 How to use

### Option 1: Open directly in the browser

Just open the `index.html` file in your browser:

```bash
open index.html
# or on Linux/Windows
xdg-open index.html  # Linux
start index.html     # Windows
```

### Option 2: Local server with Python

If you prefer a local server:

```bash
python3 -m http.server 8000
```

Then open in your browser: `http://localhost:8000`

### Option 3: Live Server (VS Code)

If you use VS Code, install the "Live Server" extension and right-click on `index.html` → "Open with Live Server"

## 🎯 Presentation Structure

1. **Cover** - Introduction to the challenge
2. **Welcome** - Explanation of the purpose
3. **Rules** - How the competitive challenge works
4. **Basic commands** - Quick reference
5. **Setup** - Checklist before starting
6. **Instructions 1-16** - Progressive hands-on challenges
7. **Congratulations** - Closing slide
8. **Resources** - Additional material
9. **Tips** - Final tips

Total: **22 slides**

## 🎮 Navigation

- **Arrows ← →** or **Space**: Next/previous slide
- **ESC**: Overview of all slides
- **F**: Fullscreen
- **S**: Speaker mode (presenter notes)
- **?**: Keyboard shortcuts help

## 📝 Instructions for the Instructor

### Before Class

1. Make sure students have:
   - A terminal installed (bash/zsh)
   - The `thecmdchallenge/` folder downloaded (from the original 4Geeks repo)
   - Basic knowledge of directory navigation

### During Class

1. Project the presentation
2. Read each instruction out loud
3. Give students time to complete the challenge
4. The first student to finish should:
   - Raise their hand
   - Explain their solution to the class
   - Show the command they used
5. Move on to the next slide

### Challenge Dynamics

- **Competitive**: The first to complete each instruction wins
- **Educational**: The winner explains their solution (everyone learns)
- **Progressive**: Instructions increase in difficulty
- **Fun**: The challenges use files with funny names

## 🎨 Customization

### Change Theme

On line 9 of `index.html`, you can change the theme:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.0.4/dist/theme/black.css">
```

Available themes:
- `black.css` (current)
- `white.css`
- `league.css`
- `beige.css`
- `sky.css`
- `night.css`
- `serif.css`
- `simple.css`
- `solarized.css`

### Modify Content

Each slide is a `<section>...</section>`. You can:
- Add more slides
- Modify existing instructions
- Change background colors with `data-background-color="#color"`
- Add gradients with `data-background-gradient`

## 📦 Dependencies

The presentation uses CDN, so **you don't need to install anything**:

- Reveal.js 5.0.4
- Syntax highlighting plugin

Everything loads automatically from CDN.

## 🔗 Useful Links

- [Reveal.js Documentation](https://revealjs.com/)
- [Original Challenge (in English)](https://breatheco-de.github.io/exercise-terminal-challenge-slides/#/0)
- [Original 4Geeks Repository](https://github.com/breatheco-de/exercise-terminal-challenge-slides)

## 📄 Files Included

```
challenge_instructions/
├── index.html          # Reveal.js presentation
├── README.md          # This file
├── slides-data.json   # Original challenge data
└── terminal-challenge.html  # Original downloaded HTML (reference)
```

## 🎓 Student Level

- **Target audience**: Beginners in web development
- **Prerequisites**: Having opened the terminal at least once
- **Estimated duration**: 60-90 minutes (depending on the group)

## 💡 Tips for the Instructor

1. **Pause between slides**: Give enough time for each challenge
2. **Selective help**: Let them try first, help only if they get stuck
3. **Encourage collaboration**: Students can help each other (after the winner)
4. **Reinforce concepts**: Use the winners' explanations to teach
5. **Celebrate mistakes**: They are learning opportunities

## 🐛 Troubleshooting

### The presentation doesn't load
- Check your internet connection (CDN-based)
- Try opening it in another browser
- Check the browser console (F12) for errors

### Commands don't work on Windows
- Use Git Bash or WSL (Windows Subsystem for Linux)
- Or use Gitpod/Cloud IDE as suggested by the original challenge

### The challenge files don't exist
- Make sure students cloned the correct repo:
  ```bash
  git clone https://github.com/breatheco-de/exercise-terminal-challenge.git
  ```

---

**Created for**: 4Geeks Academy Spain - Full Stack PT Cohort 129  
**Based on**: [Terminal Challenge by BreatheCode](https://breatheco-de.github.io/exercise-terminal-challenge-slides/)  
**Technology**: Reveal.js 5.0.4
