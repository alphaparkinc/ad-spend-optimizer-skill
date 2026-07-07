"""
example_usage.py -- Demonstrates AdSpendOptimizerClient
"""
from client import AdSpendOptimizerClient

def main():
    client = AdSpendOptimizerClient()
    result = client.optimize_budget(
        channel_performance={
            "google": {"spend": 1000, "roas": 4.2},
            "meta": {"spend": 1500, "roas": 3.1},
            "tiktok": {"spend": 800, "roas": 2.5}
        },
        total_budget_usd=5000
    )
    print("[Ad Optimization Result]")
    print(f"Blended ROAS: {result['blended_roas']}")
    print(f"Optimal Allocation: {result['allocated_budget']}")
    print(f"Revenue Est: ${result['projected_revenue']}")

if __name__ == "__main__":
    main()
