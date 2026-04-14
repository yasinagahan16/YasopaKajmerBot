# Deploying YasopaKajmerBot to Render

## Prerequisites

- Render account ([render.com](https://render.com))
- GitHub account with the bot repository
- API keys ready:
  - Discord Bot Token
  - Spotify Client ID & Secret (optional)
  - Genius API Token (optional)

## Step 1: Prepare Repository

✅ Ensure `.env` file is NOT committed (it's in `.gitignore`)
✅ Verify `.env.example` has the correct structure
✅ Check `requirements.txt` is up to date
✅ Review `SECURITY.md` for best practices

## Step 2: Create Render Service

1. Go to [render.com](https://render.com) and log in
2. Click **New +** → **Web Service**
3. Select **Deploy an existing Git repository**
4. Connect your GitHub account and select `YasopaKajmerBot`
5. Configure the service:
   - **Name**: `yasopa-kajmer-bot`
   - **Environment**: `Python 3.11`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python yasopakajmer.py`
   - **Plan**: Free or Paid (based on your needs)

## Step 3: Set Environment Variables

1. In the Render service settings, go to **Environment**
2. Add each variable individually (do NOT paste `.env` content):
   ```
   DISCORD_TOKEN=<your-discord-token>
   SPOTIFY_CLIENT_ID=<your-spotify-id>
   SPOTIFY_CLIENT_SECRET=<your-spotify-secret>
   GENIUS_TOKEN=<your-genius-token>
   ```

## Step 4: Deploy

1. Click **Deploy service**
2. Watch the build logs in the **Logs** tab
3. Once deployed, the bot will start automatically

## Step 5: Monitor & Maintain

- Check **Logs** regularly for errors
- Monitor **Metrics** for performance
- Keep dependencies updated (`requirements.txt`)
- Rotate API keys periodically

## Troubleshooting

**Bot is offline/crashed:**
- Check error logs in **Logs** tab
- Verify all environment variables are set
- Ensure Discord token is valid and active

**Bot can't connect to Spotify/YouTube:**
- Verify API credentials in Render environment
- Check API quotas in respective developer dashboards
- Review bot logs for specific error messages

**High CPU/Memory usage:**
- Check for memory leaks in bot code
- Monitor active voice connections
- Consider upgrading to a paid plan

## Security Notes

⚠️ **NEVER** commit `.env` or paste credentials in code
⚠️ **ALWAYS** use Render's environment variable system
⚠️ **ROTATE** API keys if accidentally exposed
⚠️ **REVIEW** logs for suspicious activity

---

**Last Updated**: 2026-04-14
