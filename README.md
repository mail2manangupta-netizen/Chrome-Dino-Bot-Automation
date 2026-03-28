# 🦖 Chrome Dino Auto Player Bot

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Working-success)
![Type](https://img.shields.io/badge/Project-Automation-orange)
![Level](https://img.shields.io/badge/Level-Intermediate-purple)

Automate the classic Chrome Dino game using **screen capture + pixel detection + keyboard automation**.
This bot detects obstacles in real-time and jumps automatically.

---

## 🎮 Demo Context

![Image](https://img.poki-cdn.com/cdn-cgi/image/q%3D78%2Cscq%3D50%2Cwidth%3D1200%2Cheight%3D1200%2Cfit%3Dcover%2Cf%3Dpng/9afd3b92ab41ffca7f368a8fcbd6d39a75894efe0edbc14cf1f067cf625e6678/dinosaur-game.png)

![Image](https://media.sketchfab.com/models/947431edc05b414d8df48fd13780ff2f/thumbnails/2463b506f2014a04ad68e1f7a7495ad0/de0bddc4dde8498db862cb14291828a7.jpeg)

![Image](https://miro.medium.com/1%2A82D2cg8Gpe9CVISaph6RPg.gif)

![Image](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/Social_dino-with-hat.gif)

---

## 🚀 Features

* 📸 Real-time screen capture using `mss`
* 🧠 Lightweight obstacle detection (no heavy ML)
* ⚡ Fast reaction time
* 🤖 Auto jump using `pyautogui`
* 🎯 Focused scan region for performance

---

## ⚙️ How It Works

1. Waits 5 seconds for setup
2. Captures a **small region ahead of the Dino**
3. Converts image → grayscale
4. Detects **dark pixels (cactus/bird)**
5. Calculates distance
6. Presses **space** if obstacle is close

---

## 📍 Important Setup (READ THIS ⚠️)

👉 This bot is **position-dependent**

You MUST:

* Open Chrome Dino game
* Place the game window on the **LEFT side of your screen**
* Keep:

  * Zoom = **100%**
  * Window size = **not resized randomly**
* Do NOT move the window while running

### Why?

Because detection uses fixed coordinates:

```python
SCAN_REGION = {
    "left": 140,
    "top": 590,
    "width": 110,
    "height": 80
}
```

If your layout is different → detection will fail 💀

---

## 🧰 Tech Stack

* Python 🐍
* NumPy
* MSS (screen capture)
* PyAutoGUI (keyboard control)

---

## ▶️ Installation

```bash
pip install numpy mss pyautogui
```

---

## ▶️ Run

```bash
python main.py
```

Then:

* Quickly switch to Dino game (you get 5 seconds)
* Sit back and watch the bot cook 😎

---

## 🧠 Core Logic (Simplified)

```text
Capture screen → Convert to grayscale → 
Crop region → Detect dark pixels → 
If obstacle close → Jump
```

---

## ⚠️ Limitations

* Screen resolution dependent
* Fixed scan region (needs manual tuning)
* May struggle at very high speeds

---

## 💡 Future Improvements

* 🎥 Live debug view (OpenCV)
* 📈 Speed-based adaptive jumping
* 🖥️ Auto calibration of scan region
* 🧠 Smarter obstacle classification

---

## 📌 Disclaimer

This project is for educational purposes only.
Use responsibly.

---

## ⭐ If you like this

Give it a star ⭐ and flex your automation skills 😤
