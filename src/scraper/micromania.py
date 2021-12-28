from scraper.common import ScrapeResult, Scraper, ScraperFactory

class MicroManiaResult(ScrapeResult):
    def parse(self):
        alert_subject = 'In Stock'
        alert_content = ''

        # Attempt to find the "Alert me" button
        button = self.soup.body.find("div", { "class": "add-to-cart-container d-none" })
        if button:
            return

        button = self.soup.body.find("div", { "class": "add-to-cart-container " })
        if button:
            price_str = self.set_price("1640.00")
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
