# eBayOS - Multi-Platform Seller Control Plane

A modern web application for eBay sellers to manage inventory, crosslist items across multiple platforms, handle buyer communications, and track analytics—all from one unified dashboard.

**Status:** Production-Ready ✅ | **Version:** 1.1

---

## 🎯 Features

- **Dashboard** - Command palette with AI intent parsing, smart suggestions, and market insights
- **Inventory Management** - Browse, search, and bulk-select items for crosslisting
- **Crosslist Operations** - Send items to Poshmark, eBay, and Facebook Marketplace with auto-fill via Chrome extension
- **Messages** - View and respond to buyer inquiries with AI-powered suggestions (Phase 5)
- **Orders** - Track shipments and order status across platforms
- **Vision Uplink** - Upload product images and listing details
- **Analytics** - Revenue trends, conversion funnels, performance metrics, and inventory health
- **Chrome Extension** - Auto-fill Poshmark listings from the control plane

---

## 🚀 Quick Start

### Prerequisites
- **Node.js** 18+ (includes npm)
- **Docker** (for production deployment)
- **Chrome** (for extension support)

### Local Development

```bash
# 1. Install dependencies
npm install

# 2. Set API keys in .env.local
cp .env.example .env.local
# Edit .env.local with your Gemini API key and backend URL

# 3. Start development server
npm run dev
# Opens at http://localhost:5173
```

### Production Deployment

```bash
# 1. Build for production
npm run build

# 2. Deploy Docker container
docker-compose up -d --build
# App available at http://localhost:4873 (or configured PORT)
```

---

## 📁 Project Structure

```
eBayOS/
├── src/
│   ├── components/          # React UI components
│   │   ├── Dashboard.tsx
│   │   ├── InventoryPage.tsx
│   │   ├── CrosslistPage.tsx
│   │   ├── MessagesPage.tsx
│   │   ├── OrdersPage.tsx
│   │   ├── AnalyticsPage.tsx
│   │   └── ...
│   ├── services/            # Business logic
│   │   ├── intentParser.ts   # AI command parsing
│   │   ├── spellExecutor.ts  # Command execution
│   │   └── ...
│   ├── types.ts             # TypeScript definitions
│   └── App.tsx              # Main app component
│
├── extension/               # Chrome extension source
│   ├── manifest.json
│   ├── bridge-content.js    # App ↔ Extension messaging
│   ├── poshmark-content.js  # Poshmark auto-fill
│   └── ...
│
├── public/                  # Static assets
├── dist/                    # Built frontend (gitignored)
├── package.json
├── tsconfig.json
├── vite.config.ts
├── server.ts                # Express.js backend proxy
├── Dockerfile
├── docker-compose.yml
├── ARCHITECTURE.md          # System design docs
├── DEPLOYMENT.md            # Deployment guide
└── README.md               # This file
```

---

## 🛠️ Configuration

### Environment Variables

Create `.env.local` based on `.env.example`:

```env
# Gemini API key for AI command parsing
VITE_GEMINI_API_KEY=your_gemini_api_key_here

# Backend service URL (eBay listing assistant)
BACKEND_URL=http://ebay-listing-assistant:5000

# Server configuration
NODE_ENV=development
PORT=3000
USE_HTTP=1
```

**Note:** API keys are only used server-side. Never commit `.env` files.

---

## 📦 Available Scripts

```bash
npm run dev       # Start Vite dev server with hot reload
npm run build     # Build production bundle (dist/)
npm run preview   # Preview production build locally
npm run type-check # Check TypeScript without emitting code
```

---

## 🐳 Docker Deployment

### Build & Run

```bash
docker-compose up -d --build
```

### Configuration in `docker-compose.yml`

```yaml
environment:
  - NODE_ENV=production
  - PORT=4873
  - USE_HTTP=1
  - BACKEND_URL=http://ebay-listing-assistant:5000
  - VITE_GEMINI_API_KEY=${VITE_GEMINI_API_KEY}
```

Set environment variables in your host system or `.env` file in the project root.

### Access the App

```
http://localhost:4873
```

---

## 🧩 Chrome Extension Setup

