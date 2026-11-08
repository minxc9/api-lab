import pytest


# The pizza never needs a tool that the customer excluded.
# Blocks of "how many of the three tools are excluded": 0, 1, 2, 3.
# Block 3 is tested on its own below, because no pizza can satisfy it.
@pytest.mark.parametrize(
    "excluded",
    [[], ["Knife"], ["Scissors"], ["Knife", "Scissors"]],
)
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded


# Excluding all three tools cannot be satisfied, so the API must answer
# 400 with a JSON error message, never 500.
@pytest.mark.xfail(
    reason="Defect 1: excluding all three tools answers 500 with an empty body "
    "instead of 400 with a JSON error message",
    strict=True,
)
def test_all_tools_excluded_is_refused(api, auth):
    body = {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 400
    assert "error" in res.json()