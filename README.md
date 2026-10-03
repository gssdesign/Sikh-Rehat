# ਸਿੱਖ ਰਹਿਤ · Sikh Rehat

A mobile web app that presents 64 rules of Sikh conduct from the three rahit texts attributed to Bhai Nand Lal Goya (Tankhahnama, Prashan-Uttar and Sakhi Rahit Ki), one rule per swipeable card.

**Open it:** https://gssdesign.github.io/Sikh-Rehat/

## Features

- One card per rule: an icon, the Gurmukhi wording, the English translation, the source verse, an explanation, the Gurbani reference and notes
- Swipe between cards with a page-turn animation
- Search in Gurmukhi or English, and filter by type (Do, Don't, Ideal, Vision) and by theme
- A Nitnem checklist built from the daily-discipline rules, with a calendar that marks each day all of them were followed
- A "Pending check" badge on rules whose source text still needs checking against a printed edition
- Installable: open it on a phone and use **Add to Home Screen**

Ticks and calendar marks are stored only in the browser on that device.

## About the content

The rules, verses and explanations come only from [`nand_lal_rahit_rules.json`](nand_lal_rahit_rules.json). The app does not generate religious text.

- The Gurmukhi and English wording at the top of each card is a simplified modern rendering, not scripture.
- Verse numbers follow the 62-verse online edition of the Tankhahnama.
- Rules 38, 43, 57 and 63 carry a historical-context note written for this app. It explains that these lines are 18th-century verse and are not instructions or hostility toward any community.
- Several items are still open before the content can be considered final: see `open_items_before_launch` in the dataset. Translations await review by a qualified granthi or Sikh studies scholar.

This is not the SGPC Sikh Rehat Maryada (1945), which is a separate code of conduct.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | The built app (dataset inlined). This is what GitHub Pages serves. |
| `app.src.html` | App source: markup, styles and script |
| `nand_lal_rahit_rules.json` | The rules dataset |
| `build.py` | Inlines the dataset into the app |
| `manifest.webmanifest`, `icons/` | Home-screen install name, colours and icons |

## Editing

Change `app.src.html` or the dataset, then rebuild:

```bash
python3 build.py
```

Commit the regenerated `index.html` along with your change.
