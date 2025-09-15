# Dockerfile example
FROM huggingface/transformers-pytorch-gpu

# Install Python, pip, Node.js, Git, Fish
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv git curl nodejs npm fish && \
    rm -rf /var/lib/apt/lists/*

# Optional: Install uv & gitmoji-cli
RUN pip3 install uv && npm install -g gitmoji-cli