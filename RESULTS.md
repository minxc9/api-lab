# API lab results
## Part 0
- Step 0.1, the number of pizza names: 18
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: A Hollow Romana
- Step 0.12, results of the three runs without a session (optional): FAILED, FAILED, PASSED
- Step 0.16, blocks of "how many of the three tools are excluded":
  - 0 tools excluded, input `[]`, passes
  - 1 tool excluded, inputs `["Knife"]` and `["Scissors"]`, pass (the original test covered only this block)
  - 2 tools excluded, input `["Knife", "Scissors"]`, passes
  - 3 tools excluded, input `["Knife", "Pizza cutter", "Scissors"]`, answers 500 with an empty body (Defect 1, moved to `test_all_tools_excluded_is_refused`, marked xfail)

## Defect report
- Title: Excluding all three tools returns 500 instead of 400
- Request: POST /api/pizza with a logged-in user's token and body {"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}
- Expected result: 400 with a JSON error message, because no pizza can be made
- Actual result: 500 Internal Server Error with an empty body
- Severity: Medium. No data is lost, but the app gets a server error for a normal customer choice and has no message to show the user.

## Part A
- Step A4, status codes when the other user reads, changes and deletes:

## Part B
1.
2.
3.
4.
5.
6.
7.
8.