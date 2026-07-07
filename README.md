# ad-spend-optimizer-skill

> **GenPark AI Agent Skill** -- Multi-channel ad performance optimizer.

## Quick Start

```python
from client import AdSpendOptimizerClient
client = AdSpendOptimizerClient()
res = client.optimize_budget({"google": {"roas": 5.0}, "meta": {"roas": 3.0}}, 10000)
print(res["allocated_budget"])
```
