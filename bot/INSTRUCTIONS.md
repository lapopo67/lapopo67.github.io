# SmartPick Guide — daily publishing instructions

These are the rules for the scheduled task that adds one new buying guide per day to this Jekyll site (GitHub Pages, repo `lapopo67/lapopo67.github.io`, branch `main`).

## 1. Pick a topic

- Read `bot/topics.md`. Take the first line under **Queue** that is not already published (check `_posts/` for a matching slug).
- If the queue is empty, choose a new evergreen "best X" topic with real search demand in one of the categories: `electronics`, `personal-care`, `home`. Never repeat an existing guide.
- Move the chosen topic from **Queue** to **Published** in `bot/topics.md` with today's date.

### Site focus: oral and dental care

- The site is becoming a specialist oral-care buying-guide site. Use the `personal-care` category for these posts.
- Base dental claims on established sources (ADA, NHS, peer-reviewed reviews such as Cochrane, major dental schools) in addition to product reviews, and keep them general and accurate (e.g. soft bristles, 2 minutes twice daily, cleaning between teeth daily, replacing heads about every 3 months).
- Never give individual diagnosis or treatment advice, never claim a product treats or cures a condition, and never state or imply that a dentist reviewed or wrote the post. End every oral-care post with: *This guide is general information, not personal dental advice. Ask your dentist which products suit your teeth and gums, especially if you have gum disease, implants, braces, or sensitivity.*
- Product types like night guards and whitening kits: mention when a dentist-made option is the better choice.

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

## 5. Pinterest pin (via the Buffer connector)

- Generate a 1000×1500 pin image with `bot/pin.py` (Pillow + Inter fonts):
  ```
  python3 -c "import sys; sys.path.insert(0,'bot'); from pin import make; make('assets/pins/<slug>.png','2026 buying guide','<Short title, max ~32 chars>',['Pick 1','Pick 2','Pick 3','Pick 4','Pick 5'],'<hex accent>')"
  ```
  Keep each list item under ~22 characters. Open the image and check nothing overlaps. Commit and push it with the post, then wait ~90 seconds for GitHub Pages to deploy and confirm `https://lapopo67.github.io/assets/pins/<slug>.png` loads.
- Buffer: organization "My organization" (`6b04d9b12b54d5724bdb2fac`), Pinterest channel `6b04da3e8541f09ecb80d081`, board "Best Product Picks 2026" (boardServiceId `979744162626574663`). Re-check with `get_channel` if a call fails.
- Call `create_post` with `schedulingType: automatic`, mode `addToQueue`, the image as asset (with alt text), `metadata.pinterest` = { title, url (the new guide's URL), boardServiceId }, and a 2–3 sentence description ending with 4–5 relevant hashtags.
- If the Buffer connector is unavailable or errors twice, skip the pin and say so in the run summary; the post itself is still the priority.

## Never

- Never change `_config.yml` (including `amazon_tag`), layouts, or legal pages (`disclosure.md`, `privacy.md`) unless the owner asks.
- Never delete or rewrite existing posts.
- Never post anything outside this repository.
