from ctypes import CDLL, c_wchar_p, byref
from gc import collect
from .error import (
    DllNotFoundError
)

class XdocToTxt:
    def __init__(self, dll_path: str|None=None):
        self.dll_path = dll_path if dll_path is not None else "./modules/xdoc2txt/dll/xd2txlib.dll"

    def __call__(self, file_path: str) -> str|None:
        file_text = c_wchar_p()

        # DLLの読み込み
        try:
            xdoc_to_txt = CDLL(self.dll_path)

        except OSError as e:
            print(e.args)
            raise DllNotFoundError(e.args)

        # テキスト抽出
        else:
            xdoc_to_txt.ExtractText(file_path, False, byref(file_text))
            return file_text.value

        finally:
            collect()