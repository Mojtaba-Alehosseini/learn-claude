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

Georgia deliberately remains a defensible choice, but on grounds of licensing and weight
of download, not on grounds of colour on the page. Typographically it is the plainer of
the two and it is no darker.

Side by side at real size: `docs/design/font-weight-check.html`.

## The macOS question — `-webkit-font-smoothing`, measured 2026-08-24

`assets/css/site.css:25` sets `-webkit-font-smoothing: antialiased` on `body`. Every
number above was taken on Windows, where that declaration is inert, so the worry was
that a Mac reader sees the body copy thinner than anyone here has seen it — and Light is
already the lightest cut in the family.

### What it does on Windows: nothing

Measured on the live site. The same sentence set three times at 20px in Tiempos Fine
Light, with `antialiased`, with `auto`, and with `subpixel-antialiased`:

- All three report a different `getComputedStyle` value, so Chrome parses the property.
- All three lay out at exactly 1448.8 x 28 px. It never touches layout, only rasterising.
- At 4x zoom the three lines are indistinguishable.

That is the expected result. Chrome on Windows rasterises text through DirectWrite, and
`-webkit-font-smoothing` is a Blink property implemented against CoreGraphics — it is
parsed everywhere and acted on only on macOS. Deleting it changes nothing on Windows, and
nothing on Linux or Android either.

### What it does on macOS: only ever lightens

`antialiased` asks for greyscale antialiasing instead of the platform default. Its
effect, when it has one, is to make text thinner and lighter. It has no setting that
makes text heavier. How much it still matters is genuinely uncertain from here: macOS
disabled subpixel antialiasing system-wide in Mojave, so the default moved towards
greyscale on its own and the gap narrowed. Without a Mac that cannot be settled, and it
does not need to be.

### The answer

**Delete it.** The argument does not depend on the uncertain part.

The declaration can only push in one direction — lighter. On Windows it is measurably
inert. So removing it either changes nothing, or makes text on macOS slightly heavier
than it is today. There is no platform where removing it makes anything thinner.

The whole worry was that the body copy might be too light on a Mac. This one line is the
only thing in the stylesheet arguing for lighter, and it buys nothing anywhere. Keeping
it means carrying an unmeasurable risk in exchange for no measurable benefit.

Not a zero-change edit, and it should not be described as one: Mac readers will see
slightly heavier body copy afterwards. That is the direction we want.

Nothing was changed. This is the measurement, the decision is Morteza's.

### One thing noticed next door, not acted on

`site.css:26` sets `text-rendering: optimizeLegibility` on the same rule. Chrome enables
kerning and common ligatures by default now, so it mostly asks for what is already
happening, and historically it has been a source of rendering oddities on long documents.
Worth looking at on its own some time. It is not part of this question and was not
touched.
