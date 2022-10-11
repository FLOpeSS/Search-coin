from re import search
from playwright.sync_api import sync_playwright



def search_coin():
    coins = input("Digite uma moeda para saber sua cotação: ").lower().split()
    quote = {}
    cotation = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for search in coins:
            page.goto("https://www.google.com.br")
            page.fill("xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input", "Cotação do " + str(search))
            page.press("body", "Enter")
            cotation.append(page.locator('xpath=//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value'))
            for i in cotation:
              quote.update({search: i})
        # print(quote)
        # for i in quote:
        #     print(i, quote[i])
        
        return quote



real = search_coin()

print(real)

rublo = search_coin()
print(rublo)

