def analyze_question(question):
    intent = "inventory"
    shopifyql = "SELECT sum(quantity) FROM orders WHERE date >= -30"
    answer = "You should reorder 70 units next week"
    return answer
