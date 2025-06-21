import random
from agents.agent_core import SentientAgent
from planner.sequential_planner import SequentialPlanner
from .evaluator import PlanEvaluator
from .logger import SimulationLogger

class ReflectiveSimulator:
    def __init__(self, openai_key: str):
        self.agent = SentientAgent(openai_api_key=openai_key)
        self.planner = SequentialPlanner(self.agent)
        self.evaluator = PlanEvaluator()
        self.logger = SimulationLogger()

    def simulate(self, context: str, goal: str, runs: int = 5, steps: int = 3):
        for run in range(1, runs + 1):
            # 1) Plan
            plan = self.planner.plan(context, goal, steps=steps)

            # 2) “Execute” each step (here we mock outcomes)
            outcomes = [self._mock_outcome(step) for step in plan]

            # 3) Evaluate
            evals = self.evaluator.evaluate_plan(plan, outcomes)

            # 4) Log metrics
            self.logger.log_run(run, goal, plan, outcomes, evals)

            # 5) Optionally refine context/strategy based on evals
            context = self._refine_context(context, evals)

    def _mock_outcome(self, step: str) -> str:
        # placeholder: in real world hook, replace with actual result
        return f"Result of '{step}' was {'successful' if random.random() > 0.3 else 'partial'}."

    def _refine_context(self, context: str, evals: list) -> str:
        # Simple heuristic: append lowest‑scoring step as “lesson learned”
        poorest = min(evals, key=lambda e: e["scores"]["composite"])
        lesson = f"Reflection: avoid unclear phrasing like '{poorest['step']}'"
        return context + "\n" + lesson
