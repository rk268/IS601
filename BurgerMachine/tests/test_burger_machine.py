import pytest
import random
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm
'''
# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("turkey")
    first_order.handle_patty("turkey")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    #machine.handle_pay(10000,"10000")
    return first_order

# sample test case, can delete if not using
def test_production_line(second_order):
    for j in second_order.buns:
        print(second_order.inprogress_burger)
        if j.name.lower() == second_order.inprogress_burger[0].name.lower():
            assert True
            return

    assert False
'''
# add required test cases below
def test_first_bun(machine):
    before_inprog_lst_length = len(machine.inprogress_burger)
    try:
        machine.pick_patty('beef')
        machine.pick_toppings('tomato')
    except InvalidStageException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(machine.inprogress_burger))
    # rk268 3/26/2023



def test_patty_in_stock(machine):
    machine.patties[1].quantity = 0
    name = machine.patties[1].name.lower()
    machine.handle_bun('no bun')
    before_inprog_lst_length = len(machine.inprogress_burger)
    #machine.currently_selecting = BurgerMachine.STAGE.patties
    try:
        machine.pick_patty(name)
    except OutOfStockException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(machine.inprogress_burger))
    # rk268 3/26/2023   
        

def test_topping_in_stock(machine):
    
    machine.toppings[1].quantity = 0
    name = machine.toppings[1].name.lower()
    machine.handle_bun('white burger bun')
    machine.handle_patty('next')
    before_inprog_lst_length = len(machine.inprogress_burger)
    #test.currently_selecting = IcecreamMachine.STAGE.Toppings
    try:
        machine.pick_toppings(name)
    except OutOfStockException:
        assert(before_inprog_lst_length == len(machine.inprogress_burger))
    finally:
        assert(before_inprog_lst_length == len(machine.inprogress_burger))
    # rk268 3/26/2023

def test_add_3_patties(machine):
    machine.handle_bun('no bun')
    machine.pick_patty('turkey')
    machine.pick_patty('turkey')
    machine.pick_patty('Beef')
    
    before_inprog_lst_length = len(machine.inprogress_burger)
    #machine.currently_selecting = IcecreamMachine.STAGE.Flavor
    try:
        machine.pick_patty('beef')
    except ExceededRemainingChoicesException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(machine.inprogress_burger))
    # rk268 3/26/2023


def test_add_3_toppings(machine):
    machine.handle_bun('no bun')
    machine.handle_patty('next')
    machine.pick_toppings('BBQ')
    machine.pick_toppings('Pickles')
    machine.pick_toppings('Ketchup')
    
    before_inprog_lst_length = len(machine.inprogress_burger)
    try:
        machine.pick_toppings('Tomato')
    except ExceededRemainingChoicesException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(machine.inprogress_burger))
    # rk268 3/26/2023



def test_calculate_cost(machine):
    r = 0
    while r < 4:
        i = random.randrange(0, 3, 1)
        j = random.randrange(0, 3, 1)
        k = random.randrange(0, 3, 1)
        any_burger = [machine.buns[i],machine.patties[j],machine.toppings[k]]
        ExpectedPrice = any_burger[0].cost + any_burger[1].cost + any_burger[2].cost
        machine.inprogress_burger = any_burger
        ActualPrice = machine.calculate_cost()
        assert(ActualPrice==ExpectedPrice)
        r += 1
    # rk268 3/26/2023

def test_total_sales(machine):
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(1,'1')
    machine.handle_bun("Wheat Burger Bun")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(1,'1')
    machine.handle_bun("Wheat Burger Bun")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(2.25,'2.25')

    expected_total_sales = 1 + 1 + 2.25
    assert(expected_total_sales==machine.total_sales)
# rk268 3/26/2023


def test_burger_increment(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(2.5,'2.5')
    machine.handle_bun("no bun")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(2,'2')
    expected_total_burgers = 2
    assert(expected_total_burgers==machine.total_burgers)
# rk268 3/26/2023