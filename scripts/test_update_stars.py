import os
import tempfile
import unittest

import update_stars as us

SAMPLE = """# Profile

### FreePeak projects

<!-- STARS:START -->
| Project | What it does | Language | ★ |
|---|---|---|---|
| [`alpha`](https://github.com/FreePeak/alpha) | First tool | Go | **10** |
| [`beta`](https://github.com/FreePeak/beta) | Second, tool | Rust | **30** |
| [`gamma`](https://github.com/FreePeak/gamma) | Third | Go | **20** |
<!-- STARS:END -->

Prose stays.

#### [`up/stream`](https://github.com/up/stream) — ★ 1,000

Upstream body.
"""

CURRENT = {"FreePeak/alpha": 10, "FreePeak/beta": 30, "FreePeak/gamma": 20, "up/stream": 1000}


def fetcher(values):
    return lambda repo: values[repo]


def table_rows(text):
    return [line for line in text.split("\n") if line.startswith("| [`")]


class RepoCollectionTest(unittest.TestCase):
    def test_collects_table_and_upstream_repos(self):
        self.assertEqual(
            us.repos_in(SAMPLE),
            ["FreePeak/alpha", "FreePeak/beta", "FreePeak/gamma", "up/stream"],
        )

    def test_missing_markers_raise(self):
        with self.assertRaises(ValueError):
            us.repos_in("# no table here\n")


class StarCellTest(unittest.TestCase):
    def test_star_cell_updated(self):
        out = us.apply_counts(SAMPLE, {**CURRENT, "FreePeak/alpha": 11})
        self.assertIn("| [`alpha`](https://github.com/FreePeak/alpha) | First tool | Go | **11** |", out)

    def test_rows_resorted_when_order_changes(self):
        out = us.apply_counts(SAMPLE, {**CURRENT, "FreePeak/alpha": 50, "FreePeak/beta": 5})
        names = [r.split("`")[1] for r in table_rows(out)]
        self.assertEqual(names, ["alpha", "gamma", "beta"])

    def test_ties_keep_existing_order(self):
        out = us.apply_counts(SAMPLE, {**CURRENT, "FreePeak/alpha": 20, "FreePeak/gamma": 20})
        names = [r.split("`")[1] for r in table_rows(out)]
        self.assertEqual(names, ["beta", "alpha", "gamma"])


class UpstreamHeadingTest(unittest.TestCase):
    def heading_for(self, count):
        out = us.apply_counts(SAMPLE, {**CURRENT, "up/stream": count})
        return [l for l in out.split("\n") if l.startswith("#### ")][0]

    def test_thousands_commas(self):
        self.assertEqual(
            self.heading_for(12345),
            "#### [`up/stream`](https://github.com/up/stream) — ★ 12,345",
        )

    def test_no_comma_below_thousand(self):
        self.assertTrue(self.heading_for(999).endswith("★ 999"))

    def test_millions(self):
        self.assertTrue(self.heading_for(1000000).endswith("★ 1,000,000"))


class OutsideMarkersTest(unittest.TestCase):
    def test_text_outside_markers_is_byte_identical(self):
        out = us.apply_counts(SAMPLE, {**CURRENT, "FreePeak/alpha": 99, "up/stream": 2000})
        before_in, _, rest_in = SAMPLE.partition("<!-- STARS:START -->")
        before_out, _, rest_out = out.partition("<!-- STARS:START -->")
        self.assertEqual(before_in, before_out)
        # Only the upstream heading count may differ after the table region.
        after_in = rest_in.partition("<!-- STARS:END -->")[2]
        after_out = rest_out.partition("<!-- STARS:END -->")[2]
        self.assertEqual(after_in.replace("1,000", "2,000"), after_out)
        self.assertIn("Prose stays.", after_out)
        self.assertIn("Upstream body.", after_out)


class SyncFileTest(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".md")
        os.close(fd)
        with open(self.path, "w", encoding="utf-8") as f:
            f.write(SAMPLE)

    def tearDown(self):
        os.remove(self.path)

    def read(self):
        with open(self.path, encoding="utf-8") as f:
            return f.read()

    def test_noop_when_counts_current(self):
        synced = us.apply_counts(SAMPLE, CURRENT)  # already sorted and current
        with open(self.path, "w", encoding="utf-8") as f:
            f.write(synced)
        summary = us.sync_file(self.path, fetcher(CURRENT))
        self.assertEqual(summary, "no star count changes")
        self.assertEqual(self.read(), synced)

    def test_writes_and_summarises_changes(self):
        summary = us.sync_file(self.path, fetcher({**CURRENT, "FreePeak/alpha": 11}))
        self.assertEqual(summary, "updated 1 star count(s) across 4 repo(s)")
        self.assertIn("**11**", self.read())

    def test_fetch_failure_leaves_file_unwritten(self):
        def failing(repo):
            if repo == "FreePeak/beta":
                raise RuntimeError("404 Not Found")
            return CURRENT[repo]

        with self.assertRaises(RuntimeError):
            us.sync_file(self.path, failing)
        self.assertEqual(self.read(), SAMPLE)


if __name__ == "__main__":
    unittest.main()
