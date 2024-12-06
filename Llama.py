from huggingface_hub import snapshot_download

# Lade das Modell herunter
snapshot_download(
    repo_id="meta-llama/Llama-3.2-1B",
    cache_dir="./models",
    use_auth_token="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"
)
