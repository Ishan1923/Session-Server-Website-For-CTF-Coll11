# 🕹️ Session Server Website for CTF Multiplayer Game

Welcome to the backend session manager for a **multiplayer Capture The Flag (CTF)** game built with **Unity + Photon**!  
This project ensures that even if a player gets disconnected mid-game — due to poor internet, accidental exit, or system crash — they can **rejoin seamlessly**, without losing team progress or answered questions.

---

## 🎯 Purpose

In fast-paced multiplayer games, especially during CTF competitions, players often face issues like:
- Accidental disconnections
- Sudden game/app crashes
- Network lag or session timeouts

**This server ensures continuity.** It:
- **Persists team scores**
- **Tracks answered question IDs**
- **Allows smooth re-entry into a previously joined room**

---

## 💡 Key Features

✅ **Session Persistence**  
- Stores session data on a per-team basis (score + answered questions)

✅ **Rejoin Support**  
- Recovers state for players who rejoin mid-match

✅ **Lightweight & Fast**  
- Built to handle quick read/write cycles suitable for real-time games

✅ **Photon-Friendly**  
- Designed around Photon Unity Networking session mechanics

---

## 🛠️ Tech Stack

- 🐍 **Python**
- 🌐 **Django** for backend and API endpoints
- 🛢️ **PostgreSQL** (or any SQL-based DB via Django ORM)
- ☁️ **GCP / Cloud hosting** compatible
- 🔄 **REST APIs** for session updates and fetches

---

## 🌍 How It Works

1. **During gameplay**:
   - Players answer questions
   - Team score and answered question IDs are sent to the server

2. **If a player disconnects**:
   - Their Photon session may be lost
   - But their team progress remains intact

3. **Upon rejoining**:
   - The client queries the server
   - Restores previously saved session data

---

## 🧪 API Preview (Example)

```http
GET /api/team/<team_name>/
→ Returns: { "score": 140, "answered_ids": [1, 4, 7] }

POST /api/update/
→ Payload: { "team_name": "RedTeam", "score": 150, "answered_ids": [1, 4, 7, 10] }
