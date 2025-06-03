import click
import os
import json

DATA_FILE = "finance_data.json"


def load_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        else:
            return {"expenses": [], "incomes": [], "investments": [], "budget": 0}
    except (json.JSONDecodeError, IOError) as e:
        click.echo(f"Error loading data: {e}")
        return {"expenses": [], "incomes": [], "investments": [], "budget": 0}


def save_data(data):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file)
    except IOError as e:
        click.echo(f"Error saving data: {e}")


@click.group()
def cli():
    """
    Personal Finance Manager CLI
    """
    pass


@cli.command()
@click.option("--amount", type=float)
@click.option("--category")
def add_expense(amount, category):
    """Add an expense"""
    data = load_data()
    data["expenses"].append({"amount": amount, "category": category})
    save_data(data)
    click.echo("Expense added successfully!")


@cli.command()
@click.option("--amount", type=float)
@click.option("--source")
def add_income(amount, source):
    """Add an income"""
    data = load_data()
    data["income"].append({"amount": amount, "source": source})
    save_data(data)
    click.echo("Income added successfully!")


@cli.command()
@click.option("--amount", type=float)
@click.option("--description")
def add_investment(amount, description):
    """Add an investment"""
    data = load_data()
    data["investments"].append({"amount": amount, "description": description})
    save_data(data)
    click.echo("Investment added successfully")


@cli.command()
@click.option("--budget", type=float)
def set_budget(budget):
    """Set the monthly budget"""
    data = load_data()
    data["budget"] = budget
    save_data(data)
    click.echo("Budget set successfully")


@cli.command()
def show_summary():
    """Show financial summary"""
    data = load_data()
    click.echo("Expenses:")
    for expense in data["expenses"]:
        click.echo(f"- {expense['category']}: ${expense['amount']}")

    click.echo("\nIncomes:")
    for income in data["incomes"]:
        click.echo(f"- {income['source']}: ${income['amount']}")

    click.echo("\nInvestments:")
    for investment in data["investments"]:
        click.echo(f"- {investment['description']}: ${investment['amount']}")

    click.echo(f"\nBudget for the month: ${data['budget']}")


@cli.command()
@click.option("--category", prompt="Enter the category to delete")
def delete_expense(category):
    """Delete an expense"""
    data = load_data()
    data["expenses"] = [expense for expense in data["expenses"] if expense["category"] != category]
    save_data(data)
    click.echo(f"Expenses with category '{category}' deleted successfully!")


@cli.command()
@click.option("--source", prompt="Enter the source to delete")
def delete_income(source):
    """Delete an income"""
    data = load_data()
    data["incomes"] = [income for income in data["incomes"] if income["source"] != source]
    save_data(data)
    click.echo(f"Incomes with source '{source}' deleted successfully!")


@cli.command()
@click.option("--description", prompt="Enter the description to delete")
def delete_investment(description):
    """Delete an investment"""
    data = load_data()
    data["investments"] = [investment for investment in data["investments"] if investment["description"] != description]
    save_data(data)
    click.echo(f"Investments with description '{description}' deleted successfully!")


if __name__ == "__main__":
    cli()