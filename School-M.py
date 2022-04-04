## requests(html 파일 가져옴), bs4(추출한 html 분석)
import requests
from bs4 import BeautifulSoup
import datetime     ## 오늘 날짜를 구하기 위해 사용
from neispy import Neispy

현재 = str(datetime.datetime.now())
# print(현재)
## 20220401
날 = 현재[:4] + 현재[5:7] + 현재[8:10]
급식날 = 현재[:10] 
# print(날)

요일 = ["월", "화", "수", "목" ,"금"]
오늘날 = datetime.datetime.today().weekday()
# print(요일[오늘날])

name = "성일고등학교"


def main():

    neis = Neispy.sync()

    print(dir(neis))

    # 학교이름으로 학교정보를 요청하고 교육청코드 와 학교코드로 가져옵니다.
    scinfo = neis.schoolInfo(SCHUL_NM=name)
    AE = scinfo[0].ATPT_OFCDC_SC_CODE  # 교육청코드
    SE = scinfo[0].SD_SCHUL_CODE  # 학교코드

    # 학교코드와 교육청 코드로 2022년 04월 01일의 급식 정보 요청
    scmeal = neis.mealServiceDietInfo(AE, SE, MLSV_YMD=날)
    meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")  # 줄바꿈으로 만든뒤 출력

    print("[ 성일정보고등학교 급식 ]"+"\n"+급식날+" ("+(요일[오늘날])+")\n[중식]")
    print(meal)



main()
