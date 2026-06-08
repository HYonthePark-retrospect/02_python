# PypI(Python Package Index)
# - python 패키지를 올리고 내려받는 공식 저장소
from ast import List

# pip : PyPI에서 패키지를 검색, 설치, 삭제하는 도구

# requirements.txt : 프로젝트에 필요한 패키지 목록을 적어두는 파일
#  -> 해당 패키지 목록을 이용해서 일괄 설치 가능
#  = 의존성 명세 파일

# requirements.txt 예시 내용
sample_requirements = """
# 웹 요청 라이브러리
requests==2.32.3

# 환경변수 파일(.env) 로딩
python-dotenv>=1.0.1

# 테스트 도구
pytest~=8.3.0
"""


pip_commands = [
    "python -m venv .venv", # venv라는 가상환경 생성(가상환경 폴더명 .venv)
    ".venv\\Scripts\\activate", # windows
    "source .venv/bin/activate", # mac, lnux
    "python -m pip --version", # pip 가상환경 버전 확인
    "python -m pip install requests", # 가상환경 패키지 설치
    "python -m pip show requests", # 설치된 request 패키지 정보 출력
    "python -m pip freeze > requirements.txt", # 현재 가상환경에 설치된 패키지 목록을 requirements.txt 파일로 저장
    "python -m pip install -r requirements.txt", #requirements.txt에 적힌 패키지를 한 번에 설치
    "python -m pip uninstall (패키지명)requests", #필요없는 패키지 지우는 방법
]

# 필수 패키지 목록
REQUIRED_PACKAGES = {
    'requests' : 'requests',
    'colorama' : 'colorama',
    'dotenv': 'python-dotenv'
}

from importlib import  import_module
from importlib.metadata import version, PackageNotFoundError
from io import StringIO

def find_missing_packages() -> list[str]:
    """ requirements.txt 작성된 패키지가 설치 되어 있는지 확인"""

    missing_packages = [] # 설치 안된 패키지를 저장한 list

    for package_name in REQUIRED_PACKAGES:
        try:
            # 패키지 버전 정보를 문자열로 반환
            # 단, 해당 패키지가 설치되어있지 않다면
            # PackageNotFoundError 발생
            version(package_name)
        except PackageNotFoundError:
            missing_packages.append(package_name)

    return missing_packages

def print_installed_versions() -> None:
    """ 설치된 필수 패키지 버전 출련(pip list) """
    for package_name in REQUIRED_PACKAGES:
        print(f'{package_name}=={version(package_name)}')


def print_import_results() -> None:
    """ 설치된 패키지를 실제 Python 모듈로 Import 가능한지 확인 """
    for package_name, module_name in REQUIRED_PACKAGES.items():
        import_module(module_name) # 동적 import
        print(f'{package_name}->{module_name} import 성공')

# 필수 패키지 중 설치되지 않은 패키지 list를 반환받아 저장
missing_packages = find_missing_packages()

if missing_packages: # list에 요소가 있다면 True
    print('설치 되지 않은 패키지:', missing_packages)

    for package_name in missing_packages:
        print(f'python -m pip install {package_name}')
else: # list가 비어있다면 False
    print('필수 패키지가 모두 설치 되어 있습니다')
    print_installed_versions()
    print_import_results()
