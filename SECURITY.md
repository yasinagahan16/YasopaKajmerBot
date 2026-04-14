# Security Guidelines - YasopaKajmerBot

## Environment Variables

This bot requires the following environment variables to run. **Never commit sensitive credentials to the repository.**

### Setup Instructions

1. Copy the example configuration:
   ```bash
   cp .env.example .env
   ```

2. Fill in your API keys in the `.env` file:
   - **DISCORD_TOKEN**: Get from [Discord Developer Portal](https://discord.com/developers/applications)
   - **SPOTIFY_CLIENT_ID** & **SPOTIFY_CLIENT_SECRET**: Create an app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - **GENIUS_TOKEN**: Get from [Genius API Clients](https://genius.com/api-clients)

### What Gets Ignored

The following files/directories are protected and will NOT be committed:

```
.env                   # Local environment variables
.env.local            # Local overrides
venv/                 # Virtual environment
__pycache__/          # Python cache
*.db, *.sqlite*       # Database files
.cache/, .history/    # Temporary cache
logs/                 # Log files
```

## Deployment to Render

When deploying to Render, configure environment variables through the Render dashboard:

1. Go to your service settings
2. Add environment variables under "Environment"
3. Set each variable individually (DISCORD_TOKEN, SPOTIFY_CLIENT_ID, etc.)
4. **Do NOT paste `.env` file contents**

## Security Best Practices

- ✅ Store credentials in environment variables (not in code)
- ✅ Use `.env.example` to document required variables
- ✅ Review `.gitignore` before each commit
- ✅ Rotate credentials if accidentally exposed
- ✅ Use strong, unique API keys
- ✅ Check commit history for any leaked secrets

## Sensitive Data Handling

- No credentials should be logged
- Database files contain only non-sensitive bot state
- User data (if any) should be anonymized
- Review code for hardcoded strings before commits

## Report Security Issues

If you discover a security vulnerability:
1. **Do NOT** publicly disclose it on GitHub
2. Contact the repository owner privately
3. Provide details about the vulnerability
4. Allow time for a fix before disclosure

---

**Last Updated**: 2026-04-14
