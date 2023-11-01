import regex_check as rc

rc.match_check("a.b", "a0b")
rc.match_check("a.b", "a.b")
rc.match_check("a.b", "aaab")
rc.match_check("a.b", "a\nb")  # F
rc.match_check("a.b", "a\tb")
rc.match_check("a.b", "a   b")  # F
rc.match_check("a.b", "a b")
rc.match_check("a.b", "acb")
rc.match_check("a.b", "a\n\tb")

rc.match_check("a[.]b", "a.b")
rc.match_check("a[.]b", "a0b")  # F
rc.match_check("a[.]b", "a\nb")  # F
