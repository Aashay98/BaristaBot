from langchain_core.tools import tool
from collections.abc import Iterable

# Internal "in-memory" order storage (would be a DB or session in a real app)
_current_order = []

@tool
def get_menu() -> str:
    """Provide the latest up-to-date menu."""
    return """
    MENU:
    Coffee Drinks:
    Espresso
    Americano
    Cold Brew

    Coffee Drinks with Milk:
    Latte
    Cappuccino
    Cortado
    Macchiato
    Mocha
    Flat White

    Tea Drinks:
    English Breakfast Tea
    Green Tea
    Earl Grey

    Tea Drinks with Milk:
    Chai Latte
    Matcha Latte
    London Fog

    Other Drinks:
    Steamer
    Hot Chocolate

    Modifiers:
    Milk options: Whole, 2%, Oat, Almond, 2% Lactose Free; Default option: whole
    Espresso shots: Single, Double, Triple, Quadruple; default: Double
    Caffeine: Decaf, Regular; default: Regular
    Hot-Iced: Hot, Iced; Default: Hot
    Sweeteners: vanilla, hazelnut, caramel sauce, chocolate sauce, sugar-free vanilla
    Special requests: 'extra hot', 'half caff', 'extra foam', etc.

    'Dirty' = add espresso to non-coffee drinks (e.g., Dirty Chai Latte).
    Soy milk is out of stock today.
    """

@tool
def add_to_order(drink: str, modifiers: Iterable[str]) -> str:
    """Adds the specified drink to the customer's order, including any modifiers."""
    modifier_str = ", ".join(modifiers) if modifiers else "no modifiers"
    item = f"{drink} ({modifier_str})"
    _current_order.append(item)
    return f"Added to your order: {item}"

@tool
def confirm_order() -> str:
    """Asks the customer if the order is correct."""
    if not _current_order:
        return "You currently have no items in your order."

    order_text = "\n".join(f"- {item}" for item in _current_order)
    return f"Here’s your current order:\n{order_text}\nIs this correct?"

@tool
def get_order() -> str:
    """Returns the user's order so far."""
    if not _current_order:
        return "(No order yet)"
    return "\n".join(_current_order)

@tool
def clear_order():
    """Clears the user's order."""
    _current_order.clear()
    return "Order has been cleared."

@tool
def place_order() -> int:
    """Finalizes the order and returns the estimated preparation time."""
    if not _current_order:
        return 0  # Nothing to prepare

    from random import randint
    eta = randint(2, 6)
    _current_order.clear()  # Reset after placing
    return eta
