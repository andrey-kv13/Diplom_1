import pytest
class TestBurger:
    """Тесты для класса Burger"""
    
    def test_add_burger_ingredient(self, burger, ingredient):
        """Тест добавления ингредиента"""
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1, f"Ожидался 1 ингредиент, получено {len(burger.ingredients)}"
        assert burger.ingredients[0] == ingredient, f"Ожидался {ingredient}, получен {burger.ingredients[0]}"
    
    def test_set_burger_buns(self, burger, bun):
        """Тест установки булочки"""
        burger.set_buns(bun)
        assert burger.bun == bun, f"Ожидалось {bun}, получено {burger.bun}"
    
    @pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5], ids=[
                                                                "remove_first_ingredient", 
                                                                "remove_second_ingredient", 
                                                                "remove_third_ingredient", 
                                                                "remove_fourth_ingredient", 
                                                                "remove_fifth_ingredient", 
                                                                "remove_sixth_ingredient"
                                                            ])
    def test_remove_burger_ingredient(self, index, burger_with_ingredients):
        """Тест удаления ингредиента по индексу"""
        element_to_remove = burger_with_ingredients.ingredients[index]
        initial_count = len(burger_with_ingredients.ingredients)
        
        burger_with_ingredients.remove_ingredient(index)
        
        assert len(burger_with_ingredients.ingredients) == initial_count - 1, \
            f"Ожидалось {initial_count - 1} элементов, получено {len(burger_with_ingredients.ingredients)}"
            
        assert element_to_remove not in burger_with_ingredients.ingredients, \
            f"Элемент {element_to_remove} не должен быть в списке после удаления"

    @pytest.mark.parametrize("index, new_index", [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 0),
        (5, 1)
    ], ids=[
        "move_first_ingredient_to_second",
        "move_second_ingredient_to_third", 
        "move_third_ingredient_to_fourth",
        "move_fourth_ingredient_to_fifth",
        "move_fifth_ingredient_to_first",
        "move_sixth_ingredient_to_second"
    ])
    def test_move_burger_ingredient(self, index, new_index, burger_with_ingredients):
        """Тест перемещения ингредиента по индексу"""
        element_to_move = burger_with_ingredients.ingredients[index]
        initial_count = len(burger_with_ingredients.ingredients)
        
        burger_with_ingredients.move_ingredient(index, new_index)
        
        assert len(burger_with_ingredients.ingredients) == initial_count, \
            f"Количество ингредиентов должно остаться {initial_count}"
        
        assert burger_with_ingredients.ingredients[new_index] == element_to_move, \
            f"Элемент {element_to_move} должен быть на позиции {new_index}"
    
    def test_get_burger_price(self, burger_with_bun_and_ingredients):
        """Тест получения цены бургера"""
        # Ожидаемая цена: 100*2 (булочка) + 100+200+300+100+200+300 (ингредиенты) = 200 + 1200 = 1400
        expected_price = 1400
        actual_price = burger_with_bun_and_ingredients.get_price()
        assert actual_price == expected_price, f"Ожидалась цена {expected_price}, получено {actual_price}"
        
    def test_get_burger_receipt(self, burger_with_bun_and_ingredients):
        """Тест получения чека бургера"""
        receipt = burger_with_bun_and_ingredients.get_receipt()
        assert "test bun" in receipt
        assert "hot sauce" in receipt
        assert "sour cream" in receipt
        assert "chili sauce" in receipt
        assert "cutlet" in receipt
        assert "dinosaur" in receipt
        assert "sausage" in receipt
        assert "Price: 1400" in receipt
        
    def test_get_burger_receipt_ingredient_error(self, burger, bun, mock_ingredient_name_error):
        """Тест ошибки при генерации чека ингредиента"""
        burger.set_buns(bun)
        burger.add_ingredient(mock_ingredient_name_error)
        
        with pytest.raises(ValueError) as exc_info:
            burger.get_receipt()
        assert "Invalid ingredient name" in str(exc_info.value)

    def test_get_price_ingredient_error(self, burger, bun, mock_ingredient_with_error):
        """Тест ошибки при расчете цены ингредиента"""
        burger.set_buns(bun)
        burger.add_ingredient(mock_ingredient_with_error)
        
        with pytest.raises(ValueError) as exc_info:
            burger.get_price()
        assert "Invalid ingredient price" in str(exc_info.value)

    def test_get_price_bun_error(self, burger, ingredient, mock_bun_with_error):
        """Тест ошибки при расчете цены булочки"""
        burger.set_buns(mock_bun_with_error)
        burger.add_ingredient(ingredient)
        
        with pytest.raises(ValueError) as exc_info:
            burger.get_price()
        assert "Invalid bun price" in str(exc_info.value)