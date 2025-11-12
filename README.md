# Mind the Gap: The Divergence Between Human and LLM-Generated Tasks

**Abstract:**

    Humans constantly generate a diverse range of tasks guided by internal motivations. While generative agents powered by large language models (LLMs) aim to simulate this complex behavior, it remains uncertain whether they operate on similar cognitive principles. To address this, we conducted a task-generation experiment comparing human responses with those of an LLM (GPT-4o). We find that human task generation is consistently influenced by psychological drivers, including personal values (e.g., Openness to Change) and cognitive style. 
    Even when these psychological drivers are explicitly provided to the LLM, it fails to reflect the corresponding behavioral patterns. 
    They produce tasks that are markedly less social, less physical, and thematically biased toward abstraction. Interestingly, while the LLM's tasks were perceived as more fun and novel, 
    this highlights a disconnect between its linguistic proficiency and its capacity to generate human-like, embodied goals.
    We conclude that there is a core gap between the value-driven, embodied nature of human cognition and the statistical patterns of LLMs, highlighting the necessity of incorporating intrinsic motivation and physical grounding into the design of more human-aligned agents.

## About the project

`data` folder contains the generated tasks of GPT, matched-GPT and human response samples.

`experiment_materials` contains the materials and scale descriptions for human task generation experiment.

`TaskGenGPT` folder contains the codes for LLM task generation.

## About the Psychological Scales

This project uses several psychological scales to measure human traits. Here is a brief overview of the key scales:

### 1. PVQ-21 (Portrait Values Questionnaire)

* **What it is:** PVQ-21 measures human values based on Schwartz’s theory of basic human values. This theory proposes that all individuals share a universal structure of values organized around motivational goals such as `self-enhancement`, `self-transcendence`, `openness to change`, and `conservation`. 
* **How it works**:
In the PVQ-21, participants are presented with short verbal portraits that describe a person’s goals, aspirations, or guiding principles. They then rate how similar they are to that person on a Likert scale (e.g., from “not like me at all” to “very much like me”). Each portrait corresponds to one of the ten basic value types proposed by Schwartz (e.g., achievement, security, universalism, hedonism).


### 2. TWS (Thinking and Working Style)

* **What it is:** TWS assesses cognitive style on a spectrum from intuitive (fast, associative) to systematic (slow, deliberate) by items like “I often follow my instincts” (intuitive). This scale measures a person's preferred method for problem-solving, mapping closely to the **"System 1 vs. System 2"** concept. It helps determine if their default approach is more "heuristic-based" (fast, associative, good-enough) or "algorithmic/analytical" (slow, rule-based, deliberate).
