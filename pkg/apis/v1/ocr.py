"""
Copyright (c) 2018 hu. All rights reserved.
Personal code, only for learning and communication.
You can contact me in the following ways:
    stonebirdjx <1245863260@qq.com, g1245863260@gmail.com>
    https://www.hjxstbserver.xyz/
File: ocr  2022/6/11 10:18
Desc: deal with ocr handle
"""
import easyocr


class Ocr(object):
    """Ocr is deal website ocr handler"""

    def __init__(self, lang: [], pic_name: str) -> None:
        self.__lang = lang
        self.__pic_name = pic_name

    def read_data(self) -> []:
        """
        Image text extraction
        :return:[]
        """
        reader = easyocr.Reader(self.__lang, gpu=False)
        result = reader.readtext(self.__pic_name)
        return result
