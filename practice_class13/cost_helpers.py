
TICKET_PRICE = 2.00
SPECIAL_DRAW_COST = 1.00


def base_ticket_cost(number_of_draws):
  
  return TICKET_PRICE * number_of_draws


def ticket_with_special_draw(number_of_draws):
  """
  Calculates the ticket cost with a special draw.
  """
  return base_ticket_cost(number_of_draws) + SPECIAL_DRAW_COST


def total_ticket_cost(number_of_draws, has_special_draw):
  """
  Calculates the total ticket cost according to the number
  of draws being entered and whether a special draw is being
  entered.
  Ex.:
    10, True -> 21.00
    10, False -> 20.00
  args:
    number_of_tickets: integer with the number of draws
    has_special_draw: boolean with whether a special draw is being entered
  """
  if not has_special_draw:
    return base_ticket_cost(number_of_draws)
  return ticket_with_special_draw(number_of_draws)
