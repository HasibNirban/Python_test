from my_app.app import Generic_Methods

class Addition:
    def test_add_two(self):
        assert Generic_Methods.add2(6,4) == 1
        assert Generic_Methods.add2(5,5) == 10

    def test_add_three(self):
        assert Generic_Methods.add3(1,2,3) == 6
        assert Generic_Methods.add3(4,5,6) == 15

class Substraction:
    def test_sub(self):
        assert Generic_Methods.sub(4,2) == 2
        assert Generic_Methods.sub(6,2) == 4

class Product:
    def test_product_of_two(self):
        assert Generic_Methods.pro2(1,2) == 2
        assert Generic_Methods.pro3(4,5) ==20
