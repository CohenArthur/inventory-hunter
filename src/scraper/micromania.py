from scraper.common import ScrapeResult, Scraper, ScraperFactory

class MicroManiaResult(ScrapeResult):
    def parse(self):
        alert_subject = 'In Stock'
        alert_content = ''

        button = None

        divs = self.soup.body.find_all("div", class_="add-to-cart-container d-none")
        if len(divs) != 0:
            button = divs[0]
            return

        divs = self.soup.body.find_all("div", class_="add-to-cart-container")
        if len(divs) != 0:
            spans = self.soup.body.find_all("span", { "itemprop": "price"}, class_="value")
            if len(spans) != 0:
                price = spans[0]["content"]
                price_str = self.set_price(price)
            else:
                return
            self.alert_subject = alert_subject
            self.alert_content = f"Wouuuuuuh {price_str}"

@ScraperFactory.register
class MicroManiaScraper(Scraper):
    @staticmethod
    def get_domain():
        return 'micromania'

    @staticmethod
    def get_driver_type():
        return 'lean_and_mean'

    @staticmethod
    def get_result_type():
        return MicroManiaResult
