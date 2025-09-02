# -----------------------------
# Step 1: Base image
# -----------------------------
FROM python:3.13-slim-bookworm

# -----------------------------
# Step 2: Set environment variables
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

# -----------------------------
# Step 3: Set working directory
# -----------------------------
WORKDIR /app

# -----------------------------
# Step 4: Install system dependencies
# -----------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Step 5: Install Python dependencies
# -----------------------------
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Step 6: Copy application code
# -----------------------------
COPY . .

# -----------------------------
# Step 7: Expose Streamlit port
# -----------------------------
EXPOSE 8501

# -----------------------------
# Step 8: Run Streamlit app
# -----------------------------
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
