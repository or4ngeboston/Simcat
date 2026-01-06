# Use the official Playwright Python image (latest as of Jan 2026)
FROM mcr.microsoft.com/playwright/python:v1.57.0-noble

# Set working directory (Unix-style, avoids the bug)
WORKDIR /workspace

# Copy your code (done automatically by Jenkins)
# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Browsers are pre-installed; no need for playwright install