# Format icon prompts

Seven icons, one per format, to replace the code-drawn placeholders currently in
`assets/icons/formats/`.

**Save each as** `assets/icons/formats/<name>-alpha.png` — the site already asks for
those exact filenames, so a finished drawing drops straight in with no code change.

| name | shows |
|---|---|
| `video` | film camera |
| `course` | mortarboard on books |
| `docs` | open manual |
| `article` | sheet of paper |
| `repo` | terminal window |
| `hands-on` | hands on a cog |
| `podcast` | studio microphone |

After each one, run the same palette snap the role icons went through:

```
python3 scripts/normalise-icon.py assets/icons/formats/video-alpha.png assets/icons/formats/video-alpha.png
```

---

## The style block

Paste this **after** the subject line in every prompt. It is the same set of
constraints that produced the 40 role icons.

> Hand-drawn line illustration in a single flat style. Thick, uneven black marker
> outline with visible hand-drawn wobble, like a confident felt-tip sketch.
> Completely flat colour fills — no shading, no gradient, no texture, no shadow, no
> highlight, no 3D, no perspective depth.
> Use exactly these colours and no others: black #141413 for every outline, off-white
> #FAF9F5 for the main fills, warm beige #E3DACC for exactly ONE accent shape, and
> terracotta #D97757 for one very small detail only.
> Solid plain off-white #FAF9F5 background filling the whole square.
> Do NOT use transparency. Do NOT add a border, frame, drop shadow or ground line.
> Do NOT include any text, letters, numbers, logos or watermarks.
> The object is centred and fills about 90% of the square, drawn front-on.
> Simple, warm, editorial, like a woodcut redrawn with a marker pen.

---

## The seven subjects

**1. video** — save as `video-alpha.png`

> A single old-fashioned film camera seen from the front, with one large round lens and
> one film reel mounted on top. The film reel is the beige accent shape.

**2. course** — save as `course-alpha.png`

> A graduation mortarboard cap resting on top of a small stack of two closed books, seen
> at a slight angle. The mortarboard is the beige accent shape and its tassel is the
> small terracotta detail.

**3. docs** — save as `docs-alpha.png`

> A single thick reference manual standing open, pages fanned slightly, with a ribbon
> bookmark hanging from the top. The visible page block is the beige accent shape and
> the ribbon is the small terracotta detail.

**4. article** — save as `article-alpha.png`

> A single sheet of paper with four ruled lines of writing on it and one corner folded
> over. The folded corner is the beige accent shape.

**5. repo** — save as `repo-alpha.png`

> A terminal window with a rounded rectangular frame, a command prompt chevron and a
> block cursor inside, and three small dots along the top bar. The top bar is the beige
> accent shape and the cursor is the small terracotta detail.

**6. hands-on** — save as `hands-on-alpha.png`

> Two simple hands seen from above, working together on a small cog wheel — one hand
> steadying it, one hand turning it. The cog is the beige accent shape.
>
> *This is the one the placeholder gets wrong. A cog on its own reads as "settings".
> The hands are the whole point — they have to be unmistakable.*

**7. podcast** — save as `podcast-alpha.png`

> A single studio microphone on a small round desk stand, with a rounded windscreen
> grille and a curved shock mount around it. The grille is the beige accent shape.

---

## Checking a result

The role icons were judged the same way:

1. **Four colours only.** `python3 scripts/normalise-icon.py` fixes this — a generator
   will not hit exact hex values, and chasing that in the prompt wasted a lot of time
   during the role icons.
2. **Does it read at 32px?** That is the real size on a card. Shrink it and look. Fine
   internal detail disappears and the icon turns into a grey smudge.
3. **Does it sit beside the role icons without looking foreign?** Put it next to
   `assets/icons/roles/developer/basic.png` and compare stroke weight.
4. **No transparency.** Asking for a transparent background made white objects
   transparent too during the role work.
