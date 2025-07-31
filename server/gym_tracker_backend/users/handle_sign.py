import requests
import hmac
import hashlib
import base64
import urllib.parse
import json
import os
import time
from dotenv import load_dotenv
import hashlib
from importlib import reload
import logging


logger = logging.getLogger(__name__)


def handle_sign(encoded_params: str):
    """Верификация подписи VK Mini Apps"""
    try:
        load_dotenv(override=True)
        secret = os.getenv("VK_APP_TOKEN")
        if not secret:
            raise ValueError("VK_APP_SECRET not found in .env")


        decoded = base64.urlsafe_b64decode(urllib.parse.unquote(encoded_params))
        params = json.loads(decoded)
        received_sign = params.pop('sign', '')


        vk_params = {
            k: str(v).strip() 
            for k, v in params.items() 
            if k.startswith('vk_') and v is not None
        }


        param_string = '&'.join(
            f"{k}={v}" 
            for k, v in sorted(vk_params.items(), key=lambda x: x[0])
        )


        signature = base64.urlsafe_b64encode(
            hmac.new(
                secret.encode('utf-8'),
                param_string.encode('utf-8'),
                hashlib.sha256
            ).digest()
        ).decode('utf-8').rstrip('=')


        if not hmac.compare_digest(signature, received_sign):
            print(f"Подпись не совпадает\nОжидалось: {signature}\nПолучено: {received_sign}")
            return None

        return params

    except Exception as e:
        print(f"Ошибка верификации: {str(e)}")
        return None
    

if __name__ == "__main__":
    string = "eyJ2a19hY2Nlc3NfdG9rZW5fc2V0dGluZ3MiOiIiLCJ2a19hcHBfaWQiOjUzOTQ2NTgwLCJ2a19hcmVfbm90aWZpY2F0aW9uc19lbmFibGVkIjowLCJ2a19pc19hcHBfdXNlciI6MSwidmtfaXNfZmF2b3JpdGUiOjAsInZrX2xhbmd1YWdlIjoicnUiLCJ2a19wbGF0Zm9ybSI6Im1vYmlsZV93ZWIiLCJ2a19yZWYiOiJvdGhlciIsInZrX3RzIjoxNzUzNjM1MjE1LCJ2a191c2VyX2lkIjo1OTE3Mjc5OTcsInNpZ24iOiJmTDREY2VINHcxVDBYSk8tSm4tck1ERWxMcmx6STQ5QzNMb1pPNWtPOFJrIn0="
    real = "fL4DceH4w1T0XJO-Jn-rMDElLrlzI49C3LoZO5kO8Rk"
    print(handle_sign(string))