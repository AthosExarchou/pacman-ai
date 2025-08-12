# Pacman AI – Search Algorithms

This project is based on the UC Berkeley CS188 Pacman AI framework, implementing and testing algorithms and multi-agent search strategies for Pacman.

## Description
Pacman is controlled by an AI agent that makes decisions based on:
- The distance to the nearest ghost
- The distance to the nearest food
- The current score (number of food pellets eaten)
- The remaining food

The main custom code is implemented in `search.py`, `searchAgents.py` and `multiAgents.py`.

---
## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/AthosExarchou/pacman-ai.git
cd pacman-ai
```

### 2. Create and activate a Conda environment
```bash
conda create -n pacman-env python=3.6
conda activate pacman-env
```

### 3. Run the game
Example run using AlphaBetaAgent with custom evaluation:
```bash
python pacman.py -p AlphaBetaAgent -a evalFn=better,depth=2 -l smallClassic -k 2
```

```bash
pacman-ai/
│── pacman.py               # Main entry point
│── multiAgents.py          # Contains custom evaluation function
│── search.py               # Search algorithms
│── searchAgents.py         # Search agent definitions
│── util.py                 # Helper functions
│── game.py, ghostAgents.py # Core game logic
│── graphicsDisplay.py      # Graphics rendering
│── graphicsUtils.py
│── layouts/                # Maze layout files
│── README.md               # This file
│── .gitignore              # Ignored files
```

### Testing & Project Commands
Run Pacman in a medium maze with BFS search:
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```

Run Pacman in a medium maze with A* search:
```bash
python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

Run minimax:
```bash
python pacman.py -p MinimaxAgent -a evalFn=better,depth=2 -l smallClassic -k 2
```

Run alpha-beta pruning:
```bash
python pacman.py -p AlphaBetaAgent -a evalFn=better,depth=2 -l smallClassic -k 2
```

If you want to run the UC Berkeley autograder tests:
```bash
python autograder.py --no-graphics
```
Or test a single question (e.g. question-6):
```bash
python autograder.py -q q6
```

---
## Author

- **Name**: Exarchou Athos
- **Student ID**: it2022134
- **Email**: it2022134@hua.gr or athosexarhou@gmail.com

## License
This project is based on UC Berkeley CS188 Pacman framework. Original materials available [here](https://ai.berkeley.edu/).
