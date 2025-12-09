# Manual Testing Guide

This guide explains how to manually test the Bee2Bee network using the CLI.

## Prerequisites
- Python 3.9+
- Virtual environment activated (`source .venv/bin/activate`)
- Dependencies installed (`pip install -e .`)

## 1. Start the API Server (Main Point)
The API server acts as the entry point and bootstrap node.

```bash
bee2bee api --host 127.0.0.1 --port 4002
```
*Keep this terminal open.*

## 2. Start a Model Provider
Deploy a Hugging Face model on the network.

```bash
bee2bee deploy-hf --model distilgpt2 --host 127.0.0.1 --port 0 --bootstrap-link http://127.0.0.1:4002
```
*Keep this terminal open.*

## 3. Make a Request (Client)
Request a generation from the network.

```bash
bee2bee p2p-request "Hello, world!" --model distilgpt2 --bootstrap-link http://127.0.0.1:4002
```

## 4. Configuration
You can view or set configuration values:

```bash
bee2bee config
bee2bee config bootstrap_url http://127.0.0.1:4002
```
