# mypy: disallow_untyped_defs=False

from ._abstract import AbstractScraper
from ._exceptions import RecipeScrapersExceptions


class OwenHan(AbstractScraper):
    @classmethod
    def host(cls):
        return "owen-han.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).text

    def total_time(self):
        raise RecipeScrapersExceptions(
            f"{self.host} does not provide time information."
        )

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return [x for x in map(lambda x: x.text, self.soup.select("ul > li"))]

    def instructions(self):
        return [x for x in map(lambda x: x.text, self.soup.select("ol > li"))]
