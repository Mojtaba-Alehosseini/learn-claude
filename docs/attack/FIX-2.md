# Fix prompt — the path/role mismatch

Paste everything below the line into Claude Code, in the project folder.

---

Excellent work on the seven. One thing you flagged yourself is still open, and it is the
softer half of item 3.

Two paths declare a role and then contain no step tagged with it:

```
Your first week with Claude          declares non-technical, student, teacher, business-founder
                                     no step tagged: student, teacher
Using Claude for research…           declares researcher, student
                                     no step tagged: student
```

Every step of "Your first week" is tagged `non-technical` and nothing else — including
*Get started with Claude*, *Claude 101*, *What are Projects?* and *Why do AI models
hallucinate?*

## Read that before you fix it

Those four are not non-technical-specific resources. They are things anyone opening
Claude for the first time needs, and they have been tagged as though "not a coder" were
a topic rather than one of ten equal roles. **The likely fault is the tagging, not the
path.** A student who has never used Claude needs *Get started with Claude* exactly as
much as a non-coder does.

So this is a judgment, and I want it made one resource at a time, not with a script.

For each of the six steps in "Your first week" and the five in the research path, answer
one question: **would this person, at this level, get real value from this exact
resource?** Then do one of three things:

- **yes** → add the role to that resource in `data/items.json`
- **no** → leave the resource alone
- **no for every step in the path** → remove that role from the path's `roles` in
  `build-paths.py`, because the path is not for them and saying so is honest

Show me your reasoning per resource in one line each. I want to read the judgment, not
just the result.

## What would make this wrong

- **Do not add roles to make a check pass.** If a resource does not serve a teacher, it
  does not get tagged `teacher`, and the path drops the claim instead.
- **Do not mass-tag.** If your fix touches more than about a dozen resources, stop and
  tell me — that would mean the problem is the taxonomy, not these two paths, and that
  is a bigger decision than this prompt.
- Remember `build-paths.py` regenerates `paths.json` from its own hardcoded list. Editing
  the JSON did nothing last time.

## Then close it for good

Add a validator check: **a path may not declare a role that none of its steps serves.**
That is the rule item 3 half-fixed — it caught steps sharing no role with their path, but
not a path claiming a role no step carries. Add it to the test suite like the others.

## While you are in the data

`non-technical` currently holds 68 resources and **0 at builder level**, the largest role
in the catalogue with nothing above `confident`. If the tagging fault above is real, some
of that is likely the same cause — genuinely general resources tagged to one role. Do not
fix it here. Just tell me how many resources you think are mis-scoped this way, so I know
whether this is two paths or a catalogue-wide problem.

---

One commit. Short answer. Ask before anything large.
