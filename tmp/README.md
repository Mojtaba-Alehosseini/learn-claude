# tmp/

Scratch space. Gitignored except for this file.

Patch scripts, probe output, intermediate JSON — anything that exists to get a job done
and has no business in the repository afterwards. Two rules sit behind it:

- **Never outside the repo.** Three scratch files were once written to the directory
  *above* this one, in the user's own folder, because a path was built as `ROOT + "/.."`.
  They sat there until somebody noticed.
- **Never a heredoc for anything carrying a regex or a backslash.** Write the script here
  and run the file. That rule is already in `CLAUDE.md`, and ignoring it twice produced a
  check that silently stopped checking — the matcher matched everything, no item ever
  tripped it, and the build looked healthy.
