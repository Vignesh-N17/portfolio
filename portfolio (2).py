#!/usr/bin/env python3
"""
💰 portfolio — Indian Stock Portfolio Tracker CLI
Track your stocks. See your gains. Stay informed.
"""

import json
import os
import sys
import argparse
from datetime import datetime

try:
    import yfinance as yf
    from rich.console import Console
    from rich.table import Table
    from rich import box
    from rich.panel import Panel
    from rich.text import Text
except ImportError:
    print("Installing required packages...")
    os.system("pip install yfinance rich --break-system-packages -q")
    import yfinance as yf
    from rich.console import Console
    from rich.table import Table
    from rich import box
    from rich.panel import Panel
    from rich.text import Text

console = Console()

# Where portfolio data is saved
DATA_FILE = os.path.join(os.path.dirname(__file__), "portfolio_data.json")


# ─────────────────────────────────────────────
# DATA HELPERS
# ─────────────────────────────────────────────

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def to_nse(symbol):
    """Convert plain symbol to NSE format e.g. RELIANCE → RELIANCE.NS"""
    symbol = symbol.upper().strip()
    if not symbol.endswith(".NS") and not symbol.endswith(".BO"):
        symbol += ".NS"
    return symbol


# ─────────────────────────────────────────────
# FEATURE 1: LIVE PRICE
# ─────────────────────────────────────────────

def cmd_price(symbol):
    """Check live price of a stock."""
    nse_symbol = to_nse(symbol)
    console.print(f"\n🔍 Fetching price for [bold cyan]{symbol.upper()}[/bold cyan]...")

    try:
        ticker = yf.Ticker(nse_symbol)
        info = ticker.info
        price = info.get("currentPrice") or info.get("regularMarketPrice")
        name = info.get("longName") or info.get("shortName") or symbol.upper()
        change = info.get("regularMarketChange", 0)
        change_pct = info.get("regularMarketChangePercent", 0)
        day_high = info.get("dayHigh", "N/A")
        day_low = info.get("dayLow", "N/A")

        if price is None:
            console.print(f"[red]❌ Could not fetch price for '{symbol}'. Check the symbol and try again.[/red]")
            return

        color = "green" if change >= 0 else "red"
        arrow = "▲" if change >= 0 else "▼"

        panel_text = Text()
        panel_text.append(f"{name}\n", style="bold white")
        panel_text.append(f"₹{price:,.2f}  ", style=f"bold {color} underline")
        panel_text.append(f"{arrow} {abs(change):.2f} ({abs(change_pct):.2f}%)\n", style=f"{color}")
        panel_text.append(f"\nDay High: ₹{day_high}   Day Low: ₹{day_low}", style="dim")

        console.print(Panel(panel_text, title=f"[bold]{nse_symbol}[/bold]", border_style=color))

    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")


# ─────────────────────────────────────────────
# FEATURE 2: ADD STOCK TO PORTFOLIO
# ─────────────────────────────────────────────

def cmd_add(symbol, quantity, buy_price):
    """Add a stock to your portfolio."""
    nse_symbol = to_nse(symbol)
    data = load_data()

    entry = {
        "symbol": nse_symbol,
        "quantity": float(quantity),
        "buy_price": float(buy_price),
        "added_on": datetime.now().strftime("%Y-%m-%d")
    }

    data[nse_symbol] = entry
    save_data(data)

    invested = float(quantity) * float(buy_price)
    console.print(f"\n✅ Added [bold cyan]{nse_symbol}[/bold cyan] to your portfolio.")
    console.print(f"   {quantity} shares @ ₹{float(buy_price):,.2f} = [bold]₹{invested:,.2f}[/bold] invested")


# ─────────────────────────────────────────────
# FEATURE 3: PORTFOLIO OVERVIEW + GAIN/LOSS
# ─────────────────────────────────────────────

