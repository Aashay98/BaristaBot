from langchain_core.tools import tool
from collections.abc import Iterable
from typing import Optional

# Simulated per-user session storage
_sessions = {}

def _get_user_order(session_id: str) -> list:
    return _sessions.setdefault(session_id, [])

@tool
def add_to_order(drink: str, modifiers: Iterable[str], session_id: str) -> str:
    """Add a drink with modifiers to user's session order."""
    item = f"{drink} ({', '.join(modifiers) if modifiers else 'no modifiers'})"
    _get_user_order(session_id).append(item)
    return f"Added to your order: {item}"

@tool
def get_order(session_id: str) -> str:
    """Get current order for session."""
    order = _get_user_order(session_id)
    return "\n".join(order) if order else "(No items in your order)"

@tool
def confirm_order(session_id: str) -> str:
    """Show order summary for confirmation."""
    order = _get_user_order(session_id)
    if not order:
        return "Your order is empty."
    return "Here’s your order:\n" + "\n".join(f"- {item}" for item in order)

@tool
def clear_order(session_id: str) -> str:
    """Clear the user's order."""
    _sessions[session_id] = []
    return "Order cleared."

@tool
def place_order(session_id: str) -> int:
    """Place order and return ETA in minutes."""
    from random import randint
    order = _get_user_order(session_id)
    if not order:
        return 0
    _sessions[session_id] = []  # Clear after placing
    return randint(2, 6)

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
