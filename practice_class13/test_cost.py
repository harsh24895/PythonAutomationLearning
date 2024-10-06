import pytest

from practice_class13.cost_helpers import base_ticket_cost,total_ticket_cost,ticket_with_special_draw

def test_base_ticket_cost():
    num_of_draw = 1.0
    ticket_cost = 2.0

    #Act
    actual_output = base_ticket_cost(num_of_draw)
    #Assert
    assert ticket_cost == actual_output

#NEED TO FOCUS WITH INNER HELPER FUNCTIONS IMPORTANT
def test_special_draw():
    #Arrange
    num_of_draw = 1.0
    expected = 3.0

    actual_output = ticket_with_special_draw(num_of_draw)

    assert expected == actual_output


@pytest.mark.parametrize('number_of_draws,has_special_draw',[
                                (10, True),
                                (10, False)])
def test_total_cost(number_of_draws,has_special_draw):

    actual = total_ticket_cost(number_of_draws)
    assert actual == has_special_draw


