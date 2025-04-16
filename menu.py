VALID_DRINKS = {
    "Espresso",
    "Americano",
    "Cold Brew",
    "Latte",
    "Cappuccino",
    "Cortado",
    "Macchiato",
    "Mocha",
    "Flat White",
    "English Breakfast Tea",
    "Green Tea",
    "Earl Grey",
    "Chai Latte",
    "Matcha Latte",
    "London Fog",
    "Steamer",
    "Hot Chocolate",
}

VALID_MODIFIERS = {
    "Whole",
    "2%",
    "Oat",
    "Almond",
    "2% Lactose Free",
    "Single",
    "Double",
    "Triple",
    "Quadruple",
    "Decaf",
    "Regular",
    "Hot",
    "Iced",
    "vanilla",
    "hazelnut",
    "caramel sauce",
    "chocolate sauce",
    "sugar-free vanilla",
    "extra hot",
    "half caff",
    "extra foam",
    "Dirty",
}


def get_formatted_menu() -> str:
    return """
        **☕ Coffee Drinks:**
        - Espresso
        - Americano
        - Cold Brew

        **🥛 Coffee with Milk:**
        - Latte
        - Cappuccino
        - Cortado
        - Macchiato
        - Mocha
        - Flat White

        **🍵 Tea Drinks:**
        - English Breakfast Tea
        - Green Tea
        - Earl Grey

        **🍶 Tea with Milk:**
        - Chai Latte
        - Matcha Latte
        - London Fog

        **🍫 Other Drinks:**
        - Steamer
        - Hot Chocolate

        **🛠 Modifiers:**
        - Milk: Whole, 2%, Oat, Almond, 2% Lactose Free _(default: whole)_
        - Espresso shots: Single, Double, Triple, Quadruple _(default: double)_
        - Caffeine: Decaf, Regular _(default: regular)_
        - Temp: Hot, Iced _(default: hot)_
        - Sweeteners: vanilla, hazelnut, caramel sauce, chocolate sauce, sugar-free vanilla
        - Extras: extra hot, half caff, extra foam
        - Soy milk is **out of stock**.
        - ‘Dirty’ = add espresso to non-coffee drinks (e.g., Dirty Chai Latte).
        """
