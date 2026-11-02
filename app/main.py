from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="End-to-End CI/CD Demo", version="1.0.0")


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>CI/CD Demo</title><style>
body{font:16px system-ui,sans-serif;max-width:760px;margin:12vh auto;padding:0 24px;color:#172033;background:#f5f7fb}
main{background:white;border:1px solid #e1e7f0;border-radius:16px;padding:36px;box-shadow:0 12px 40px #17203312}
.tag{display:inline-block;background:#e8f5ee;color:#167443;padding:6px 10px;border-radius:999px;font-size:13px}
h1{font-size:clamp(2rem,6vw,3.5rem);margin:20px 0 12px}p{line-height:1.65;color:#536078}
code{background:#f0f3f8;padding:3px 7px;border-radius:5px}
</style></head><body><main><span class="tag">● Service is running</span>
<h1>Deploy with confidence.</h1><p>This demo app is delivered by a GitHub Actions pipeline using Docker, Amazon ECR, and Kubernetes rolling updates.</p>
<p>Container health: <code>/health/live</code> · Readiness: <code>/health/ready</code></p></main></body></html>"""


@app.get("/health/live")
def liveness() -> dict[str, str]:
    return {"status": "alive"}


@app.get("/health/ready")
def readiness() -> dict[str, str]:
    return {"status": "ready"}
