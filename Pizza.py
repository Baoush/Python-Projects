Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> number_of_pizzas = eval (input("How many pizzas do you want?"))
... 
... cost_per_pizza = eval (input)("How much does a pizza cost?")
... subtotal = number_of_pizzas * cost_per_pizza
... 
... tax_rate = 0.08
... sales_tax = subtotal * tax_rate
... total = subtotal + sales_tax
... 
... print("The total cost is £",   total)
... print("This includes £", subtotal, "for the pizza and")
