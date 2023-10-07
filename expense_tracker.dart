class Expense {
  final String description;
  final double amount;

  Expense(this.description, this.amount);
}

class ExpenseTracker {
  List<Expense> expenses = [];

  void addExpense(String description, double amount) {
    expenses.add(Expense(description, amount));
  }

  double getTotalExpenses() {
    double total = 0;
    for (var expense in expenses) {
      total += expense.amount;
    }
    return total;
  }

  void viewExpenses() {
    print("Expense List:");
    for (var expense in expenses) {
      print("${expense.description}: \$${expense.amount}");
    }
    print("Total Expenses: \$${getTotalExpenses()}");
  }
}

void main() {
  var tracker = ExpenseTracker();

  tracker.addExpense("Groceries", 50.0);
  tracker.addExpense("Dinner", 30.0);
  tracker.addExpense("Gas", 40.0);

  tracker.viewExpenses();
}
