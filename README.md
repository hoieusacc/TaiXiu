# TaiXiu

_A simple Tai Xiu dice game simulation (Python)_

_Built with Python_

![Last Commit](https://img.shields.io/github/last-commit/hoieusacc/TaiXiu?style=flat-square)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

---

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Game Logic](#game-logic)
- [License](#license)

---

## Overview

**TaiXiu** is a Python script that simulates the traditional “Tài Xỉu” dice game, where three six-sided dice are rolled and players guess whether the total is “Tài” (big) or “Xỉu” (small).

---

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/hoieusacc/TaiXiu.git
2. **Navigate into the project directory:**
   ```bash
   cd TaiXiu
Usage
Run the simulation with:
  ```bash
  python TaiXiu.py
```

Game Logic
  - Rolls 3 dice (values 1–6 each)
  - Computes sum:
    + Tài (big): sum from 11 to 18
    + Xỉu (small): sum from 3 to 10
  - Outputs the result along with the dice values and whether the guess was correct or not.

[⬅ Return](#TaiXiu)

