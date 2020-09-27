import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 設定値
chromedriver_path = 'ChromeDriverのパス'
max_page = 3


def main():
    '''
    メインの処理
    「メンズ新着アイテム」のリンクをたどり、商品の情報を取得
    '''

    options = Options()
    options.add_argument('--headless')  # ヘッドレスモードを有効にする
    driver = webdriver.Chrome(chromedriver_path, options=options)  # ChromeのWebDriverオブジェクトを作成
    driver.get('https://www.mercari.com/jp/')  # メルカリのトップページを開く
    assert 'メルカリ' in driver.title  # タイトルに'メルカリ'が含まれていることを確認

    a = driver.find_elements_by_css_selector('#__next > div > div > div > div:nth-child(3) > div')[1]  # 'メンズ新着アイテム'のボックスを取得
    next_url = a.find_element_by_css_selector('a').get_attribute('href')  # URLを取得

    items = []
    for i in range(1, max_page + 1):  # max_pageまでクローリング
        driver.get(next_url)
        if i == 1:
            initial_url = driver.current_url
        new_item = scrape_contents(driver)
        items.append({'{}'.format(i): new_item})
        next_url = initial_url + '?page=' + str(i+1)  # 次にクローリングするページのURLを取得

    with open('mercari_practice.csv', 'w') as f:
        writer = csv.DictWriter(f, ['url', 'title', 'price'])
        writer.writeheader()
        for item in items:
            for value in item.values():
                writer.writerows(value)

    driver.quit()


def scrape_contents(driver):
    '''
    URL、タイトル、価格を取得してdictとしてリストに追加
    '''

    new_item = []
    for a in driver.find_elements_by_css_selector('#__next > div > div > div > div > div:nth-child(1) > ul > li'):  # 各アイテムのボックスを取得
        new_item.append({
            'url': a.find_element_by_css_selector('a').get_attribute('href'),
            'title': a.find_element_by_css_selector('a > figure > figcaption > span').text,
            'price': a.find_element_by_css_selector('a > figure > div > span').text
        })  # URL、タイトル、価格を取得してdictとしてリストに追加
    return new_item


if __name__ == '__main__':
    main()
