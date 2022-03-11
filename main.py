import sys
from pathlib import Path
from subprocess import call
from typing import List
from googletrans import Translator

def pdf_to_txt(file_name:str):
    # pdfminer.sixのpdf2txtを実行する
    py_path = Path(sys.exec_prefix) / "Scripts" / "pdf2txt.py"
    call(["py", str(py_path), "-o output.txt", "-p 1", "extract-sample.pdf"])

def read_txt() -> List[str]:
    with open(" output.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def get_abst()->List[str]:
    # 論文のアブストのみを抽出する
    lines = read_txt()
    idx = 0
    for line in lines:
        if line == "Abstract\n":
            start = idx
        elif line == "Introduction\n":
            end = idx
            break
        idx += 1
    
    abst = [lines[i] for i in range(start+1, end)]
    abst_str = "".join(abst).replace("\n", "")
    abst = abst_str.split(".")
    return abst


def output_jp_txt(abst:List[str]):
    # 日本語に翻訳してtxtファイルに出力する
    tr = Translator()
    print("----input----")
    print(abst)
    
    for txt in abst:
        if txt == "\n": continue
        print(txt)
        jp_txt = tr.translate(txt, src="en", dest="ja").text
        print(jp_txt)
        with open(" output.txt", 'a', encoding='utf-8')as f:
            f.write(jp_txt+"\n")
    


def main():
    print("file_name(PDF):", end="")
    file_name= input()
    pdf_to_txt(file_name)
    abst = get_abst()
    output_jp_txt(abst)

def test():
    file_name = "extract-sample.pdf"
    pdf_to_txt(file_name)
    abst = get_abst()
    output_jp_txt(abst)


if __name__=="__main__":
    # main()
    test()
    