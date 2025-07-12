# Automated 2048 Game Bot

This is a simple Python script that uses Selenium to automatically play the 2048 game by randomly selecting legal moves each turn until the game ends.

---

## What It Does

* **Opens** Google Chrome and navigates to play2048.co
* **Reads** the 4×4 game board and tracks tile values
* **Chooses** a random valid move each turn
* **Prints** each move in the terminal and shows the final board and score
* **Easy to modify**: update the move logic to try different strategies

## Requirements

* Python 3.7 or higher
* Google Chrome browser
* ChromeDriver matching your Chrome version
* Selenium Python package (install with: pip install selenium)

## Setup

1. **Clone the repository:**
   git clone [https://github.com/kokoc30/automated-2048-game-bot.git](https://github.com/kokoc30/automated-2048-game-bot.git)
   cd automated-2048-game-bot
2. **Optional: Create a virtual environment:**
   python -m venv .venv
   Activate with:

   * On Linux/macOS: source .venv/bin/activate
   * On Windows PowerShell: ..venv\Scripts\activate
3. **Install dependencies:**
   pip install selenium
4. **Download ChromeDriver:**

   * Visit: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
   * Download the version matching your Chrome browser
   * Place the chromedriver file in the project root or in your system PATH

## Usage

Run the bot with:
python automated\_2048\_game.py

* Chrome will open and play 2048 until the game ends
* The terminal will display each move and the final score
* Press Enter in the terminal to close the browser

## Customization

* Change the move logic in automated\_2048\_game.py to try new strategies
* Adjust any time delays (time.sleep) to speed up or slow down the bot

## License

This project is licensed under the MIT License. See the LICENSE file for details.



