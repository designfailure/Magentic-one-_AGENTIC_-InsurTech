import os
from dotenv import load_dotenv
from typing import Dict, Any
import logging

def setup_logging(logs_dir: str) -> None:
    """Nastavitev beleženja dogodkov"""
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(logs_dir, 'app.log')),
            logging.StreamHandler()
        ]
    )

def load_environment() -> None:
    """Nalaganje okoljskih spremenljivk"""
    load_dotenv()
    required_vars = [
        'OPENAI_API_KEY',
        'TOGETHER_API_KEY',
        'STRIPE_API_KEY'
    ]
    
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        raise EnvironmentError(f"Manjkajoče okoljske spremenljivke: {', '.join(missing)}")

def process_image_data(image_path: str) -> Dict[str, Any]:
    """Obdelava vhodne slike"""
    from PIL import Image
    
    try:
        with Image.open(image_path) as img:
            return {
                "path": image_path,
                "size": img.size,
                "format": img.format,
                "mode": img.mode
            }
    except Exception as e:
        logging.error(f"Napaka pri obdelavi slike: {str(e)}")
        return {}