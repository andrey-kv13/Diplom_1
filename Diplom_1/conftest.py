import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

@pytest.fixture
def burger():
    """Фикстура бургера"""
    return Burger()

@pytest.fixture
def bun():
    """Фикстура с булочкой"""
    return Bun("test bun", 100)

@pytest.fixture
def ingredient():
    """Фикстура с ингредиентом"""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 50)

@pytest.fixture
def burger_with_bun_and_ingredients(burger, bun):
    """Фикстура бургера с булочкой и ингредиентами"""
    burger.set_buns(bun)
    db = Database()
    ingredients = db.available_ingredients()
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    return burger

@pytest.fixture
def burger_with_ingredients(burger):
    """Фикстура бургера только с ингредиентами (без булочки)"""
    db = Database()
    ingredients = db.available_ingredients()
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    return burger

# Фикстуры для моков
@pytest.fixture
def mock_ingredient_with_error():
    """Фикстура с моком ингредиента, вызывающим ошибку при получении цены"""
    from unittest.mock import Mock
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_price.side_effect = ValueError("Invalid ingredient price")
    mock_ingredient.get_name.return_value = "error ingredient"
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_ingredient

@pytest.fixture
def mock_ingredient_name_error():
    """Фикстура с моком ингредиента, вызывающим ошибку при получении имени"""
    from unittest.mock import Mock
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_price.return_value = 100
    mock_ingredient.get_name.side_effect = ValueError("Invalid ingredient name")
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_ingredient

@pytest.fixture
def mock_bun_with_error():
    """Фикстура с моком булочки, вызывающим ошибку при получении цены"""
    from unittest.mock import Mock
    mock_bun = Mock(spec=Bun)
    mock_bun.get_price.side_effect = ValueError("Invalid bun price")
    mock_bun.get_name.return_value = "error bun"
    return mock_bun