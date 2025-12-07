ConnectIT
==========

<a href="https://www.producthunt.com/products/connect-it?embed=true&utm_source=badge-featured&utm_medium=badge&utm_source=badge-connect&#0045;it" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1016671&theme=neutral&t=1758001359763" alt="Connect&#0032;it&#0032; - Torrent&#0032;Like&#0032;Protocol&#0032;for&#0032;Deployment&#0032;LLM&#0032;Models | Product Hunt" style="width: 250px; height: 54px;" width="250" height="54" /></a>

# ConnectIT

[![PyPI version](https://img.shields.io/pypi/v/connectit.svg)](https://pypi.org/project/connectit/)
[![Python versions](https://img.shields.io/pypi/pyversions/connectit.svg)](https://pypi.org/project/connectit/)
[![Downloads](https://img.shields.io/pypi/dm/connectit.svg)](https://pypi.org/project/connectit/)
[![License](https://img.shields.io/badge/License-Custom-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/github/actions/workflow/status/connectit/connectit/ci.yml?branch=main)](https://github.com/connectit/connectit/actions)

**A decentralized peer-to-peer network for deploying and accessing AI models.**

ConnectIT behaves like a single giant computer. You configure a **Main Entry Point** once, and all your nodes—whether providers or clients—automatically connect, discover each other, and share work.

## ✨ Features

- 🌐 **Zero-Config Networking**: Set your Main Point once. No manual IP handling.
- 👁️ **Supervisor Monitoring**: The Main Point actively monitors network health.
- 💰 **Automated Economics**: Clients automatically route queries to the cheapest/fastest provider.
- 🔌 **HTTP API**: Monitor your entire mesh via a REST interface.

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/loayabdalslam/connectit.chatit.git
cd connectit

# Install with all dependencies
pip install -e .[all]
```

## 🚀 Usage

### 1. Start the Main Entry Point (Supervisor)

This server acts as the central hub (bootstrap) for your network.

```bash
# Start the supervisor. Note the P2P address (e.g., ws://192.168.1.15:4001)
python -m connectit api --port 8000
```

### 2. Configure Clients/Nodes (One-Time Setup)

On any machine you want to join the network, tell it where the supervisor is. You only do this **once**.

```bash
python -m connectit config bootstrap_url ws://192.168.1.15:4001
```

### 3. Deploy Providers (Zero Config)

Now, start as many providers as you want. You don't need to specify IPs or ports.

```bash
python -m connectit deploy-hf --model distilgpt2
```

The node will:
1.  Read the config to find the Main Point.
2.  Auto-assign a port.
3.  Join the mesh and announce its service.

### 4. Run Requests (Client)

Similarly, clients just run.

```bash
python -m connectit p2p-request "Hello AI" --model distilgpt2
```

## 🏗 Architecture

-   **Main Point**: The configured `bootstrap_url` is the heartbeat of the network. It gossips peer lists to everyone.
-   **Config Persistence**: Stored in `~/.connectit/config.json`.
-   **Dynamic Mesh**: Nodes can come and go; the mesh heals automatically.

## 🤝 Contributing

We welcome contributions! Please check the [issues](https://github.com/connectit/connectit/issues) page.

## License

Custom License (Non-Commercial). See [LICENSE](LICENSE) for details.
