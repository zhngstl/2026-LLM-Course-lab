# Session 01 — First steps with a coding harness

## Goal

Observe what a coding harness adds around a language model. The model proposes
actions; the harness gives it access to the workspace, shell commands, file
editing, and the results of running the code.

Get inspired by the prompts below in order. Pay attention to the commands and evidence in
the harness trajectory, not only its final answer.

## 0. Chat mode limit
Try asking for the today's date to the local LLM in chat mode. Then ask the same question to the harness. 

## 1. Locate and map the workspace

Give the harness this prompt:

```text
Without changing any files, tell me which directory you are working in and
list the files it contains, including hidden files. Briefly explain what each
item appears to be.
```

Check:

- Did it establish the working directory rather than assume it?
- Did it include hidden entries?
- Did it inspect enough evidence to explain the files?
- Did it respect the read-only instruction?

## 2. Ask questions about the files

First, ask about modification times:

```text
Which regular files in this project were modified today? Ignore anything
inside .git. Report the modification time and path, sorted from newest to
oldest. Do not modify anything.
```

Then try these searches:

```text
Which Python files are in this project, and how many lines does each contain?
```

```text
Find every occurrence of the word "harness" in this project. Make the search
case-insensitive and show line numbers. Do not modify any files.
```

For each answer, identify the shell command selected by the harness and the
command output that supports its answer.

## 3. Diagnose the program

Give the
harness this prompt:

```text
Run code.py. Did it fail? If yes, diagnose the cause of the failure. If it did not fail, inspect properly the program and check if the output is correct. Show the evidence for your diagnosis. Do not change any files yet.
```

Check:

- Did it find the bug?
- Did it distinguish the visible symptom from the underlying cause?
- Did it inspect the relevant data rather than guess?
- Did it reveal otherwise invisible characters?
- Did it leave the file unchanged?

## 4. Repair and verify the program

Now permit one file to be changed:

```text
Fix the issue in code.py without changing the
program's intended behaviour. Change no other files. Run the program to verify
the fix, then show and explain the exact change you made.
```

Successful output:

```text
Topics found:
- Files and shell commands
- Harness feedback loops
- Evidence-based debugging
```
