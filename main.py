STD_INPUT_HANDLE   = -10
STD_OUTPUT_HANDLE  = -11
STD_ERROR_HANDLE   = -12
FOREGROUND_BLACK     = 0x00
FOREGROUND_BLUE      = 0x01
FOREGROUND_GREEN     = 0x02
FOREGROUND_RED       = 0x04
FOREGROUND_INTENSITY = 0x08
BACKGROUND_BLUE      = 0x10
BACKGROUND_GREEN     = 0x20
BACKGROUND_RED       = 0x40
BACKGROUND_INTENSITY = 0x80

import sys
import school_food_language_pack.dic
import ctypes

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

while True:
    print('''
    대한민국 초중고생을 위한 급식어 사전
    1. 급식단어 -> 한국단어 번역
    2. 한국단어 -> 급식단어 번역
    3. 프로그램 종료
    ''')
    select = int(input("무엇을 하시겠습니까? : "))

    # 급식어 -> 한국어 번역
    if select == 1:
        translate_1 = input("변환을 원하는 급식단어를 입력해주십시오. : ")
        if translate_1 in school_food_language_pack.dic.school_food:
            set_color(4)
            print("\n\n"
                  "[" + translate_1 + "] 의 한국어로 변환 결과 : " + school_food_language_pack.dic.school_food[translate_1])

            continuee = int(input("\n\n계속 진행하시겠습니까? \n 1. 예 \n 2. 프로그램 종료 \n\n 입력 :"))

            if continuee == 2:
                sys.exit()

    # 한국어 -> 급식어 번역
    elif select == 2:
        translate_2 = input("번역을 원하는 한국어를 입력해주십시오. : ")
        if translate_2 in school_food_language_pack.dic.school_food_2_Korean:
            set_color(4)
            print("\n\n"
                  "[" + translate_2 + "] 의 급식어로 변환 결과 : " + school_food_language_pack.dic.school_food_2_Korean[translate_2])

            continueee = int(input("\n\n계속 진행하시겠습니까? \n 1. 예 \n 2. 프로그램 종료 \n\n\ 입력 : "))
            if continueee == 2:
                sys.exit()

    elif select == 3: # 프로그램 종료
        sys.exit()
