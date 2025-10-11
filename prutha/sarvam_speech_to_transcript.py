import asyncio
from sarvamai import AsyncSarvamAI

async def main():
    client = AsyncSarvamAI(api_subscription_key="YOUR_API_KEY")

    job = await client.speech_to_text_job.create_job(
        language_code="en-IN",
        model="saarika:v2.5",
        with_timestamps=True,
        with_diarization=True,
        num_speakers=2
    )

    audio_paths = ["path/to/audio.mp3"]
    await job.upload_files(file_paths=audio_paths)

    await job.start()

    final_status = await job.wait_until_complete()

    if await job.is_failed():
        print("STT job failed.")
        return

    output_dir = "./output"
    await job.download_outputs(output_dir=output_dir)
    print(f"Output downloaded to: {output_dir}")

if __name__ == "__main__":
    asyncio.run(main())

# --- Notebook/Colab usage ---
# await main()
