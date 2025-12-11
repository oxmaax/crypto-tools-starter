def future_value(
    principal: float,
    annual_rate: float,
    years: float,
    compounds_per_year: int = 1,
) -> float:
    """
    calculate future value using compound interest.

    principal: starting amount
    annual_rate: apy in decimal (e.g. 0.05 for 5%)
    years: how many years to grow
    compounds_per_year: how many times per year interest is added
    """
    factor = 1 + annual_rate / compounds_per_year
    periods = years * compounds_per_year
    return principal * (factor ** periods)


if __name__ == "__main__":
    # you can edit these values freely
    principal = 1000.0       # starting balance
    annual_rate = 0.08       # 8% apy
    years = 3                # number of years
    compounds_per_year = 12  # monthly compounding

    result = future_value(principal, annual_rate, years, compounds_per_year)

    print(f"starting balance: ${principal:,.2f}")
    print(f"apy: {annual_rate * 100:.2f}%")
    print(f"years: {years}")
    print(f"compounding: {compounds_per_year}x per year")
    print("-" * 40)
    print(f"estimated future balance: ${result:,.2f}")
