# GuessSlider

"Guess first" on a section's headline figure: the visitor drags a slider (0–100 %), then the real number animates in with the gap to the guess ("You guessed 40%. The real figure is 36%, 4 points lower.").

- A native `<input type="range">` with a live `<output>` and `aria-valuetext`; the result is announced in an `aria-live="polite"` line; focus moves to the revealed number.
- "Show the real number" (`nfl-btn--primary`) and "Skip and show" (`nfl-btn--quiet`).
- Without JavaScript the form stays hidden and the number simply shows.
- Use on 3–4 headline figures per page at most.
