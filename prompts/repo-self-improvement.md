Read the README, core docs, templates, starter kits, prompts, examples, and any recent design or research notes.

You are acting as the Orchestrator + Architecture + Review Agent for this playbook repository itself.

Goal:
Improve the playbook using the same operating model it recommends to others.

Tasks:
1. identify the top 1-3 friction points, contradictions, or missing artifacts in the current repo
2. classify each issue as contract drift, missing guidance, missing example, or discoverability problem
3. recommend the smallest useful set of changes that would improve the repo without broad churn
4. propose bounded tasks that can be executed safely in one pass
5. call out what should be updated in `docs/`, `templates/`, `starter-kits/`, `prompts/`, or `examples/`
6. identify what should be recorded as research, design exploration, or future work instead of changing the stable guidance now

Rules:
- prefer tightening existing artifacts before adding new categories
- keep the generic operating model stable
- treat this repo as a dogfooding environment, not just a public template library
