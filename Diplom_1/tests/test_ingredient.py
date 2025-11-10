from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING

class TestIngredient:
    def test_get_ingridient_price(self, ):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        ingredient.get_price()
        assert ingredient.get_price() == 100
        
    def test_get_ingridient_name(self,):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        ingredient.get_name()
        assert ingredient.get_name() == "cutlet"
        
    def test_get_ingridient_type(self,):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        ingredient.get_type()
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING