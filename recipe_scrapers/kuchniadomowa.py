# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class KuchniaDomowa(AbstractScraper):
    @classmethod
    def host(cls):
        return "kuchnia-domowa.pl"

    def title(self):
        return self.soup.find("h2").get_text().strip()

    def total_time(self):
        return self.schema.total_time()

    def image(self):
        urls = self.soup.findAll("img", {"class": "article-img", "id": "article-img-1"})
        return f"https:{urls[1]['src']}"

    def ingredients(self):
        # TODO: add implementation
        raise NotImplementedError("This should be implemented.")

    def instructions(self):
        instructions = self.soup.find("div", {"id": "recipe-instructions"}).findAll(
            "li"
        )
        instructions = [x.text for x in instructions]
        return "\n".join(instructions)
