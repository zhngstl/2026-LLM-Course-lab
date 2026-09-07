"""A tiny program for the Session 01 debugging exercise.
"""


def extract_topics(outline):
    """Extract topics indented with a tab."""
    return [
        line.strip()
        for line in outline.splitlines()
        if line.startswith("\t")
    ]


# The outline format requires a tab before every topic.
course_outline = """Session 01
	Files and shell commands
	Harness feedback loops
    Evidence-based debugging
"""

topics = extract_topics(course_outline)

print("Topics found:")
for topic in topics:
    print(f"- {topic}")

