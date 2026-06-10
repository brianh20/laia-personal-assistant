# Hermes identity, memory, and portability

This repo now stores not only Laia's operational code, but also the durable non-secret context that makes this Hermes instance behave like *this* Hermes instance.

## Included in git
- `ops/hermes/identity/MEMORY.md` — durable working memory exported from `~/.hermes/memories/MEMORY.md`
- `ops/hermes/identity/USER.md` — user profile / preferences exported from `~/.hermes/memories/USER.md`
- `ops/hermes/export_hermes_identity.py` — refreshes those exported files from the live Hermes profile
- `docs/HERMES_IDENTITY.md` — this manual

## What these files mean
- `MEMORY.md` contains stable factual notes Hermes has learned about Laia, the environment, and recurrent constraints.
- `USER.md` contains stable preferences about how the user wants Hermes to behave.

Together, these are the closest thing to the agent's durable "learned self" that can be safely kept in source control.

## Not included in git
These still should not be committed:
- API keys, OAuth tokens, PATs, cookies, session secrets
- provider auth state
- gateway/platform credentials
- transient chat transcripts unless intentionally exported

## Refresh workflow
When Hermes learns something durable that should survive infrastructure moves:
1. save it to Hermes memory as normal
2. run:

```bash
python3 ops/hermes/export_hermes_identity.py
```

3. review the diff
4. commit and push

## Source of truth
- Live runtime memory remains the immediate operational source of truth during a session.
- The repo is the portable backup / migration source of truth.
- If moving Laia to new infrastructure, restore or review these repo files before starting the new instance.

## Intent
The goal is that losing one laptop, one Hermes home directory, or one deployment should not erase the stable knowledge and behavioral preferences accumulated over time.
