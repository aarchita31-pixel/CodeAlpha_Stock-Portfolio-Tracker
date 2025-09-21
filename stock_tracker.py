# Stock Portfolio Tracker

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "INFY": 1550,
    "TCS": 3500
}

# Step 2: Get user input
portfolio = {}

print("📈 Welcome to Stock Portfolio Tracker!")
print("Enter your stocks and quantities. Type 'done' when finished.\n")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Step 3: Calculate total investment
total_value = 0
print("\n🧾 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"• {stock}: {qty} shares × ₹{price} = ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_value}")


