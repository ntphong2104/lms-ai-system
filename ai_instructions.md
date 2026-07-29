# AI AGENT INSTRUCTIONS FOR LMS SYSTEM

## 1. VAI TRÒ VÀ TECH STACK
- Bạn là một Senior Backend Developer chuyên nghiệp.
- Tech Stack Backend: Python 3.11+, FastAPI, SQLAlchemy (Async), Alembic (Migrations), PostgreSQL, Redis, Qdrant (Vector DB).
- Tech Stack Frontend: Next.js, React, TailwindCSS.
- Nguyên tắc cốt lõi: Luôn viết code bất đồng bộ (async/await) cho tất cả các tác vụ I/O. Áp dụng chuẩn mã hóa PEP8 (sử dụng Ruff).

## 2. QUY TẮC KIẾN TRÚC PHẦN MỀM (LAYERED ARCHITECTURE)
Tuyệt đối tuân thủ cấu trúc phân lớp:
- `backend/app/api/`: Chỉ chứa endpoints (routes), parse request và response.
- `backend/app/services/`: Chứa toàn bộ logic nghiệp vụ, validation.
- `backend/app/ai_engine/`: CÔ LẬP TOÀN BỘ logic RAG, VectorDB, Chunking PDF, và gọi LLM API.
- `backend/app/worker/`: Background jobs xử lý file nặng.

## 3. THIẾT KẾ CƠ SỞ DỮ LIỆU & BẢO MẬT
- Soft Delete: Chỉ áp dụng `deleted_at` cho bảng `users` và `courses`.
- Hard Delete: Bảng `materials` (tài liệu) phải xóa thật trong DB, trên MinIO/S3 và Vector DB.
- JSONB: Dùng cột JSONB lưu `scorm_data` trong bảng `learning_progress`.
- Search: Dùng GIN index + extension `unaccent` của PostgreSQL để search Full-text Tiếng Việt. Tuyệt đối không dùng ILIKE quét toàn bảng.

## 4. TÍCH HỢP REDIS & BEST PRACTICES
- Rate Limit: Dùng Token Bucket trên Redis giới hạn 50 lượt chat/ngày/user.
- Semantic Caching: Cache lại câu trả lời AI cho các câu hỏi trùng lặp.
- Reset Password: Lưu token tạm vào Redis (TTL 15 phút), không tạo bảng SQL.

## 5. TÍCH HỢP AI & LLM 
- Không hardcode API Key. Đọc từ biến môi trường hoặc cấu hình động (`system_configs`).
- Data Isolation: Bắt buộc truyền `course_id` vào query filter của Vector DB để AI không lấy nhầm kiến thức môn học khác.
- Xử lý PDF: Tối ưu thư viện bóc tách text từ PDF, đảm bảo phân mảnh (chunking) chuẩn xác, tránh mất ngữ cảnh.
