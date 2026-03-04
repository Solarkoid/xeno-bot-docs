# <Page Title>

One-sentence summary of what this page covers and who it is for.

----

## Quick facts

- **Applies to:** <feature/system/command>
- **Required permissions:** <none/admin/manage server/etc>
- **Related pages:** [Configuration](Self Hosting/Configuration.md), [FAQ](FAQ.md)
- **Last updated:** <YYYY-MM-DD>

## Overview

Use this section for context and expected outcomes.

### Key points

- Point one
- Point two
- Point three

!!! note "Tip"
    Put important guidance here.

!!! warning "Important"
    Call out breaking behavior, risk, or common mistakes.

## Step-by-step

1. First step.
2. Second step.
3. Verify result.

### Example command

```bash
/xeno <subcommand> <required-arg> [optional-arg]
```

### Example output

```text
✅ Action completed.
```

## Configuration reference

| Setting | Type | Default | Required | Description |
|---|---|---|---|---|
| `feature.enabled` | boolean | `true` | Yes | Enables the feature |
| `feature.limit` | integer | `10` | No | Max items processed |

## Command reference template

Use this block when documenting a command page.

### Syntax

```bash
/command <required> [optional]
```

### Arguments

| Argument | Required | Description |
|---|---|---|
| `<required>` | Yes | What this value does |
| `[optional]` | No | Optional behavior |

### Permissions

- User: <yes/no>
- Admin: <yes/no>

### Examples

```bash
/command value
/command value --flag
```

## Setup/deployment template

Use this block for installation or hosting guides.

### Prerequisites

- Requirement 1
- Requirement 2

### Install

```bash
<install command>
```

### Configure

```yaml
key: value
another_key: value
```

### Run

```bash
<run command>
```

### Verify

- Check 1
- Check 2

## Troubleshooting template

### Problem: <short issue title>

**Symptoms**

- Symptom 1
- Symptom 2

**Cause**

Brief likely cause.

**Fix**

1. First action.
2. Second action.
3. Re-test.

## FAQ entry template

### Q: <Question>

A: <Short, direct answer>.

## Changelog entry template

Use this format when adding release notes.

### <YYYY-MM-DD>

#### Added

- New feature.

#### Changed

- Updated behavior.

#### Fixed

- Bug fix.

## Writing checklist

- [ ] Title is clear and specific.
- [ ] Steps are testable.
- [ ] Commands are copy/paste safe.
- [ ] Links point to existing pages.
- [ ] No leftover placeholders.
