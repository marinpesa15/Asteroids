# Asteroids

A classic Asteroids arcade game clone built with Python and Pygame. Navigate your ship through an asteroid field, shoot to survive, and try to last as long as possible.

## Gameplay

You control a triangular ship in the center of the screen. Asteroids spawn continuously from all four edges and drift across the playing field. Shoot them to break them apart — large asteroids split into two smaller, faster fragments. If any asteroid collides with your ship, the game is over.

### Controls

| Key | Action |
|-----|--------|
| `W` | Move forward |
| `S` | Move backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot (with 0.3s cooldown) |

## Project Structure

```
Asteroids/
├── main.py            # Game loop, event handling, collision detection
├── player.py          # Player ship: movement, rotation, shooting
├── asteroid.py        # Asteroid behavior and splitting logic
├── asteroidfield.py   # Spawns asteroids from random screen edges
├── shot.py            # Projectile fired by the player
├── circleshape.py     # Base class for all game objects (collision, position, velocity)
├── constants.py       # Game configuration (screen size, speeds, radii, cooldowns)
├── logger.py          # Debug logger — writes game state and events to JSONL files
├── pyproject.toml     # Project metadata and dependencies
└── uv.lock            # Dependency lock file
```

## Requirements

- Python >= 3.14
- Pygame 2.6.1

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
git clone https://github.com/marinpesa15/Asteroids.git
cd Asteroids
uv sync
```

## Running the Game

```bash
uv run python main.py
```

## How It Works

The game is built on Pygame's sprite system. All game objects (player, asteroids, shots) inherit from `CircleShape`, which extends `pygame.sprite.Sprite` and provides position/velocity tracking and circle-based collision detection.

Asteroids spawn at timed intervals from random positions along the screen edges, moving inward at randomized speeds and angles. When shot, an asteroid splits into two smaller pieces that move faster and at diverging angles — unless it's already at the minimum size, in which case it's destroyed. The game runs at 60 FPS with delta-time-based movement for consistent behavior.

A built-in logger captures game state snapshots (once per second for the first 16 seconds) and discrete events like hits and splits, writing them to `game_state.jsonl` and `game_events.jsonl` for debugging and analysis.

## Built With

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/)
- [uv](https://docs.astral.sh/uv/)
