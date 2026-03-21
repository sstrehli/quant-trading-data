var healthData = {
  "status": "healthy",
  "timestamp": "2026-03-21T06:29:14.155020",
  "systems": {
    "paper_trading": "active",
    "model_integration": "polyclaw_connected",
    "data_pipeline": "real_market_data",
    "exit_logic": "builder_rules_active",
    "github_pages": "deployed"
  },
  "metrics": {
    "paper_positions": 11,
    "paper_trades": 45,
    "paper_capital": 10000,
    "capital_used": 3000.0,
    "capital_remaining": 7000.0,
    "total_pnl": 75.75999999999999,
    "models_integrated": 6,
    "data_source": "real_market_data",
    "edge_threshold": "greater of 0.02 or 5%",
    "exit_logic": "stop loss: greater of 5% or 0.02, trailing stop: 10%"
  },
  "builder_notes": [
    "\u2705 Models integrated with Polyclaw",
    "\u2705 Paper trading system created",
    "\u2705 Exit logic: stop loss (greater of 5% or 0.02), trailing stop (10%)",
    "\u2705 Real market data for exits",
    "\u2705 No take profit (as specified)"
  ]
};