# 1️⃣ Use official lightweight Python image
FROM python:3.12-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy requirements.txt first (for caching)
COPY requirements.txt .

# 4️⃣ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy your FastAPI app code
COPY ./app ./app

# 6️⃣ Expose port 8000 for FastAPI
EXPOSE 8000

# 7️⃣ Command to run FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]