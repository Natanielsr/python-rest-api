import os
import sys

def resource_path(relative_path):
    """Retorna o caminho absoluto compatível com PyInstaller e desenvolvimento"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        # Pega o diretório do arquivo atual e volta um nível para a raiz do projeto
        base_path = os.path.dirname(os.path.abspath(__file__))

    parts = relative_path.replace("\\", "/").split("/")
    return os.path.join(base_path, *parts)