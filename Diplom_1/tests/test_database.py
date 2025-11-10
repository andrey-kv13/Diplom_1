from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    
    def test_available_buns(self):
        """Тест получения доступных булочек из базы данных"""
        db = Database()
        
        result = db.available_buns()
        assert len(result) == 3, f"Ожидалось 3 булочки, получено {len(result)}"
        assert isinstance(result, list), f"Ожидался список, получен {type(result).__name__}"
        assert all(isinstance(bun, Bun) for bun in result), f"Ожидались объекты Bun, получены {[type(bun).__name__ for bun in result]}"
        assert result[0].name == "black bun", f"Ожидалось название 'black bun', получено '{result[0].name}'"
        assert result[0].price == 100, f"Ожидалась цена 100, получена {result[0].price}"
        assert result[1].name == "white bun", f"Ожидалось название 'white bun', получено '{result[1].name}'"
        assert result[1].price == 200, f"Ожидалась цена 200, получена {result[1].price}"
        assert result[2].name == "red bun", f"Ожидалось название 'red bun', получено '{result[2].name}'"
        assert result[2].price == 300, f"Ожидалась цена 300, получена {result[2].price}"
        
    def test_available_ingredients(self):
        """Тест получения доступных ингредиентов из базы данных"""
        db = Database()
        result = db.available_ingredients()
        
        assert len(result) == 6, f"Ожидалось 6 ингредиентов, получено {len(result)}"
        assert isinstance(result, list), f"Ожидался список, получен {type(result).__name__}"
        assert all(isinstance(ing, Ingredient) for ing in result), f"Ожидались объекты Ingredient, получены {[type(ing).__name__ for ing in result]}"
        
        # Проверяем конкретные ингредиенты
        assert result[0].type == INGREDIENT_TYPE_SAUCE, f"Ожидался тип SAUCE, получен {result[0].type}"
        assert result[0].name == "hot sauce", f"Ожидалось название 'hot sauce', получено '{result[0].name}'"
        assert result[0].price == 100, f"Ожидалась цена 100, получена {result[0].price}"
        
        assert result[2].type == INGREDIENT_TYPE_SAUCE, f"Ожидался тип SAUCE, получен {result[2].type}"
        assert result[2].name == "chili sauce", f"Ожидалось название 'chili sauce', получено '{result[2].name}'"
        assert result[2].price == 300, f"Ожидалась цена 300, получена {result[2].price}"
        
        assert result[5].type == INGREDIENT_TYPE_FILLING, f"Ожидался тип FILLING, получен {result[5].type}"
        assert result[5].name == "sausage", f"Ожидалось название 'sausage', получено '{result[5].name}'"
        assert result[5].price == 300, f"Ожидалась цена 300, получена {result[5].price}"
