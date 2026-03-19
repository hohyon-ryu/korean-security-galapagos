"""Generate banner/hero images for Korean IT infrastructure website using Gemini API."""

import base64
import time
from pathlib import Path
from google import genai
from google.genai import types

API_KEY = "AIzaSyBGKyzEZCAdbBqKBwi41SgWLmmrQ2w96x8"
MODEL = "gemini-2.5-flash-preview-05-20"
OUTPUT_DIR = Path("/Users/will_ryu/workspace/personal/korean_it/결제보안/docs/img")

client = genai.Client(api_key=API_KEY)

IMAGES = [
    {
        "filename": "hero-banner.png",
        "prompt": (
            "Create a wide illustration (1200x600 pixels) in warm pastel tones (peach, cream, soft coral). "
            "A frustrated Korean office worker staring at a computer screen covered with dozens of security program "
            "installation popup windows. The popups say things like 'Install Security Module', 'ActiveX Required', "
            "'Certificate Needed'. Korean office setting with fluorescent lights. "
            "Illustration style, flat design, not photo-realistic. Clean lines, modern vector art style."
        ),
        "aspect_ratio": "2:1",
    },
    {
        "filename": "problem-auth.png",
        "prompt": (
            "Create a square illustration (800x800 pixels) in warm coral and peach tones. "
            "A person looking overwhelmed and drowning in a sea of authentication devices: "
            "passwords floating in the air, USB security sticks, security cards, OTP token devices, "
            "phone screens showing verification codes, certificate files. "
            "The person has an exhausted, overwhelmed expression. "
            "Illustration style, flat design, modern vector art. Not photo-realistic."
        ),
        "aspect_ratio": "1:1",
    },
    {
        "filename": "problem-wall.png",
        "prompt": (
            "Create a wide illustration (1200x600 pixels) in mint and green tones. "
            "Left side: a Korean government worker sitting at a desk, blocked by a huge brick wall. "
            "The wall has Korean text '망분리' (network separation) written on it in large letters. "
            "Right side of the wall: workers from other countries happily using AI, chatbots, and modern tools "
            "with smiles on their faces. Strong contrast between the two sides. "
            "Illustration style, flat design, modern vector art. Not photo-realistic."
        ),
        "aspect_ratio": "2:1",
    },
    {
        "filename": "solution-fingerprint.png",
        "prompt": (
            "Create a square illustration (800x800 pixels) in bright, optimistic spring green tones. "
            "A clean, minimal smartphone screen showing a simple fingerprint icon being touched by a finger. "
            "One touch authentication concept. Glowing green success indicator. "
            "Very clean, minimal design with lots of white space. Modern, fresh, optimistic feeling. "
            "Flat design illustration style, not photo-realistic."
        ),
        "aspect_ratio": "1:1",
    },
]


def generate_image(image_config: dict) -> None:
    """Generate a single image and save it."""
    filename = image_config["filename"]
    output_path = OUTPUT_DIR / filename
    print(f"\n--- Generating: {filename} ---")
    print(f"Prompt: {image_config['prompt'][:80]}...")

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=image_config["prompt"],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(
                    aspect_ratio=image_config["aspect_ratio"],
                ),
            ),
        )

        # Extract image data from response
        saved = False
        if response.candidates:
            for part in response.candidates[0].content.parts:
                if hasattr(part, "inline_data") and part.inline_data:
                    image_data = part.inline_data.data
                    mime_type = part.inline_data.mime_type
                    print(f"  Got image data, mime_type: {mime_type}")

                    # If data is base64-encoded string, decode it
                    if isinstance(image_data, str):
                        image_data = base64.b64decode(image_data)

                    with open(output_path, "wb") as f:
                        f.write(image_data)

                    print(f"  Saved to: {output_path}")
                    saved = True
                    break

        if not saved:
            print(f"  WARNING: No image data in response for {filename}")
            print(f"  Response: {response}")

    except Exception as e:
        print(f"  ERROR generating {filename}: {e}")
        raise


def main():
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Model: {MODEL}")

    for i, img_config in enumerate(IMAGES):
        generate_image(img_config)
        # Small delay between requests to avoid rate limiting
        if i < len(IMAGES) - 1:
            print("  Waiting 5 seconds before next request...")
            time.sleep(5)

    print("\n=== Done! ===")


if __name__ == "__main__":
    main()
