# Package Delivery Routing System

This project simulates a package delivery routing system for a local delivery service. It models the logistics of tracking and delivering packages efficiently using truck route optimization.

## Overview

The system is designed to:
- Track the real-time status of packages (`At Hub`, `En Route`, `Delivered`)
- Assign packages to trucks with time and location constraints
- Simulate delivery routes using a distance-based algorithm
- Account for real-world rules, such as:
  - Delayed address correction for a specific package
  - Limited number of truck drivers

This project was built as part of WGU's Data Structures and Algorithms II course and demonstrates skills in Python, object-oriented programming, and algorithmic problem solving.

## Features

- **Package Class**  
  Stores package data and dynamically updates status based on simulated time and truck delivery info.

- **Truck Class**  
  Models each truck's delivery behavior, tracks mileage, and manages packages on board.

- **Address Correction Logic**  
  Implements a constraint where Package 9 has an incorrect address until 10:20 AM.

- **Routing Algorithm (Nearest Neighbor)**  
  Selects the next package to deliver based on the shortest distance to reduce mileage.

- **Delivery Simulation**  
  Tracks delivery time and calculates when each package is delivered based on truck speed (18 mph).

## 🛠 Technologies

- Python 3
- Standard Library (`datetime`, `csv`, etc.)
- Object-Oriented Programming (OOP)

## 📦 Example Usage

```bash
# Run the main delivery simulation
python main.py
```

Inside the program, you can:
- Print the delivery status of all packages at a given time
- Check individual package delivery details
- View total mileage of trucks

## Project Structure

```
├── main.py                  # Main driver file
├── package.py               # Package class with update logic
├── truck.py                 # Truck class with delivery simulation
├── distances.csv            # Distance table between addresses
├── addresses.csv            # Address index
└── README.md                # Project documentation
```

## Special Constraints

- Only two drivers available, so only two trucks can be on the road at once
- Package 9 has an incorrect address until 10:20 AM
- Truck 3 cannot leave the hub until 10:20 AM or until another truck returns

## Learning Objectives

- Implement custom data structures
- Simulate real-world logistics
- Apply greedy algorithms for route optimization
- Track and manipulate time-based package delivery