def cmd_show():
    """Show your full portfolio with gain/loss."""
    data = load_data()

    if not data:
        console.print("\n[yellow]📭 Your portfolio is empty. Add stocks using:[/yellow]")
        console.print("   [bold]python portfolio.py add RELIANCE 10 2500[/bold]")
        return

    console.print("\n📊 [bold]Fetching live prices...[/bold]")

    table = Table(
        title="💰 My Portfolio",
        box=box.ROUNDED,
        show_header=True,
        header_style="bold magenta",
        border_style="dim"
    )

    table.add_column("Stock", style="bold cyan", no_wrap=True)
    table.add_column("Qty", justify="right")
    table.add_column("Buy Price", justify="right")
    table.add_column("Current", justify="right")
    table.add_column("Invested", justify="right")
    table.add_column("Current Value", justify="right")
    table.add_column("Gain / Loss", justify="right")
    table.add_column("Return %", justify="right")

    total_invested = 0
    total_current = 0

    for symbol, entry in data.items():
        qty = entry["quantity"]
        buy_price = entry["buy_price"]
        invested = qty * buy_price

        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            current_price = info.get("currentPrice") or info.get("regularMarketPrice")

            if current_price is None:
                current_price = buy_price  # fallback
                price_str = f"₹{current_price:,.2f} [dim](stale)[/dim]"
            else:
                price_str = f"₹{current_price:,.2f}"

        except:
            current_price = buy_price
            price_str = f"₹{current_price:,.2f} [dim](err)[/dim]"

        current_value = qty * current_price
        gain = current_value - invested
        gain_pct = (gain / invested) * 100

        total_invested += invested
        total_current += current_value

        gain_str = f"₹{gain:+,.2f}"
        pct_str = f"{gain_pct:+.2f}%"
        color = "green" if gain >= 0 else "red"

        table.add_row(
            symbol.replace(".NS", ""),
            str(int(qty)),
            f"₹{buy_price:,.2f}",
            price_str,
            f"₹{invested:,.2f}",
            f"₹{current_value:,.2f}",
            f"[{color}]{gain_str}[/{color}]",
            f"[{color}]{pct_str}[/{color}]"
        )

    console.print(table)

    # Summary
    total_gain = total_current - total_invested
    total_pct = (total_gain / total_invested) * 100 if total_invested else 0
    color = "green" if total_gain >= 0 else "red"
    arrow = "▲" if total_gain >= 0 else "▼"

    summary = (
        f"Total Invested: [bold]₹{total_invested:,.2f}[/bold]   "
        f"Current Value: [bold]₹{total_current:,.2f}[/bold]   "
        f"Overall P&L: [{color}]{arrow} ₹{abs(total_gain):,.2f} ({abs(total_pct):.2f}%)[/{color}]"
    )
    console.print(Panel(summary, title="[bold]Portfolio Summary[/bold]", border_style=color))


# ─────────────────────────────────────────────
# FEATURE: REMOVE STOCK
# ─────────────────────────────────────────────

def cmd_remove(symbol):
    """Remove a stock from your portfolio."""
    nse_symbol = to_nse(symbol)
    data = load_data()

    if nse_symbol in data:
        del data[nse_symbol]
        save_data(data)
        console.print(f"\n🗑️  Removed [bold cyan]{nse_symbol}[/bold cyan] from your portfolio.")
    else:
        console.print(f"\n[yellow]'{nse_symbol}' not found in your portfolio.[/yellow]")


# ─────────────────────────────────────────────
# CLI ENTRY POINT
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="portfolio",
        description="💰 Indian Stock Portfolio Tracker"
    )
    subparsers = parser.add_subparsers(dest="command")

    # price command
    p_price = subparsers.add_parser("price", help="Get live price of a stock")
    p_price.add_argument("symbol", help="Stock symbol e.g. RELIANCE, TCS, INFY")

    # add command
    p_add = subparsers.add_parser("add", help="Add a stock to your portfolio")
    p_add.add_argument("symbol", help="Stock symbol e.g. RELIANCE")
    p_add.add_argument("quantity", type=float, help="Number of shares")
    p_add.add_argument("buy_price", type=float, help="Price you bought at (₹)")

    # show command
    subparsers.add_parser("show", help="Show your portfolio with gain/loss")

    # remove command
    p_remove = subparsers.add_parser("remove", help="Remove a stock from portfolio")
    p_remove.add_argument("symbol", help="Stock symbol to remove")

    args = parser.parse_args()

    if args.command == "price":
        cmd_price(args.symbol)
    elif args.command == "add":
        cmd_add(args.symbol, args.quantity, args.buy_price)
    elif args.command == "show":
        cmd_show()
    elif args.command == "remove":
        cmd_remove(args.symbol)
    else:
        console.print(Panel(
            "[bold cyan]💰 portfolio — Indian Stock Tracker[/bold cyan]\n\n"
            "[white]Commands:[/white]\n"
            "  [green]python portfolio.py price RELIANCE[/green]         → Live price\n"
            "  [green]python portfolio.py add RELIANCE 10 2500[/green]   → Add to portfolio\n"
            "  [green]python portfolio.py show[/green]                   → Portfolio + P&L\n"
            "  [green]python portfolio.py remove RELIANCE[/green]        → Remove stock",
            title="Welcome",
            border_style="cyan"
        ))


if __name__ == "__main__":
    main()
