# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3500,
    "MSFT": 320
}

# Store total investment
total_investment = 0
user_portfolio = {}

print("📈 Welcome to the Simple Stock Tracker!\n")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"  {stock}: ${price}")

print("\nEnter your stock purchases (type 'done' to finish):")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not available. Please enter a valid symbol.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print("⚠️ Quantity must be positive.")
            continue
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    investment = stock_prices[stock] * quantity
    user_portfolio[stock] = user_portfolio.get(stock, 0) + quantity
    total_investment += investment
    print(f"✅ Added {quantity} shares of {stock} for ${investment}\n")

# Display final results
print("\n📊 Investment Summary:")
for stock, quantity in user_portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${value}")
print(f"\n💰 Total Investment: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save the summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("investment_summary.txt", "w") as file:
        file.write("Investment Summary:\n")
        for stock, quantity in user_portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print("📁 Summary saved to 'investment_summary.txt'")
