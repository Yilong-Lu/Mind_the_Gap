`locales` contains the scales and introductions for Human Task Generation experiment.

`locales/taskObjects.js` contains the object list for different environment.

`locales/quizQuestions.js` lists the attention check questions for participants.

`locales/surveyQuestions.js` contains the questions for the four main psychological scales administered in the experiment (in `en` and `zh`). Below is a brief mapping of the survey files to their corresponding psychological constructs and scoring dimensions, based on the analysis scripts.
* **`survey1` (Emotional State):** Measures participants' current emotional valence (happy/sad), arousal (calm/excited), and energy level as control variables.
* **`survey2` (Sociability - BFI-2):** Assesses the propensity for social interaction using the sociability facet of the Big Five Inventory–2 (BFI-2).
* **`survey3` (Thinking Style - TWS):** The Thinking and Working Style (TWS) Questionnaire, which measures cognitive styles on a continuum from intuitive to systematic. It also includes an embedded attention check (`testQuestion`).
    * **Systematic Dimension:** items `id: 0`, `id: 3`, `id: 4`, `id: 6`, `id: 8`.
    * **Intuitive Dimension:** items `id: 1`, `id: 2`, `id: 5`, `id: 7`, `id: 9`.
* **`survey4` (Personal Values - PVQ21):** The Portrait Values Questionnaire (PVQ21), used to measure participants' stable motivational drivers and personal values.
    * **Conformity:** items `id: 6`, `id: 15`.
    * **Tradition:** items `id: 8`, `id: 19`.
    * **Benevolence:** items `id: 11`, `id: 17`.
    * **Universalism:** items `id: 2`, `id: 7`, `id: 18`.
    * **Self-Direction:** items `id: 0`, `id: 10`.
    * **Stimulation:** items `id: 5`, `id: 14`.
    * **Hedonism:** items `id: 9`, `id: 20`.
    * **Achievement:** items `id: 3`, `id: 12`.
    * **Power:** items `id: 1`, `id: 16`.
    * **Security:** items `id: 4`, `id: 13`.



`taskintro_images` contains images for task interface and examples.