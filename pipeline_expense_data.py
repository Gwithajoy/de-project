from sort_and_download import sort_by_location_year_month
import navigation_crawler
from navigation_crawler import get_driver
from navigation_crawler import set_location_and_crawling,login,goto_bigdata_navigation_page, set_year_date
from send_mysql import to_mysql

#다른 모듈의 펑션을 쓰기위한 과정 =>터미널에서와 같이 직접 호출되어 사용될 때는 그 자체로 기능을 수행하고, 동시에 다른 모듈에서 필요한 함수 등을 제공할 수 있다
if __name__ == '__main__':
    #관광지별 소비지출유형분석
    expense ='//*[@id="gnb"]/ul/li[4]/div/ul/li[2]/ul/li[2]/a'
    path ='/Users/glebang/Desktop/team4/'
   
   
    #관광지별 소비지출유형분석
    driver =get_driver(path+'expense_data')
    login('gkfakdrn218@naver.com','bg2181357!',driver)
    goto_bigdata_navigation_page(expense, driver)
    years = set_year_date(driver, is_yearly=True)
    set_location_and_crawling(years, driver, path+'expense_data/', is_yearly=True)
    sort_by_location_year_month(path+'expense_data','소비지출유형분석')
    to_mysql(path, '관광지별 소비지출유형분석(연도별)')