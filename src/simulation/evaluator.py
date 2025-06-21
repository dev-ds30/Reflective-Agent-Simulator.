from typing import List, Dict

class PlanEvaluator:
    def __init__(self):
        # e.g. weight or rubric definitions
        self.weights = {"relevance": 0.4, "completeness": 0.3, "clarity": 0.3}

    def evaluate_step(self, step: str, outcome: str) -> Dict[str, float]:
        """
        Score a single step against its real-world outcome.
        Returns a dict of sub–scores and a composite score.
        """
        # placeholder heuristics: override with LLM or metrics
        scores = {
            "relevance": 1.0 if step.lower() in outcome.lower() else 0.5,
            "completeness": min(len(outcome) / 100, 1.0),
            "clarity": 1.0 if len(step.split()) < 20 else 0.7
        }
        composite = sum(scores[k] * self.weights[k] for k in scores)
        scores["composite"] = round(composite, 3)
        return scores

    def evaluate_plan(self, plan: List[str], outcomes: List[str]) -> List[Dict]:
        """
        Evaluate each step in plan against corresponding outcome.
        """
        results = []
        for step, out in zip(plan, outcomes):
            results.append({
                "step": step,
                "outcome": out,
                "scores": self.evaluate_step(step, out)
            })
        return results
