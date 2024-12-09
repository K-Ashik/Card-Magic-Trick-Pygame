# Card Trick Game 🎩🃏

Welcome to **Card Trick Game**, a fun and interactive card magic trick simulation built using Python and Pygame. The game combines visual effects, humorous commentary, and dynamic narratives to create an immersive magician experience.

## Table of Contents
- [Features](#features)
- [Gameplay](#gameplay)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Folder Structure](#folder-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **21-Card Trick Magic**: Classic magician's trick with cards shuffled and revealed.
- **Dynamic Commentary**: The game includes humorous and engaging commentary that adapts based on the game state.
- **Narrative Mode**: Provides a story-driven experience to enhance gameplay immersion.
- **Interactive Buttons**: Buttons allow the player to interact with the game and control actions.
- **Visual Animations**: Smooth card movements and interactive elements.

---

## Gameplay

The magician shuffles and deals a set of 21 cards into three rows. The player selects a row, and the magician magically identifies the player's card through a series of shuffles and reveals. Can you outsmart the magician? 🤔

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/K-Ashik/Card-Magic-Trick-Pygame.git
    cd card_trick_pygame
    ```
2. Install the required dependencies:
    ```bash
    pip install pygame
    ```
3. Ensure the required images and resources are in the appropriate directories:
    - **Cards**: Images for card assets.
    - **Background and Icons**: Game background and application icon.

4. Run the game:
    ```bash
    card_trick.py
    ```

---

## How to Play

1. Launch the game.
2. Click **Start** to deal the cards.
3. Choose a row where your card is located (Row A, B, or C).
4. Watch as the magician shuffles the cards.
5. Repeat for three rounds. The magician will reveal your card at the end!

### Controls:
- **Mouse**: Click on buttons to make selections.
- **Keyboard**:
  - `Space`: Deal the cards.
  - `A`, `B`: Rearrange or display cards in rows.

---

## Folder Structure

```plaintext
card_trick_pygame/
│
├── card_trick.py                 # Run game script
├── twenty_one_cards_trick.py     # Main game script
├── back_end.py             # Backend logic for card handling and positioning
├── images/                 # Contains image assets
│   ├── blackjack.png       # Background image
│   ├── cards/              # Card images
│   ├── icon/               # Application icons
│   └── ...
└── README.md               # Project documentation

```



### Technologies Used
	•	Python: Core language for development.
	•	Pygame: For game development, graphics, and user interaction.


### Credits

Developed by [PythonGameDev].

Enjoy the game and amaze yourself with the magician’s tricks! 🎩✨
