from praktikum.bun import Bun
import pytest
class TestBun:
    
    @pytest.mark.parametrize("name, price", [
        ("burger_bun", 100),
        ("sesame_bun", 150),
        ("whole_wheat_bun", 120),
        ("gluten_free_bun", 180),
    ])
    def test_get_bun_with_name_and_price(self, name, price):
        """Тест получения булочки с именем и ценой."""
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price