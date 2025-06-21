# src/simulation/run_simulation.py
import os
from simulation.simulator import ReflectiveSimulator
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    sim = ReflectiveSimulator(openai_key=OPENAI_API_KEY)
    initial_context = "Team planning Q3 roadmap"
    sim.simulate(context=initial_context, goal="Finalize milestones", runs=3, steps=4)


// run via bash as python src/simulation/run_simulation.py
