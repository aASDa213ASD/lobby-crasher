# Lobby crasher:
Lobby crasher for League Of Legends, commited to work from 13.20 to 14.1.

# Requirements:
| Prerequisite               | Description       |
| -------------------------- | ----------------- |
| `Windows x32/x64`          | Operating System  |
| `Python 3.11`              | Interpreter       |

<br>

# Installation:
Step 1: Create virtual environment.
`python -m venv .env`

Step 2: Enter virtual environment you've just created.
`.env\Scripts\activate`

Step 3: Install prerequisites.
`pip install -r requirements.txt`

<br>

# Usage:
### Variant A:
Run `launch.bat` (if you've created virtual environment with different name -> change it in `.bat` file as well)

### Variant B:
```batch
.env\Scripts\activate
python main.py
```

> **How to:** <hr>
Step 1. Log into `main account` and launch the script. <br>
Step 2. Log into the `second account` and create a custom lobby. <br>
Step 3. Press <kbd>1</kbd> in the script and provide your second account summoner name. <br>
Step 4. Queue up and press <kbd>2</kbd> to escape the prison. <br>
Step 5. Leave from custom lobby with your `second account` (so that only `main account` remains in it) <br>
Step 6. Launch the custom game's champ select with `main account` and proceed to the game. <br>
Step 7. **Wait until your soloq lobby goes to 0 seconds**, only after that you may leave the custom game and play again with no penalties applied & LP losses.<br>