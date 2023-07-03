from selenium import webdriver
import requests
import time


def get_paper_list(num):
    url = "https://m.app.dawuhanapp.com/journalist/works"
    param = {"identity": 1,
             "memberid": 666805,
             "to_member_id": 666805,
             "page": 1,
             "pagesize": num}
    req = requests.request('GET', url, params=param)
    paper_list = req.json()['data']['list']
    return paper_list


def get_one_paper(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Host": "m.app.dawuhanapp.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/114.0.0.0"}
    one_req = requests.request('GET', url, headers=headers)
    print("get url=" + url + " stat_code=" + str(one_req.status_code))


def browser_one_paper(url):
    mobile_emulation = {'deviceName': 'iPhone 12 Pro'}
    options = webdriver.EdgeOptions()
    options.add_experimental_option('mobileEmulation', mobile_emulation)
    browser = webdriver.Edge(options=options)
    browser.get(url)
    print("get url=" + url + ", succ:" + str(succ_count) + ", fail:" + str(fail_count))
    time.sleep(2)


def refresh_and_shuffle(times):
    print("refreshing...")
    p_list = get_paper_list(5)
    for i in range(1, times):
        for paper_item in p_list:
            browser_one_paper(paper_item['share_url'])


succ_count = 0
fail_count = 0
if __name__ == '__main__':
    ex_count = 0
    # while True:
    for i in range(1, 30):
        try:
            refresh_and_shuffle(100)
            ex_count = 0
            succ_count += 1
        except Exception as ex:
            ex_count += 1
            fail_count += 1
            print(str(ex))
            if ex_count > 100:
                print("ex count > 100, shutdown")
                break
