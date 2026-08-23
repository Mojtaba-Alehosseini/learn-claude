# Role icon prompts

**Created:** 2026-08-19
**For:** Nano Banana (or any image model)
**Style locked by:** `assets/icons/roles/student.png`

Ten icons, one per role. The style wording is identical in every prompt. Only the
object changes. That is what keeps the set consistent.

---

## How to use

1. Copy one prompt below. Generate.
2. If the result drifts, feed `assets/icons/roles/student.png` back as a **reference
   image** and say "same style, same line weight, same fill colour, but <object>".
3. Do not chase the exact colours or margin in the prompt. The model cannot hit a hex
   code. Fix it afterwards:

```
python3 scripts/normalise-icon.py <generated>.jpeg -o assets/icons/roles --transparent
```

That snaps every colour to the brand palette, crops, and re-frames to 93% fill. It is
what makes ten separately generated images look like one set.

## The style block

Every prompt below is this sentence with `<OBJECT>` swapped:

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D.
> **\<OBJECT\>.** Very thick, chunky black outline like a fat felt-tip marker — uneven
> hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line
> ends. Solid background #F0EEE6. \<ACCENT PART\> filled solid #E3DACC. All other shapes
> filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture,
> no shadow. The drawing fills almost the whole square with only a small even margin.
> Very few lines, simple and naive. No text, no letters, no numbers, no people. Square
> format.

Rules that keep the set coherent:

- **One accent shape per icon.** Exactly one thing is `#E3DACC`. Never two.
- **One or two objects.** Never three.
- **No faces, no hands, no people.** The icon is an object, not a person.
- **No text or numbers**, even on a screen or a book cover. The model will try. Say no.
- **No modern brand shapes** — no phone notches, no app icons, no logos.

---

## 1. Student — done

Object: three books stacked flat, tiny two-leaf sprout growing from the top book.
Accent: the top book and the two leaves.
File: `assets/icons/roles/student.png`

## 2. Non-technical

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A simple folded paper aeroplane flying, with one small curved dashed trail line behind it. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. The lower wing of the paper aeroplane filled solid #E3DACC. All other shapes filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Very few lines, simple and naive. No text, no letters, no numbers, no people. Square format.

## 3. Researcher

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A simple microscope seen from the side, with one small round slide on its stage. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. The body tube of the microscope filled solid #E3DACC. All other shapes filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Very few lines, simple and naive. No text, no letters, no numbers, no people. Square format.

## 4. Teacher

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A small blackboard on a simple wooden easel stand, completely blank, with one short stick of chalk resting on its ledge. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. The board surface filled solid #E3DACC. All other shapes filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Very few lines, simple and naive. No text, no letters, no numbers, no people, nothing written on the board. Square format.

## 5. Developer

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A simple rounded rectangular window frame with three small dots along its top bar and one short horizontal line inside it, like an empty terminal window. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. The top bar strip of the window filled solid #E3DACC. All other shapes filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Very few lines, simple and naive. No text, no letters, no numbers, no code, no people. Square format.

## 6. Data analyst

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. Three simple vertical bars of different heights standing side by side on one horizontal base line, like a plain bar chart. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. The tallest bar filled solid #E3DACC. All other shapes filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Very few lines, simple and naive. No text, no letters, no numbers, no axis labels, no people. Square format.

## 7. Product manager

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A simple clipboard seen from the front with a clip at the top and three short horizontal lines on it, the first line with a small tick mark beside it. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. The clip at the top filled solid #E3DACC. All other shapes filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Very few lines, simple and naive. No text, no letters, no numbers, no people. Square format.

## 8. Designer

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A wide flat paintbrush lying diagonally, with one single round drop of paint beside its tip. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. The brush bristles and the paint drop filled solid #E3DACC. All other shapes filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Very few lines, simple and naive. No text, no letters, no numbers, no people. Square format.

## 9. Business / founder

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A small shop front seen straight from the front: a simple rectangular building with a scalloped awning over a plain doorway. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. The awning filled solid #E3DACC. All other shapes filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Very few lines, simple and naive. No text, no letters, no numbers, no signage, no people. Square format.

## 10. Writer / marketer

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A fountain pen lying diagonally with its nib pointing down, and one single round ink drop below the nib. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. The pen barrel and the ink drop filled solid #E3DACC. All other shapes filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Very few lines, simple and naive. No text, no letters, no numbers, no people. Square format.

---

## Naming

Save the normalised output as the role value used in the data, so the site can find it
without a lookup table:

