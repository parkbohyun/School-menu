
import datetime     ## 오늘 날짜를 구하기 위해 사용
from neispy import Neispy

T_day = str(datetime.datetime.now())        # 오늘 날짜를 구함

D_day = T_day[:4] + T_day[5:7] + T_day[8:10]       # 오늘 날짜를 바탕으로 "년월일" 을 구함
DD_day = T_day[:10]         # 오늘 날짜를 바탕으로 "년-월-일" 을 구함

W_day = ["월", "화", "수", "목" ,"금"]      # datetime 모듈을 이용하여 숫자로 구한 요일을 텍스트 형테로 변환
WN_day = datetime.datetime.today().weekday()    # datetime 모듈을 이용하여 오늘의 요일을 숫자로 구함

name = "성일고등학교"

def main():

    neis = Neispy.sync()

    print(dir(neis))

    scinfo = neis.schoolInfo(SCHUL_NM=name)     # 학교이름으로 학교정보를 요청하고 교육청코드 와 학교코드로 가져옵니다.
    AE = scinfo[0].ATPT_OFCDC_SC_CODE       # 교육청코드
    SE = scinfo[0].SD_SCHUL_CODE        # 학교코드

    scmeal = neis.mealServiceDietInfo(AE, SE, MLSV_YMD=D_day)         # 학교코드와 교육청 코드로 2022년 04월 01일의 급식 정보 요청
    meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든뒤 출력

    print("[ 성일정보고등학교 급식 ]"+"\n"+DD_day+" ("+(W_day[WN_day])+")\n[중식]")
    print(meal)

main()
