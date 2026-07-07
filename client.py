"""
ad-spend-optimizer-skill: Client SDK
Evaluates multi-channel ROAS performance and shifts budget to the highest return channels.
"""
from __future__ import annotations
from typing import Optional


class AdSpendOptimizerClient:
    """
    SDK for ad spend modeling.
    """

    def optimize_budget(
        self,
        channel_performance: dict,
        total_budget_usd: float,
    ) -> dict:
        total_roas = sum(float(chan.get("roas", 1.0)) for chan in channel_performance.values())
        if total_roas == 0:
            total_roas = 1.0

        allocation = {}
        projected_revenue = 0.0

        for key, chan in channel_performance.items():
            roas = float(chan.get("roas", 1.0))
            # Allocate proportion based on relative channel performance
            weight = roas / total_roas
            channel_budget = round(total_budget_usd * weight, 2)
            
            allocation[key] = channel_budget
            projected_revenue += channel_budget * roas

        return {
            "allocated_budget": allocation,
            "projected_revenue": round(projected_revenue, 2),
            "blended_roas": round(projected_revenue / max(1.0, total_budget_usd), 2)
        }
