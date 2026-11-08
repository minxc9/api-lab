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
  - read (GET): 404, body {"error":"not found"}
  - change (PUT): 400, body {"error":"rating ID 12714 not found"}
  - delete (DELETE): 400, body {"error":"rating ID 12715 not found"}

## Part B
1. A real-server test can find problems between parts (e.g. the load balancer and login) and real server errors (e.g. the 500 in Step 0.16). Unit tests with stubs are still useful because they are fast and show exactly which function broke.

2. Public-token ratings are shared. A new user keeps each test's data separate. In Project 2, we can use this so each test will create and delete its own data.

3. Each server keeps its own users, and the session's AWSALB cookie keeps all requests on the same server. My three runs of Step 0.12: failed, failed, then passed. The test is flaky.

4. The block "all 3 tools excluded". A 500 with no body gives the app no message, while a 400 explains the problem. The xfail keeps the defect visible until it's fixed.

5. Base choice: 1 + 2 + 3 + 1 + 2 = 9 tests. All combinations: 3 x 4 x 2 x 3 = 72 tests.

6. 404 (read), 400 (change), 400 (delete). I expect the same code for all, like 404 or 403. It is a minor defect because the codes are inconsistent, but the rating stayed safe.

7. It returns 200 with the default user's ratings. Any 16-character token is accepted. This is a defect: a stranger could see or change other people's data without logging in.

8. An API test checks status codes and error messages better and runs faster. Only a web page test can check what the user sees on screen.