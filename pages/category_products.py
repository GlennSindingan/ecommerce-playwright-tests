class CategoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.women_category = page.get_by_role("link", name="Women")
        self.sub_dress_category = page.locator("#Women").get_by_role("link", name="Dress")
        self.sub_top_category = page.locator("#Women").get_by_role("link", name="Tops")

        self.men_category = page.get_by_role("link", name="Men")
        self.men_tshirt_category = page.locator("#Men").get_by_role("link", name="Tshirts")
        self.men_jeans_category = page.locator("#Men").get_by_role("link", name="Jeans")

        self.left_sidebar = page.locator(".left-sidebar")

        self.dress_heading = page.get_by_text("Women - Dress Products")
        self.top_heading = page.get_by_text("Women - Tops Products")

        self.tshirt_heading = page.get_by_text("Men - Tshirts Products")
        self.jeans_heading = page.get_by_text("Men - Jeans Products")
    


    def click_women_category(self):
        self.women_category.click()

    def click_dress_category(self):
        self.sub_dress_category.click()

    def click_top_category(self):
        self.sub_top_category.click()

    def click_men_category(self):
        self.men_category.click()

    def click_tshirt_category(self):
        self.men_tshirt_category.click()

    def click_jeans_category(self):
        self.men_jeans_category.click()
        

