# Camus

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

> A modern, extensible platform for building and deploying real-time applications.  
> Developed by **Bocaletto Luca**.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Technology Stack](#technology-stack)  
4. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
5. [Usage](#usage)  
6. [Configuration](#configuration)  
7. [Directory Structure](#directory-structure)  
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Contact](#contact)  

---

## Project Overview

Camus is a lightweight, Python-powered framework designed to accelerate development of real-time, event-driven applications. Whether you’re building chat services, multiplayer games, or IoT dashboards, Camus provides a modular core, pluggable transport layers, and a minimal CLI to scaffold, run, and monitor your projects with ease.

---

## Features

- Modular core with support for multiple messaging backends (WebSocket, MQTT, Redis Pub/Sub)  
- Built-in user/session management and authentication hooks  
- Real-time event routing, filtering, and broadcasting  
- CLI tooling for scaffolding, running, and deploying applications  
- Extensible plugin system for custom transports, storage adapters, and middleware  
- Comprehensive logging and metrics collection  

---

## Technology Stack

- Python 3.8+  
- `asyncio` for high-performance event loop  
- `FastAPI` (optional) for RESTful endpoints  
- `websockets`, `paho-mqtt`, `aioredis` transport adapters  
- `Typer` for command-line interface  
- `PyTest` & `Hypothesis` for testing  
- `Docker` & `docker-compose` for containerized deployments  

---

## Getting Started

### Prerequisites

- Python 3.8 or newer  
- [Git](https://git-scm.com/)  
- [Docker](https://www.docker.com/) & [docker-compose](https://docs.docker.com/compose/) (optional)  

### Installation

```bash
# Clone the repository
git clone https://github.com/bocaletto-luca/Camus.git
cd Camus

# Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate       # Linux / macOS
.\.venv\Scripts\activate        # Windows PowerShell

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Usage

### CLI Commands

```bash
# Initialize a new Camus application
camus init my_app

# Run the development server
cd my_app
camus serve --host 0.0.0.0 --port 8080

# Build a Docker image
camus build --tag camus/my_app:latest
```

### Embedding in Python

```python
from camus import CamusApp

app = CamusApp(name="my_app")
app.register_route("message", handler=my_message_handler)
app.run(host="0.0.0.0", port=8080)
```

---

## Configuration

Camus applications are driven by a `config.yaml` in the project root:

```yaml
app:
  name: my_app
  debug: true

server:
  host: 0.0.0.0
  port: 8080

transports:
  websocket:
    enabled: true
    path: /ws
  redis:
    url: redis://localhost:6379/0
```

---

## Directory Structure

```
Camus/
├── camus/                  # Core library modules
│   ├── __init__.py
│   ├── core.py             # Application core & event loop
│   ├── cli.py              # Typer-based CLI
│   ├── transports/         # WebSocket, MQTT, Redis adapters
│   └── middleware/         # Authentication, logging, etc.
├── examples/               # Example apps & demos
│   └── chat/               # Real-time chat example
├── tests/                  # Unit & integration tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── config.yaml             # Default application configuration
└── README.md
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository  
2. Create a feature branch  
   ```bash
   git checkout -b feature/awesome-feature
   ```  
3. Commit your changes  
   ```bash
   git commit -m "Add awesome feature"
   ```  
4. Push to your fork and open a Pull Request  
5. Ensure tests pass and code style checks  
   ```bash
   pytest
   flake8
   black --check .
   ```  

---

## License

This project is licensed under the **GNU General Public License v3.0**.  
See [LICENSE](LICENSE) for details.

---

## Contact

Bocaletto Luca  
– GitHub: [@bocaletto-luca](https://github.com/bocaletto-luca)  

---
