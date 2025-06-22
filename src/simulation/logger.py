import json
import os
from datetime import datetime

class SimulationLogger:
    def __init__(self, out_dir: str = "simulation_logs"):
        os.makedirs(out_dir, exist_ok=True)
        self.out_dir = out_dir

    def log_run(self, run_id: int, goal: str, plan, outcomes, evals):
        timestamp = datetime.utcnow().isoformat()
        record = {
            "run_id": run_id,
            "timestamp": timestamp,
            "goal": goal,
            "plan": plan,
            "outcomes": outcomes,
            "evaluations": evals
        }
        fname = f"{self.out_dir}/run_{run_id}_{timestamp}.json"
        with open(fname, "w") as f:
            json.dump(record, f, indent=2)
        print(f"Logged simulation run {run_id} → {fname}")
