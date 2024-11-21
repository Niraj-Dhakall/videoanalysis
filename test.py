import vid2cleantxt

text_output_dir, metadata_output_dir = vid2cleantxt.transcribe.transcribe_dir(
    input_dir="venv/videos/",
    model_id="openai/whisper-base.en",
    chunk_length=30,
)

# do things with text files in text_output_dir
