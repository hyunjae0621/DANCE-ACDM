# backend/backend/settings/env.py
import os
from pathlib import Path
from dotenv import load_dotenv

# .env 파일 로드
env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(env_path)

# 환경변수 로드 함수
def get_env_variable(var_name: str, default=None):
    """환경변수를 가져오는 헬퍼 함수"""
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        error_msg = f'Set the {var_name} environment variable'
        raise Exception(error_msg)

# 주요 환경변수 설정
DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = get_env_variable('SECRET_KEY')
ALLOWED_HOSTS = get_env_variable('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# JWT 설정
JWT_SECRET_KEY = get_env_variable('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_LIFETIME = get_env_variable('JWT_ACCESS_TOKEN_LIFETIME', '1h')
JWT_REFRESH_TOKEN_LIFETIME = get_env_variable('JWT_REFRESH_TOKEN_LIFETIME', '7d')

# 이메일 설정
EMAIL_HOST = get_env_variable('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(get_env_variable('EMAIL_PORT', 587))
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True