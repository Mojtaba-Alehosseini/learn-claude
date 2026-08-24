# Which face for body copy — measured 2026-08-24

Measured because a review said the switch to `Tiempos Fine Light` may have overcorrected,
and quoted PIL ink coverage saying Light was well below the Georgia the site used to
render by accident. Chrome disagrees with PIL, and Chrome is what people read the site in.

Rendered with Chrome's own rasteriser on the live site, `2d` canvas, 20px, weight 400,
the longest `Skip if:` sentence in the catalogue. Two sizes: 25 device px, which is 20 CSS
px at this machine's 1.25 device pixel ratio, and 50 device px, which is the same text at
200% browser zoom.

| Face | Total ink vs Georgia | Advance | x-height | Stem solidity 100% | 200% |
|---|---|---|---|---|---|
| Tiempos Fine Light — live | **101%** | 706 px | 10.4 px | 80.3% | 89.8% |
| Tiempos Fine Medium | 151% | 744 px | 11.2 px | 85.9% | 92.1% |
| Georgia — the old accident | 100% | 739 px | 9.6 px | 87.3% | 94.0% |

"Total ink" is the sum of pixel darkness over the whole line, so it counts what the eye
receives rather than what the weight is called. "Stem solidity" is the mean of the
darkest pixel in each inked column: 100% means strokes land solid black, lower means the
antialiasing greys them out.

## What the numbers say

**Light is not lighter than Georgia.** It lays down 101% of Georgia's ink — the same
amount, inside measurement noise. The PIL figure that started this review had the
direction wrong, not merely the magnitude. PIL rasterises through FreeType with different
hinting and gamma, so it answers a question about FreeType, not about the browser.

**Medium is not a body weight.** 151% of Georgia's ink. That is half again as much, which
is why it read as bold rather than as slightly heavy. Rejecting it was right.

**The real difference is contrast, not weight.** Light's strokes render 7 points less
solid than Georgia's at 100% zoom, 80.3% against 87.3%. That is the display cut showing:
`Fine` is drawn with thin hairlines for large sizes, and at 20px the thin parts fall
between pixels and go grey. It is a true observation, and it is small, and it closes at
200% zoom where Light reaches 89.8% against Georgia's 94.0%.

**Light buys something back.** 8% more x-height and 4.5% narrower setting: bigger letters,
more of them per line, same ink. That is a good trade at a 20px reading size.

## Recommendation

Keep `Tiempos Fine Light`. The premise that started this — that Light is too thin
against what shipped before — does not survive being measured in the browser.

One thing to know before deciding, because it is the strongest argument on the other
side. `assets/css/site.css` sets `-webkit-font-smoothing: antialiased` on `body`. On
Windows that does nothing. On macOS it switches text from subpixel to greyscale
antialiasing and makes it visibly lighter. So a Mac reader sees Light thinner than these
numbers, which were taken on Windows. If Light ever does look weak, that line is the
lever to pull first, not the typeface — it is one declaration and it changes nothing else.

Georgia deliberately remains a defensible choice, but on grounds of licensing and weight
of download, not on grounds of colour on the page. Typographically it is the plainer of
the two and it is no darker.

Side by side at real size: `docs/design/font-weight-check.html`.
