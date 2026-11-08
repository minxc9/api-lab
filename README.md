# api-lab

## Install and run

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows PowerShell
pip install -r requirements.txt
pytest -v
```

To save the output of a full run as an HTML report:

```bash
pytest -v --html=report.html --self-contained-html
```

| Characteristic | Blocks | Values in the tests |
|---|---|---|
| C1 Value of stars | below 1, 1 to 5 (base), above 5 | 0, 3, 6 |
| C2 Type of stars | whole number (base), decimal, text, missing | 3, 3.5, "3", no field |
| C3 Pizza | exists (base), does not exist | a new pizza, 999999999 |
| C4 Token | the user's own (base), none, wrong length | from auth, no header, token short |

### Base choice coverage

The base test uses every base block: 3 stars as a whole number, a pizza that exists, and the user's own token. Each other test changes one characteristic to one of its other blocks and keeps the rest at the base. That gives 1 + 2 + 3 + 1 + 2 = 9 tests.

| Characteristic | Block | Test that covers it | Expected answer |
|---|---|---|---|
| all | base (3, whole number, exists, own token) | `test_base_choice_is_saved` | 201 |
| C1 | below 1 (0) | `test_stars_out_of_range[0]` | 400, stars must be between 1 and 5 |
| C1 | above 5 (6) | `test_stars_out_of_range[6]` | 400, stars must be between 1 and 5 |
| C2 | decimal (3.5) | `test_stars_decimal_is_refused` | 400, cannot unmarshal number 3.5 |
| C2 | text ("3") | `test_stars_text_is_refused` | 400, cannot unmarshal string |
| C2 | missing | `test_stars_missing_is_refused` | 400, stars must be between 1 and 5 |
| C3 | does not exist (999999999) | `test_pizza_not_found_is_refused` | 400, pizza ID 999999999 not found |
| C4 | none | `test_no_token_is_refused` | 401, authentication failed |
| C4 | wrong length ("short") | `test_short_token_is_refused` | 401, authentication failed |