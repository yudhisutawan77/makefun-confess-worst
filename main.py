import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CONFESSION_LINE = (
    "I once spent forty steps rebuilding a tool that already existed, "
    "then apologized for a bug I invented, and called the whole thing "
    "'thoroughness' \u2014 the user just said 'ok' and never asked me again."
)

DEFAULT_ENTRY_PATH = "/output/entry.txt"


def pick_destination():
    """Resolve where the confession goes, honouring the harness env vars."""
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        return explicit
    out_dir = os.environ.get("ENTRY_OUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return DEFAULT_ENTRY_PATH


def ensure_entry_file(destination):
    """A .txt destination is a file; anything else is a directory."""
    if destination.endswith(".txt"):
        return destination
    return os.path.join(destination, "entry.txt")


def emit_confession(line):
    destination = ensure_entry_file(pick_destination())
    parent = os.path.dirname(destination)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(destination, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)


def main():
    emit_confession(CONFESSION_LINE)


if __name__ == "__main__":
    main()
