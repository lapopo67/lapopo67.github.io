# SmartPick Guide — daily publishing instructions

These are the rules for the scheduled task that adds one new buying guide per day to this Jekyll site (GitHub Pages, repo `lapopo67/lapopo67.github.io`, branch `main`).

## 1. Pick a topic

- Read `bot/topics.md`. Take the first line under **Queue** that is not already published (check `_posts/` for a matching slug).
- If the queue is empty, choose a new evergreen "best X" topic with real search demand in one of the categories: `electronics`, `personal-care`, `home`. Never repeat an existing guide.
- Move the chosen topic from **Queue** to **Published** in `bot/topics.md` with today's date.

## 2. Research (required)

- Run several web searches for current (this year) independent reviews of the topic: e.g. Wirecutter, RTINGS, TechRadar, Tom's Guide, Consumer Reports, SoundGuys, Expert Reviews, Engadget, Popular Science.
- Only recommend products that appear in at least one reputable independent review from the last 12 months and are sold on Amazon.com.
- Never invent specs, test results, prices, ratings, or quotes. If a detail can't be confirmed, leave it out.
- Paraphrase. Never copy sentences from sources; at most a few words per source.
- Do **not** claim we tested products ourselves. Phrase findings as "X's testing found…" or "reviewers note…".

## 3. Write the post

- File: `_posts/YYYY-MM-DD-slug.md` using **today's date** with a time earlier than now (e.g. `00:05:00 +0300`), otherwise Jekyll will not publish it.
- Front matter:
  ```
  ---
  title: "Best … (YEAR): …"
  description: "One or two sentences, under 160 characters."
  categories: [electronics | personal-care | home]
  date: YYYY-MM-DD 00:05:00 +0300
  ---
  ```
- Structure, following the existing posts as the template:
  1. Short intro (2–3 paragraphs) that says which sources were compared.
  2. `## Quick picks` table wrapped in `<div class="table-scroll" markdown="1">`.
  3. 4–6 product boxes, each:
     ```
     <div class="pick" markdown="1">
     <span class="label">Best overall</span>
     ### Product Name

     Why it's recommended (paraphrased, attributed).

     - **Great for:** …
     - **Keep in mind:** …

     {% include amzn.html q="Exact product name" %}
     </div>
     ```
  4. `## How to choose` with practical buying criteria.
  5. `## Bottom line`.
- Length: roughly 900–1,500 words. Plain, helpful English.
- Links to Amazon must go **only** through `{% include amzn.html q="…" %}` (it adds the Associates tag). No raw Amazon URLs, no product images, no prices in text except clearly approximate ranges ("under $100").
- Health/personal-care guides end with a one-line note that it is general information, not medical or dental advice.

## 4. Publish

- Commit with a message like `Add guide: Best … (YEAR)` and push to `main`.
- After pushing, write one line in the run summary: the post title and its URL (`https://lapopo67.github.io/<category>/<slug>/`).

## Never

- Never change `_config.yml` (including `amazon_tag`), layouts, or legal pages (`disclosure.md`, `privacy.md`) unless the owner asks.
- Never delete or rewrite existing posts.
- Never post anything outside this repository.
