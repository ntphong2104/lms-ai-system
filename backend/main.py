# main.py
import sentry_sdk
from fastapi import FastAPI

# Khởi tạo Sentry giám sát lỗi
sentry_sdk.init(
    dsn="ĐƯỜNG_LINK_DSN_CỦA_BẠN_LẤY_TỪ_SENTRY.IO",
    traces_sample_rate=1.0,
)

app = FastAPI(title="LMS AI System")
