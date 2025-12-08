# ConnectIT Desktop App

<div align="center">
  
  ![ConnectIT](https://img.shields.io/badge/ConnectIT-Desktop-blue)
  ![Tauri](https://img.shields.io/badge/Tauri-2.0-24C8D8?logo=tauri)
  ![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
  ![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?logo=typescript)

</div>

A modern desktop application for managing and monitoring the **ConnectIT** decentralized AI network. Built with Tauri, React, and TypeScript for native performance and a beautiful user interface.

---

## ✨ Features

- **🛡️ Network Administration**: Monitor active peers, health status, and network metrics in real-time
- **💬 AI Chat Interface**: Interact with distributed AI models across the P2P network
- **🎨 Modern UI**: Beautiful interface with custom title bar, animations, and dark mode
- **⚡ Native Performance**: Powered by Tauri for lightweight, fast desktop experience
- **🔌 Dynamic API Connection**: Connect to local or remote ConnectIT instances
- **📊 Real-time Metrics**: View CPU, RAM, and GPU usage of network peers
- **🔄 Auto-updates**: Built-in updater for seamless version management

---

## 🚀 Quick Start

### Prerequisites

- **Node.js** 20+ ([Download](https://nodejs.org/))
- **Rust** ([Install](https://www.rust-lang.org/tools/install))
- **ConnectIT API** running locally or remotely

### Installation

1. **Clone the repository** (if not already):

   ```bash
   git clone https://github.com/MohammedEAbdelAziz/BEE2BEE.git
   cd BEE2BEE/tauri-app
   ```

2. **Install dependencies**:

   ```bash
   npm install
   ```

3. **Run in development mode**:

   ```bash
   npm run tauri dev
   ```

4. **Build for production**:

   ```bash
   npm run tauri build
   ```

   Built applications will be in `src-tauri/target/release/bundle/`

---

## 🎯 Usage

### First Launch

1. The app connects to `http://127.0.0.1:4002` by default
2. Click the ⚙️ settings icon to configure a different API endpoint
3. Enter the URL of your ConnectIT API instance and click "Connect"

### Network Admin View

- **Overview**: See connected API endpoint and online status
- **Active Peers**: Monitor all connected nodes with latency and health metrics
- **System Config**: Add or remove bootstrap entry points
- **Metrics**: Real-time CPU, RAM, and GPU usage per peer

### AI Chat View

- Select an available AI model from connected peers
- Type your message and press Enter or click Send
- View conversation history with timestamps
- Clear chat or switch between models

---

## 🏗️ Tech Stack

| Technology        | Purpose                                        |
| ----------------- | ---------------------------------------------- |
| **Tauri 2.0**     | Native desktop framework (Rust backend)        |
| **React 19**      | UI framework with hooks                        |
| **TypeScript**    | Type-safe development                          |
| **Vite**          | Fast build tool and dev server                 |
| **TailwindCSS 4** | Utility-first styling                          |
| **Framer Motion** | Smooth animations                              |
| **Lucide React**  | Beautiful icon library                         |
| **shadcn/ui**     | Component library (Button, Card, Input, Badge) |

---

## 📁 Project Structure

```
tauri-app/
├── src/                    # React frontend
│   ├── App.tsx            # Main application component
│   ├── components/        # UI components (Button, Card, etc.)
│   ├── lib/               # Utilities (cn helper)
│   └── assets/            # Static assets
├── src-tauri/             # Tauri/Rust backend
│   ├── src/
│   │   ├── main.rs       # Rust entry point
│   │   └── lib.rs        # Tauri setup
│   ├── tauri.conf.json   # Tauri configuration
│   ├── Cargo.toml        # Rust dependencies
│   └── icons/            # App icons
├── package.json           # npm dependencies
└── vite.config.ts        # Vite configuration
```

---

## 🔧 Configuration

### API Connection

The app stores the API URL in localStorage. To change it:

- Click the ⚙️ settings icon in the bottom left
- Enter the new API URL (e.g., `http://192.168.1.100:4002`)
- Click "Connect"

### Custom Title Bar

The app uses a custom frameless window with native controls:

- **Minimize**: `_` button
- **Maximize**: `□` button
- **Close**: `×` button

### Environment Variables

Create a `.env` file for custom defaults:

```env
VITE_API_URL=http://127.0.0.1:4002
```

---

## 🛠️ Development

### Available Scripts

```bash
npm run dev          # Start Vite dev server only
npm run build        # Build frontend for production
npm run preview      # Preview production build
npm run tauri dev    # Run Tauri app in development
npm run tauri build  # Build production app
```

### Adding New Features

1. **Frontend components**: Add to `src/components/`
2. **UI utilities**: Extend `src/lib/utils.ts`
3. **Backend commands**: Add to `src-tauri/src/lib.rs`
4. **Icons**: Import from `lucide-react`

### Styling Guidelines

- Use TailwindCSS utility classes
- Follow the existing color scheme (primary, secondary, muted)
- Use `cn()` helper for conditional classes
- Maintain dark mode compatibility

---

## 📦 Building & Distribution

### Build for Your Platform

```bash
npm run tauri build
```

**Output locations**:

- **Windows**: `src-tauri/target/release/bundle/msi/` or `nsis/`
- **macOS**: `src-tauri/target/release/bundle/dmg/` or `app/`
- **Linux**: `src-tauri/target/release/bundle/deb/` or `appimage/`

### Multi-Platform Builds

See `.github/workflows/actions.yaml` for automated builds via GitHub Actions.

For release instructions, see [UPDATE_INSTRUCTIONS.md](./UPDATE_INSTRUCTIONS.md)

---

## 🐛 Troubleshooting

**App won't start?**

- Ensure Rust is installed: `rustc --version`
- Clear Cargo cache: `cd src-tauri && cargo clean`
- Reinstall dependencies: `rm -rf node_modules && npm install`

**Can't connect to API?**

- Verify the API is running: `curl http://127.0.0.1:4002/docs`
- Check firewall settings
- Try the full URL with `http://`

**Build fails on Windows?**

- Install [WebView2](https://developer.microsoft.com/en-us/microsoft-edge/webview2/)
- Run as administrator if permission errors occur

**Build fails on Linux?**

- Install system dependencies:
  ```bash
  sudo apt install libwebkit2gtk-4.1-dev \
    libappindicator3-dev librsvg2-dev patchelf
  ```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is part of the **ConnectIT** ecosystem. See the root [LICENSE](../LICENSE) file for details.

---

## 🔗 Related Projects

- [ConnectIT Core](../README.md) - Python P2P networking backend
- [Electron App](../desktop-app/) - Alternative Electron-based desktop app
- [Cloud Notebooks](../notebook/) - Google Colab integration

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/MohammedEAbdelAziz/BEE2BEE/issues)
- **Discussions**: [GitHub Discussions](https://github.com/MohammedEAbdelAziz/BEE2BEE/discussions)
- **Documentation**: See main [README](../README.md)
