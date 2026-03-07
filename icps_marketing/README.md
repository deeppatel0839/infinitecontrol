# ∞ Infinite Control Panel System Inc.
## Marketing Website — Python Flask + SQLite

### 📁 Structure
```
icps_marketing/
├── app.py               ← Flask server (3 routes)
├── inquiries.db         ← SQLite DB (auto-created)
├── templates/
│   ├── index.html       ← Full marketing website
│   └── inquiries.html   ← View saved inquiries
└── README.md
```

### 🚀 Run It
```bash
pip install flask
cd icps_marketing
python app.py
```
Open → **http://127.0.0.1:5000**

### 🗄️ How Database Works
- Visitor fills out contact form → clicks Submit
- Form data POSTs to `/submit` (Flask route)
- Flask saves to `inquiries.db` (SQLite, auto-created)
- View all saved inquiries at `/inquiries`

### 📄 Pages
| URL | Description |
|-----|-------------|
| `/` | Full marketing website |
| `/submit` | POST endpoint — saves inquiry to DB |
| `/inquiries` | View all saved inquiries (admin) |

### 📧 Contact
**Darpan Patel** — dp83364@gmail.com