1. **Build the extension:**
   - Extension source is in `extension/` directory
   - Manifest configured for localhost and production URLs

2. **Load in Chrome:**
   - Open `chrome://extensions`
   - Enable "Developer mode"
   - Click "Load unpacked"
   - Select `extension/` folder

3. **Features:**
   - Auto-fill Poshmark listings from eBayOS
   - Syncs item data (title, price, images, size, brand)
   - Real-time messaging bridge with app

---

## 🔗 API Architecture

### Frontend → Backend Proxy

All `/api/*` requests are proxied to the eBay listing assistant backend:

```
Browser Request
  ↓
Express Server (server.ts)
  ↓
Proxy Middleware
  ↓
Backend Service (http://backend:5000)
  ↓
Response to Browser
```

### Mock Endpoints (for offline development)

- `GET /api/active-listings` - Sample inventory
- `GET /api/messages` - Sample conversations
- `GET /api/status` - Health check

### Real Endpoints (Backend)

- All other `/api/*` calls forwarded to backend service
- Automatically uses mock data if backend is unavailable

---

## 🧪 Testing

### Browser Testing

```bash
npm run dev
# Navigate to http://localhost:5173
# Test each page: Dashboard, Inventory, Crosslist, Messages, Orders, Analytics
```

### Console Validation

Open DevTools (F12) → Console tab to check for errors while testing features.

### Extension Testing

1. Open app at http://localhost:5173
2. Open Poshmark in another tab
3. Click Crosslist → Select items → Send to Poshmark
4. Extension should auto-fill the form

---

## 🚨 Troubleshooting

### App Not Loading

```bash
# Hard refresh browser
Ctrl+Shift+R  # Windows
Cmd+Shift+R   # Mac

# Check npm dev server logs
npm run dev

# Verify API backend is running
curl http://localhost:5000/health
```

### Docker Container Issues

```bash
# View logs
docker logs ebayos -f

# Restart container
docker-compose restart

# Full rebuild
docker-compose down
docker image rm ebayos:latest
docker-compose up -d --build
```

### Extension Not Connecting

1. Check extension is enabled: `chrome://extensions`
2. Reload extension (F5 or Reload button)
3. Verify manifest.json has correct URLs
4. Check browser console for errors

---

## 📚 Architecture & Docs

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - System design, data flow, and critical issues
- **[DEPLOYMENT.md](./DEPLOYMENT.md)** - Production deployment on Docker/CasaOS
- **[EXTENSION_DEBUG.md](./EXTENSION_DEBUG.md)** - Extension troubleshooting guide

---

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make changes and test locally with `npm run dev`
3. Build for production: `npm run build`
4. Commit with clear messages: `git commit -m "feat: description"`
5. Push and open a Pull Request

---

## 📋 Development Workflow

### Adding a New Component

1. Create `src/components/YourComponent.tsx`
2. Export from `src/App.tsx`
3. Add route/menu item in Sidebar
4. Test with `npm run dev`
5. Build and verify: `npm run build`

### Adding API Endpoints

1. Add route in `server.ts` (for mocks) or forward to backend
2. Create service in `src/services/` if needed
3. Call from component with `fetch('/api/your-endpoint')`
4. Test in browser console: `await fetch('/api/endpoint').then(r => r.json())`

### Updating the Extension

1. Modify files in `extension/`
2. Reload extension in Chrome
3. Test functionality end-to-end

---

## 🎯 Next Phase: Smart Messages (Phase 5)

Planned features:
- AI intent detection (price inquiry, shipping question, bulk order, complaint, praise)
- Gemini-powered response suggestions
- Message analysis with Seller DNA context
- Notification badges on navigation items

---

## 📝 License

This project is proprietary. All rights reserved.

---

## 🆘 Support

For issues, check:
1. Browser console (F12 → Console)
2. Server logs (`npm run dev` or `docker logs ebayos`)
3. [DEPLOYMENT.md](./DEPLOYMENT.md) troubleshooting section
4. Extension debug guide for Chrome extension issues

---

**Built with:** React + TypeScript + Vite + Express + Docker

**Last Updated:** March 15, 2026 | **Status:** Production-Ready ✅
