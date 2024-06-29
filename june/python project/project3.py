import csv

def analyze_financial_data(csv_file):

    total_months = 0
    total_profit_losses = 0
    prev_profit_loss = 0
    greatest_increase = 0
    greatest_decrease = 0


    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            date, profit_loss = row
            profit_loss = int(profit_loss)


            total_months += 1
            total_profit_losses += profit_loss

            if total_months > 1:
                change = profit_loss - prev_profit_loss
                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_date = date
                elif change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_date = date

            prev_profit_loss = profit_loss


    average_change = total_profit_losses / (total_months - 1)


    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")


analyze_financial_data('budget_data.csv')

def analyze_financial_data(csv_file):

    total_months = 0
    total_profit_losses = 0
    prev_profit_loss = 0
    greatest_increase = 0
    greatest_decrease = 0

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            date, profit_loss = row
            profit_loss = int(profit_loss)

            total_months += 1
            total_profit_losses += profit_loss

            if total_months > 1:
                change = profit_loss - prev_profit_loss
                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_date = date
                elif change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_date = date

            prev_profit_loss = profit_loss

    average_change = total_profit_losses / (total_months - 1)

    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_losses}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

analyze_financial_data('budget_data.csv')