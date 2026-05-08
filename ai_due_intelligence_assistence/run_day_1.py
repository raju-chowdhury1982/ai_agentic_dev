from rich.console import Console

from app.chains import analyze_business_info

console = Console()

sample_business_info = """
A mid-sized real estate developer operates in Kolkata and nearby regions.
The company sells residential flats, leases commercial units, and manages
property maintenance for completed projects. It uses offline brokers,
Facebook ads, and local newspaper campaigns for lead generation.

The legal team handles land title verification, customer agreements,
RERA documentation, and litigation tracking manually using shared folders.
The finance team maintains project-wise cash flow in Excel. Marketing
reports are prepared weekly by two employees using manual data collection.
"""


if __name__ == "__main__":
    console.rule("[bold red]AI Business Due Diligence Assistant - Day 1[/bold red]")
    console.rule("[bold blue]Business Due Diligence Analysis[/bold blue]")
    result = analyze_business_info(sample_business_info)  # type: ignore
    console.print(result)
