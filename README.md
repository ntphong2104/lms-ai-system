# LMS AI System

Hệ thống quản lý học tập trực tuyến (LMS) tích hợp Trợ lý AI hỗ trợ học tập.

## Tổng quan

Dự án xây dựng một nền tảng LMS với 3 vai trò chính:
- **Super Admin** — Quản trị hệ thống, tài khoản, cấu hình API AI
- **Giảng viên (Teacher)** — Quản lý khóa học, tài liệu, theo dõi tiến độ học viên
- **Học viên (Student)** — Học tập, chat với Trợ lý AI (RAG), làm bài thi, nhận OpenBadges

## Tính năng nổi bật

- 🤖 **Trợ lý AI (RAG Chatbot)** — Trả lời câu hỏi bám sát nội dung khóa học
- 📚 **Tự động Vector hóa tài liệu** — Upload PDF/Text → Chunking → Embedding → Vector DB
- 🛡️ **AI Guardrails** — 2 lớp kiểm soát Input/Output để đảm bảo an toàn
- 📦 **Hỗ trợ SCORM** — Bài giảng tương tác chuẩn quốc tế
- 🏅 **OpenBadges** — Chứng chỉ số chia sẻ lên LinkedIn
- 🎥 **Hỗ trợ 1-1 qua Google Meet**

## Tech Stack

| Thành phần | Công nghệ |
|---|---|
| Backend | FastAPI (Python) |
| Database | PostgreSQL |
| Vector DB | Qdrant / ChromaDB |
| Cache & Queue | Redis |
| LLM | Google Gemini API |
| Frontend | Next.js / React |
| Deployment | Docker Compose |

## Cấu trúc thư mục

```
lms-ai-system/
├── docs/                           # Tài liệu hệ thống
│   ├── 01_business_requirements.md
│   ├── 02_system_architecture.md
│   └── 03_database_schema.md
├── backend/
│   └── app/
│       ├── api/v1/                 # Endpoints
│       ├── core/                   # Config, Security, Rate Limiter
│       ├── models/                 # ORM Models
│       ├── services/               # Business Logic
│       ├── ai_engine/              # AI Logic (LLM, RAG, Guardrails)
│       └── worker/                 # Background Jobs
├── frontend/
├── docker-compose.yml
└── ai_instructions.md
```

## Tài liệu

- [01 — Đặc tả nghiệp vụ](docs/01_business_requirements.md)
- [02 — Kiến trúc hệ thống](docs/02_system_architecture.md)
- [03 — Database Schema](docs/03_database_schema.md)