```
assets/icons/roles/non-technical.png
assets/icons/roles/student.png
assets/icons/roles/researcher.png
assets/icons/roles/teacher.png
assets/icons/roles/developer.png
assets/icons/roles/data-analyst.png
assets/icons/roles/pm.png
assets/icons/roles/designer.png
assets/icons/roles/business-founder.png
assets/icons/roles/writer-marketer.png
```

## Checking the set

Put all ten side by side at small size. Ask three questions:

1. Does one of them look like it came from a different set? Regenerate that one.
2. Is any of them unreadable at 48px? Simplify the object.
3. Does more than one shape carry the accent colour? Fix it — one accent per icon.

---

# Level and time icons

Eight more, in the same style but **simpler**. These sit next to small text, so they are
secondary. They must still read at 32px.

Rules for these eight, on top of the style block:

- **One motif per axis.** All four level icons are the same object; only the amount of
  beige changes. Same for time. That is what makes the progression obvious.
- **The accent colour carries the meaning here.** More beige means more. This is the one
  place where the accent is allowed to grow across a set.
- **Even simpler than the role icons.** Fewer lines. No small details.
- They must not look like any role icon. That is why level is round (moon) and time is
  an hourglass — nothing else in the role set is either shape.

Save as:

```
assets/icons/level/never-used.png   basic.png   confident.png   builder.png
assets/icons/time/under-15min.png   under-1hr.png   half-day.png   multi-day.png
```

## Level — moon phases

### never-used

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A single simple circle, like an empty new moon, drawn as one clean round outline. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. The inside of the circle filled solid #FAF9F5, with no beige anywhere. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Only one shape, extremely simple. No text, no letters, no numbers, no people, no stars, no face. Square format.

### basic

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A single simple circle, like a crescent moon, with a thin crescent sliver on the left side filled in. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. Only the thin crescent sliver, about one quarter of the circle, filled solid #E3DACC. The rest of the circle filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Only one shape, extremely simple. No text, no letters, no numbers, no people, no stars, no face. Square format.

### confident

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A single simple circle, like a half moon, split down the middle by one straight vertical line, with the left half filled in. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. Only the left half of the circle filled solid #E3DACC. The right half filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Only one shape, extremely simple. No text, no letters, no numbers, no people, no stars, no face. Square format.

### builder

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A single simple circle, like a full moon, completely filled in. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. The whole inside of the circle filled solid #E3DACC. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Only one shape, extremely simple. No text, no letters, no numbers, no people, no stars, no face. Square format.

## Time — hourglass

Same hourglass every time. Only the amount of sand changes.

### under-15min

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A simple hourglass shape: two triangles meeting at a narrow waist, with a flat bar across the top and a flat bar across the bottom. A very small amount of sand rests in the bottom chamber, filling only the narrow tip. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. Only the small patch of sand filled solid #E3DACC. Everything else filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Extremely simple, very few lines. No text, no letters, no numbers, no people, no falling grains. Square format.

### under-1hr

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A simple hourglass shape: two triangles meeting at a narrow waist, with a flat bar across the top and a flat bar across the bottom. Sand fills about one third of the bottom chamber. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. Only the sand filled solid #E3DACC. Everything else filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Extremely simple, very few lines. No text, no letters, no numbers, no people, no falling grains. Square format.

### half-day

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A simple hourglass shape: two triangles meeting at a narrow waist, with a flat bar across the top and a flat bar across the bottom. Sand fills about two thirds of the bottom chamber. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. Only the sand filled solid #E3DACC. Everything else filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Extremely simple, very few lines. No text, no letters, no numbers, no people, no falling grains. Square format.

### multi-day

> Minimalist hand-drawn line illustration, completely flat, no perspective, no 3D. A simple hourglass shape: two triangles meeting at a narrow waist, with a flat bar across the top and a flat bar across the bottom. The bottom chamber is completely full of sand, right up to the narrow waist. Very thick, chunky black outline like a fat felt-tip marker — uneven hand-drawn stroke, line weight varies slightly, wobbly and imperfect, rounded line ends. Solid background #F0EEE6. Only the sand filled solid #E3DACC. Everything else filled solid #FAF9F5. No transparency, no white, no shading, no gradient, no texture, no shadow. The drawing fills almost the whole square with only a small even margin. Extremely simple, very few lines. No text, no letters, no numbers, no people, no falling grains. Square format.

## Checking these eight

Put the four level icons in a row, then the four time icons in a row.

1. **Does the amount clearly grow left to right?** If two look the same, redo the middle one.
2. **Is the hourglass shape identical in all four?** Only the sand may change. If the
   glass itself changes shape, regenerate from the first one as a reference image.
3. **Readable at 32px?** These sit next to text, much smaller than the role icons.
