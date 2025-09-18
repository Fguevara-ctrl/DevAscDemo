"""
myscripts.py

A small, beginner-friendly Python script demonstrating:
- variables and types
- functions
- user input (safe default when running non-interactively)
- conditionals
- loops
- lists and dictionaries

Run this file with: `python -m pyscripts.myscripts` or `python pyscripts/myscripts.py`
"""

from __future__ import annotations

import sys
from typing import List


def greet(name: str) -> str:
    """Return a greeting for the provided name."""
    return f"Hello, {name}! Welcome to this beginner Python script."


def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def is_even(n: int) -> bool:
    """Return True if n is even, otherwise False."""
    return n % 2 == 0


def simple_quiz(questions: List[dict]) -> int:
    """A tiny non-interactive quiz that demonstrates loops and conditionals.

    The function accepts a list of question dicts with the keys:
    - "q": question text
    - "a": integer index of the correct answer in "choices"
    - "choices": list of possible answers

    This function doesn't require input() so it can be run in CI or non-interactive
    environments. It returns the score (number of correct answers).
    """
    score = 0
    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['q']}")
        for idx, choice in enumerate(q.get("choices", []), start=1):
            print(f"  {idx}. {choice}")
        # Use the provided answer index to simulate a user's answer
        user_ans = q.get("user_ans", q.get("a", 1))
        correct_idx = q["a"]
        if (user_ans - 1) == correct_idx:
            print("  Correct!\n")
            score += 1
        else:
            print(f"  Incorrect. The correct answer was: {q['choices'][correct_idx]}\n")
    return score


def demo_noninteractive() -> None:
    """Demonstrate script behavior without requiring user input."""
    print(greet("Reader"))

    # Variables and arithmetic
    x = 3
    y = 4.5
    print(f"x = {x} (int), y = {y} (float)")
    print(f"x + y = {add_numbers(x, y)}")

    # Lists and loops
    fruits = ["apple", "banana", "cherry"]
    print("I have the following fruits:")
    for fruit in fruits:
        print(f" - {fruit}")

    # Dictionaries
    person = {"name": "Alex", "age": 30}
    print(f"Person dict: name={person['name']}, age={person['age']}")

    # Even/odd check
    n = 10
    print(f"Is {n} even? {is_even(n)}")

    # Small quiz (non-interactive)
    questions = [
        {"q": "What is 2 + 2?", "choices": ["3", "4", "5"], "a": 1, "user_ans": 2},
        {"q": "Which is a fruit?", "choices": ["Carrot", "Banana", "Potato"], "a": 1, "user_ans": 2},
    ]
    score = simple_quiz(questions)
    print(f"Quiz score: {score}/{len(questions)}")


def interactive_mode() -> None:
    """Run a tiny interactive session that asks the user's name and a number.

    If running in a non-interactive environment (no tty), the function prints a
    message and falls back to `demo_noninteractive()`.
    """
    try:
        if not sys.stdin or sys.stdin.closed:
            raise RuntimeError("No stdin")
        name = input("What's your name? ").strip() or "Friend"
        print(greet(name))

        raw = input("Enter a whole number to check even/odd: ").strip()
        n = int(raw)
        print(f"You entered {n} which is {'even' if is_even(n) else 'odd'}.")
    except (EOFError, RuntimeError):
        print("Interactive input not available — running non-interactive demo instead.\n")
        demo_noninteractive()
    except ValueError:
        print("That's not a valid integer — running non-interactive demo instead.\n")
        demo_noninteractive()


def main(argv: List[str] | None = None) -> int:
    """Main entry point. Use `--interactive` to run interactive mode."""
    argv = list(argv or sys.argv[1:])
    if "--interactive" in argv:
        interactive_mode()
    else:
        demo_noninteractive()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
