import unittest
from sim_class import Character, Family, House, Furniture, TV, Fridge, Bed, Toilet, Bath, Bookshelf

class TestGame(unittest.TestCase):
    def setUp(self):
        self.fam = Family("Kowal")
        self.adult = Character("Anna", self.fam, 25)
        self.child = Character("Kuba", self.fam, 10)
        self.elder = Character("Irena", self.fam, 80)
        self.home = House("willa", self.fam)
        self.fridge = Fridge(2, 50, self.home)
    
    def test_init(self):
        f = Family("Kowal", 950)
        c = Character("Anna", f, 25, 10)
        h = House("dom", f, 48, 500, 0)
        self.assertEqual(h.capacity, self.home.capacity)
        self.assertEqual(h.bill_price, self.home.bill_price)
        self.assertEqual(h.bills, self.home.bills)
        self.assertEqual(c.hunger, self.adult.hunger)
        self.assertEqual(f.money, self.fam.money)
    
    def test_is_child(self):
        self.assertFalse(self.adult.is_child())
        self.assertFalse(self.elder.is_child())
        self.assertTrue(self.child.is_child())
    
    def test_go_to_work(self):
        self.adult.go_to_work()
        self.assertEqual(self.fam.money, 980)
        self.assertEqual(self.adult.energy, 5)
        self.assertEqual(self.adult.hunger, 8)
        self.assertEqual(self.adult.hygene, 9)
    
    def test_go_to_school(self):
        self.child.go_to_school()
        self.assertEqual(self.child.inteligence, 13)
    
    def test_get_penstion(self):
        self.elder.get_pension()
        self.assertEqual(self.fam.money, 965)
    
    def test_exercise(self):
        self.elder.exercise()
        self.assertIn(self.elder.strenght, [14, 13, 12, 7])
    
    def test_bills(self):
        self.home.add_bills()
        self.assertEqual(self.home.bills, 500)
        self.home.pay_bills()
        self.assertEqual(self.home.bills, 0)
        self.assertEqual(self.fam.money, 450)
    
    def test_fridge(self):
        self.fridge.eat(self.adult)
        self.assertEqual(self.fam.money, 940)
        self.assertEqual(self.adult.hunger, 10)
    
    def test_tv(self):
        tv = TV(0, 0, self.home)
        tv.watch_tv(self.child)
        self.assertIn(self.child.inteligence, [10, 15, 7])
        self.assertIn(self.child.creativity, [10, 15, 7])
    

if __name__ == "__main__":
    unittest.main()