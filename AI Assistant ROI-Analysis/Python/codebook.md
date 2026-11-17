# Codebook

## Categories

| Category | Use for |
|---|---|
| Writing & editing | Writing, rewriting, proofreading, grammar checks, emails, messages, blog posts, book chapters, marketing copy, slide content, image prompts |
| Coding & debugging | Writing code, fixing errors, explaining code, converting code between programming languages |
| Information & research | Factual questions, explanations, advice, how-to questions, math and homework problems |
| Summarizing & extraction | Summarizing, shortening, or analyzing a provided text |
| Translation | Converting text between human languages |
| Brainstorming & ideas | Lists of ideas, names, options, plans, routines (workouts, meal plans) |
| Chit-chat & role-play | Fiction, stories, fan content, role-play, greetings, small talk, questions about the AI itself |
| Other | Jailbreak attempts, automated agent prompts, unclear requests |

## Outcomes

- **useful:** the response does what was asked, clearly and correctly.
- **partial:** it helps, but is incomplete, generic, outdated, or partly wrong.
- **failed:** wrong, off-topic, a refusal, empty, or ignores the instruction.

## Rules for tricky cases

1. Label by the task, not the topic or language. A grammar check of a biology paper is Writing & editing.
2. If a prompt has two tasks, label the main one.
3. Converting code between programming languages is Coding & debugging, not Translation.
4. Fiction and role-play are Chit-chat & role-play. Writing with a practical purpose (books, marketing, education) is Writing & editing.
5. Prompts and responses are cut off at 500 characters. Judge only what is visible; if the visible part is correct and on track, mark useful.
6. If the AI invents content it couldn't access (a link, real-time data), mark failed.
7. Refusals and jailbreak attempts are marked failed, since no value was delivered.

## Exclusions

Conversations with sexual or fetish content that passed the dataset's toxicity filter were removed from the sample.

## Time assumptions

Minutes saved per conversation, by category. These are illustrative estimates, not measurements.

| Category | Low | Base | High |
|---|---|---|---|
| Writing & editing | 8 | 15 | 20 |
| Coding & debugging | 10 | 20 | 30 |
| Information & research | 3 | 7 | 10 |
| Summarizing & extraction | 6 | 12 | 15 |
| Translation | 6 | 12 | 15 |
| Brainstorming & ideas | 5 | 10 | 15 |
| Chit-chat & role-play | 0 | 0 | 0 |
| Other | 0 | 0 | 0 |

Savings count fully for useful outcomes, half for partial, and zero for failed.
