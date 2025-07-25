from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# ─── Setup ───────────
driver = webdriver.Chrome()
driver.get("https://play2048.co")
body = driver.find_element(By.TAG_NAME, "body")


# ─── Board Parser ───────────
def get_board():
    board = [[0] * 4 for _ in range(4)]
    tiles = driver.find_elements(By.CSS_SELECTOR, ".tile")
    for tile in tiles:
        try:
            cls = tile.get_attribute("class").split()
            val_class = [c for c in cls if c.startswith("tile-") and c.count("-") == 1][0]
            val = int(val_class.split("-")[1])
            pos_class = [c for c in cls if c.startswith("tile-position-")][0]
            _, _, col_str, row_str = pos_class.split("-")
            col, row = int(col_str) - 1, int(row_str) - 1
            if 0 <= row < 4 and 0 <= col < 4:
                board[row][col] = val
        except (IndexError, ValueError):
            pass
    return board


# ─── Game Logic ───────────────────────────────────────
print("Initial board:")
for row in get_board():
    print(row)

MOVES = [Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_UP, Keys.ARROW_RIGHT]

while True:
    # Check for game over
    if driver.find_elements(By.CSS_SELECTOR, ".game-over"):
        print("Game Over detected!")
        break

    board_before = get_board()

    random.shuffle(MOVES)
    for move in MOVES:
        body.send_keys(move)
        time.sleep(0.05)
        if get_board() != board_before:
            break

    time.sleep(0.15)

# ─── Final Score ──────────
print("\n" + "=" * 20)
print("Final Board:")
for row in get_board():
    print(row)

score = driver.find_element(By.CLASS_NAME, "score-container").text.split('\n')[0]
print("\nFinal Score:", score)
print("=" * 20)

input("Press Enter to close browser…")
driver.quit()
