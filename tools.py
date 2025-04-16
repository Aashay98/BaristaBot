import json
import os
from collections.abc import Iterable
from datetime import datetime

from langchain_core.tools import tool

from menu import VALID_DRINKS, VALID_MODIFIERS, get_formatted_menu

# Simulated per-user session storage
_sessions = {}


def _get_user_order(session_id: str) -> list:
    return _sessions.setdefault(session_id, [])


@tool
def add_to_order(drink: str, modifiers: Iterable[str], session_id: str) -> str:
    """Add a drink with modifiers to user's session order."""
    if drink not in VALID_DRINKS:
        return f"Sorry, we don't have {drink}."
    invalid_mods = [m for m in modifiers if m not in VALID_MODIFIERS]
    if invalid_mods:
        return f"Invalid modifiers: {', '.join(invalid_mods)}"

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
    eta = randint(2, 6)
    # Log data to local JSON file
    log_data = {
        "session_id": session_id,
        "timestamp": datetime.now().isoformat(),
        "order": order,
        "eta_min": eta,
    }

    os.makedirs("order_logs", exist_ok=True)
    with open(f"order_logs/order_{session_id}.json", "w") as f:
        json.dump(log_data, f, indent=2)

    _sessions[session_id] = []  # Clear order after placing
    return eta


@tool
def get_menu() -> str:
    """Provide the latest up-to-date menu."""
    return get_formatted_menu()
