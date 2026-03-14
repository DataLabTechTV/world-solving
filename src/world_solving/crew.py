import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class WorldSolving:
    """WorldSolving crew for tackling critical global problems"""

    agents: list[BaseAgent]
    tasks: list[Task]

    llm = LLM(
        model=os.getenv("MODEL", "ollama/llama3.1:8b"),
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        num_ctx=2048,
        temperature=0.2,
    )

    # ----------------------------
    # Agent definitions
    # ----------------------------
    @agent
    def systems_thinker(self) -> Agent:
        return Agent(config=self.agents_config["systems_thinker"], verbose=True)  # type: ignore[index]

    @agent
    def economist(self) -> Agent:
        return Agent(config=self.agents_config["economist"], verbose=True)  # type: ignore[index]

    @agent
    def climate_scientist(self) -> Agent:
        return Agent(config=self.agents_config["climate_scientist"], verbose=True)  # type: ignore[index]

    @agent
    def public_health_expert(self) -> Agent:
        return Agent(config=self.agents_config["public_health_expert"], verbose=True)  # type: ignore[index]

    @agent
    def engineering_lead(self) -> Agent:
        return Agent(config=self.agents_config["engineering_lead"], verbose=True)  # type: ignore[index]

    @agent
    def technology_architect(self) -> Agent:
        return Agent(config=self.agents_config["technology_architect"], verbose=True)  # type: ignore[index]

    @agent
    def behavioral_scientist(self) -> Agent:
        return Agent(config=self.agents_config["behavioral_scientist"], verbose=True)  # type: ignore[index]

    @agent
    def political_strategist(self) -> Agent:
        return Agent(config=self.agents_config["political_strategist"], verbose=True)  # type: ignore[index]

    @agent
    def operations_specialist(self) -> Agent:
        return Agent(config=self.agents_config["operations_specialist"], verbose=True)  # type: ignore[index]

    @agent
    def finance_strategist(self) -> Agent:
        return Agent(config=self.agents_config["finance_strategist"], verbose=True)  # type: ignore[index]

    @agent
    def risk_analyst(self) -> Agent:
        return Agent(config=self.agents_config["risk_analyst"], verbose=True)  # type: ignore[index]

    @agent
    def ethics_advisor(self) -> Agent:
        return Agent(config=self.agents_config["ethics_advisor"], verbose=True)  # type: ignore[index]

    @agent
    def integrator(self) -> Agent:
        return Agent(config=self.agents_config["integrator"], verbose=True)  # type: ignore[index]

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(config=self.agents_config["reporting_analyst"], verbose=True)  # type: ignore[index]

    # ----------------------------
    # Task definitions (flat, single-agent)
    # ----------------------------
    @task
    def problem_identification_map_global_systems(self) -> Task:
        return Task(
            config=self.tasks_config["problem_identification_map_global_systems"]  # type: ignore[index]
        )

    @task
    def problem_identification_detect_critical_problems(self) -> Task:
        return Task(
            config=self.tasks_config["problem_identification_detect_critical_problems"]  # type: ignore[index]
        )

    @task
    def problem_identification_preliminary_impact_analysis(self) -> Task:
        return Task(
            config=self.tasks_config[  # type: ignore[index]
                "problem_identification_preliminary_impact_analysis"
            ]
        )

    @task
    def solution_design_solution_brainstorm(self) -> Task:
        return Task(config=self.tasks_config["solution_design_solution_brainstorm"])  # type: ignore[index]

    @task
    def solution_design_technical_feasibility(self) -> Task:
        return Task(config=self.tasks_config["solution_design_technical_feasibility"])  # type: ignore[index]

    @task
    def solution_design_behavioral_feasibility(self) -> Task:
        return Task(config=self.tasks_config["solution_design_behavioral_feasibility"])  # type: ignore[index]

    @task
    def feasibility_review_political_analysis(self) -> Task:
        return Task(config=self.tasks_config["feasibility_review_political_analysis"])  # type: ignore[index]

    @task
    def feasibility_review_operations_analysis(self) -> Task:
        return Task(config=self.tasks_config["feasibility_review_operations_analysis"])  # type: ignore[index]

    @task
    def feasibility_review_financial_analysis(self) -> Task:
        return Task(config=self.tasks_config["feasibility_review_financial_analysis"])  # type: ignore[index]

    @task
    def feasibility_review_risk_assessment(self) -> Task:
        return Task(config=self.tasks_config["feasibility_review_risk_assessment"])  # type: ignore[index]

    @task
    def feasibility_review_ethical_review(self) -> Task:
        return Task(config=self.tasks_config["feasibility_review_ethical_review"])  # type: ignore[index]

    @task
    def integration_cross_domain_synthesis(self) -> Task:
        return Task(config=self.tasks_config["integration_cross_domain_synthesis"])  # type: ignore[index]

    @task
    def integration_prepare_summary_for_reporting(self) -> Task:
        return Task(
            config=self.tasks_config["integration_prepare_summary_for_reporting"]  # type: ignore[index]
        )  # type: ignore[index]

    @task
    def final_reporting_compile_final_report(self) -> Task:
        return Task(
            config=self.tasks_config["final_reporting_compile_final_report"],  # type: ignore[index]
            output_file="report.md",
        )

    @task
    def final_reporting_executive_summary(self) -> Task:
        return Task(
            config=self.tasks_config["final_reporting_executive_summary"],  # type: ignore[index]
            output_file="executive_summary.md",
        )

    # ----------------------------
    # Crew definition
    # ----------------------------
    @crew
    def crew(self) -> Crew:
        """Creates the WorldSolving crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Run tasks in stage order
            manager_llm=self.llm,
            verbose=True,
        )
