"""Explainer videos. Files live in static/videos/<slug>.mp4 (+ .jpg poster).

`lesson` is (section_id, lesson_index) for videos shown at the top of a lesson,
or None for videos that only appear on the Videos page.
"""

VIDEOS = [
    {"slug": "buy-sell", "title": "Buy-sell agreements: cross-purchase vs. entity", "length": "1:23",
     "lesson": ("basics", 1), "blurb": "Who owns the policies, and why 4 owners need 12 of them."},
    {"slug": "replacement", "title": "Replacing a policy in Arizona", "length": "1:47",
     "lesson": ("basics", 3), "blurb": "The producer's and insurers' duties, and the 5-day and 30-day rules."},
    {"slug": "policy-types", "title": "Term vs. whole life vs. universal life", "length": "1:42",
     "lesson": ("policies", 0), "blurb": "How premium, coverage and cash value behave over a lifetime."},
    {"slug": "ul-options", "title": "Universal life: Option A vs. Option B", "length": "1:06",
     "lesson": ("policies", 2), "blurb": "Level vs. increasing death benefit, and the insurer's risk."},
    {"slug": "policy-timeline", "title": "The Arizona policy timeline", "length": "1:39",
     "lesson": ("provisions", 0), "blurb": "Free look, grace period, reinstatement and incontestability."},
    {"slug": "beneficiaries", "title": "Who gets paid? Beneficiary rules", "length": "1:43",
     "lesson": ("provisions", 1), "blurb": "Primary vs. contingent, revocable vs. irrevocable, simultaneous death."},
    {"slug": "per-stirpes-per-capita", "title": "Per stirpes vs. per capita", "length": "1:18",
     "lesson": ("provisions", 1), "blurb": "What happens to a share when a beneficiary dies first."},
    {"slug": "settlement-options", "title": "Settlement options", "length": "1:56",
     "lesson": ("provisions", 2), "blurb": "Lump sum, interest only, fixed period vs. fixed amount, life income."},
    {"slug": "nonforfeiture-options", "title": "Nonforfeiture options", "length": "2:06",
     "lesson": ("provisions", 3), "blurb": "Cash surrender, reduced paid-up and extended term."},
    {"slug": "annuity-phases", "title": "How an annuity works", "length": "1:48",
     "lesson": ("annuities", 0), "blurb": "Accumulation, annuitization, payout options and Arizona's free look."},
    {"slug": "mec", "title": "MECs and the 7-pay test", "length": "1:41",
     "lesson": ("tax", 1), "blurb": "What makes a policy a MEC and how withdrawals get taxed."},
    {"slug": "1035-exchanges", "title": "1035 exchanges", "length": "1:05",
     "lesson": ("tax", 2), "blurb": "Which contract swaps are tax-free, and which one isn't."},
    {"slug": "arizona-numbers", "title": "Arizona numbers in 2 minutes", "length": "2:05",
     "lesson": None, "blurb": "Every number to memorize. Watch it the morning of your exam."},
]

VIDEOS_BY_LESSON = {}
for _v in VIDEOS:
    if _v["lesson"]:
        VIDEOS_BY_LESSON.setdefault(_v["lesson"], []).append(_v)
