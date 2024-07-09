# Coding for Sustainability

Base project for the Eureka Stem Academy Coding For Sustainability Program.

This project models an [industrial control system (ICS)](https://en.wikipedia.org/wiki/Industrial_control_system) used to observe sensors embedded in the solar arrays of [Sembcorp's Tengeh Floating Solar Farm](https://www.youtube.com/watch?v=SYRouvzPwzQ&t=58s).

See the diagrams about how [electricity flows from the solar farm to the grid](./docs/esa-electricity-flow-sg-0.1.1.pdf) and how [data flows between the solar arrays and the ICS](./docs/esa-solar-array-ics-0.1.1.pdf) for more context.

## Prerequisites

- [Python >=3.12](https://www.python.org/downloads/)
- [GNU Make](https://www.gnu.org/software/make/) (optional)

## Setup

- `make setup` to set up project tools such as git hooks
- `python3 -m venv .venv && source .venv/bin/activate` to setup a virtual environment and activate it

## Development

- `make install` to install required packages
- `make run` to run the program

## Lint

- `make lint` to lint the source code

## Format

- `make format` to format the source code

## Test

- `make test` to run tests

## Install a new dependency

1. `pip install [your-package-name]` to install a new package
2. `pip freeze > requirements.txt` to recreate the requirements file