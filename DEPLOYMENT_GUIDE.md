# Deployment Guide - Movie Recap AI

Complete instructions for deploying the Movie Recap AI Streamlit application to cloud platforms.

## Table of Contents

1. [Railway Deployment](#railway-deployment)
2. [Render Deployment](#render-deployment)
3. [DigitalOcean Deployment](#digitalocean-deployment)
4. [Environment Variables](#environment-variables)
5. [Troubleshooting](#troubleshooting)

---

## Railway Deployment

Railway is the easiest platform for deploying Streamlit apps. It offers a free tier and automatic deployments from GitHub.

### Prerequisites

- GitHub account with the project repository
- Railway account (free tier available at [railway.app](https://railway.app))
- Gemini API key

### Step-by-Step Deployment

**1. Push Code to GitHub**

```bash
# Initialize git repository if not already done
git init
git add .
git commit -m "Initial commit: Movie Recap AI Streamlit app"

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/movie_recap_streamlit.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**2. Connect Railway to GitHub**

1. Visit [railway.app](https://railway.app)
2. Click "Login with GitHub" and authorize Railway
3. Click "Create New Project"
4. Select "Deploy from GitHub repo"
5. Select your `movie_recap_streamlit` repository
6. Railway will automatically detect the Dockerfile and start building

**3. Configure Environment Variables**

1. In Railway dashboard, go to your project
2. Click the "Variables" tab
3. Add the following environment variables:

```
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here (optional)
MAX_FILE_SIZE_MB=500
```

**4. Configure Streamlit Settings**

Create a `.streamlit/config.toml` file in your project:

```toml
[server]
port = 8501
headless = true
runOnSave = true
maxUploadSize = 500

[client]
showErrorDetails = true
```

**5. Wait for Deployment**

Railway will automatically build and deploy your app. Once complete, you'll receive a public URL like: `https://movie-recap-ai-production.up.railway.app`

### Monitoring and Logs

- View deployment logs: Click "Deployments" tab in Railway dashboard
- View real-time logs: Click "Logs" tab
- Monitor resource usage: Check "Monitoring" section

---

## Render Deployment

Render offers a straightforward deployment process with free tier support for Streamlit apps.

### Prerequisites

- GitHub account with the project repository
- Render account (free tier available at [render.com](https://render.com))
- Gemini API key

### Step-by-Step Deployment

**1. Push Code to GitHub**

Follow the same steps as Railway (see above).

**2. Create New Web Service on Render**

1. Visit [render.com](https://render.com)
2. Click "New +" and select "Web Service"
3. Select "Deploy an existing repository"
4. Connect your GitHub account if not already connected
5. Select the `movie_recap_streamlit` repository

**3. Configure Service Settings**

Fill in the following information:

| Setting | Value |
|---------|-------|
| Name | movie-recap-ai |
| Environment | Docker |
| Region | Select closest to your users |
| Branch | main |

**4. Set Environment Variables**

1. Scroll to "Environment" section
2. Add the following variables:

```
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
MAX_FILE_SIZE_MB=500
```

**5. Configure Build Settings**

- Build Command: (leave empty - Dockerfile handles it)
- Start Command: (leave empty - Dockerfile handles it)

**6. Deploy**

1. Click "Create Web Service"
2. Render will build and deploy your application
3. Once complete, you'll receive a URL like: `https://movie-recap-ai.onrender.com`

### Important Notes for Render

The free tier on Render has the following limitations:

- Services spin down after 15 minutes of inactivity
- Limited to 0.5 CPU and 512 MB RAM
- For production use, upgrade to a paid plan

To avoid spindown, you can add a monitoring service or upgrade to a paid tier.

---

## DigitalOcean Deployment

DigitalOcean provides more control and better performance through App Platform or Droplets.

### Option A: DigitalOcean App Platform (Recommended)

**Prerequisites**

- DigitalOcean account (free $200 credit for new users)
- GitHub account with the project repository
- Gemini API key

**Step-by-Step Deployment**

**1. Push Code to GitHub**

Follow the same steps as Railway (see above).

**2. Create App on DigitalOcean**

1. Visit [cloud.digitalocean.com](https://cloud.digitalocean.com)
2. Click "Apps" in the left sidebar
3. Click "Create App"
4. Select "GitHub" as the source
5. Authorize DigitalOcean to access your GitHub account
6. Select the `movie_recap_streamlit` repository

**3. Configure App Settings**

1. App name: `movie-recap-ai`
2. Source branch: `main`
3. Dockerfile path: `./Dockerfile`

**4. Set Environment Variables**

1. Click "Edit" on the app
2. Go to "Environment" tab
3. Add the following variables:

```
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
MAX_FILE_SIZE_MB=500
```

**5. Configure Resource Allocation**

- Instance type: Basic (1 GB RAM, 1 vCPU)
- HTTP Port: 8501
- Health check path: `/_stcore/health`

**6. Deploy**

1. Click "Create Resources"
2. DigitalOcean will build and deploy your app
3. Your app will be available at: `https://movie-recap-ai-xxxxx.ondigitalocean.app`

### Option B: DigitalOcean Droplet (Advanced)

For more control and better performance, deploy to a Droplet:

**1. Create Droplet**

1. Click "Droplets" in DigitalOcean dashboard
2. Click "Create Droplet"
3. Choose image: Ubuntu 22.04 LTS
4. Choose plan: Basic ($5/month or higher)
5. Select region closest to your users
6. Add SSH key for secure access
7. Click "Create Droplet"

**2. SSH into Droplet**

```bash
ssh root@your_droplet_ip
```

**3. Install Docker**

```bash
# Update system
apt-get update && apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Docker Compose
curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

**4. Clone Repository and Deploy**

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/movie_recap_streamlit.git
cd movie_recap_streamlit

# Create .env file
cp .env.example .env
# Edit .env with your API keys
nano .env

# Start the application
docker-compose up -d
```

**5. Set Up Reverse Proxy (Optional but Recommended)**

Install Nginx to proxy traffic to Streamlit:

```bash
apt-get install -y nginx

# Create Nginx configuration
cat > /etc/nginx/sites-available/default << 'EOF'
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOF

# Restart Nginx
systemctl restart nginx
```

**6. Access Your Application**

Your app will be available at: `http://your_droplet_ip`

---

## Environment Variables

All deployment platforms require the following environment variables:

| Variable | Required | Description |
|----------|----------|-------------|
| GEMINI_API_KEY | Yes | Google Gemini API key from [aistudio.google.com](https://aistudio.google.com) |
| OPENAI_API_KEY | No | OpenAI API key (optional, for advanced features) |
| MAX_FILE_SIZE_MB | No | Maximum upload file size in MB (default: 500) |
| TEMP_DIR | No | Temporary directory path (default: ./temp_files) |
| OUTPUT_DIR | No | Output directory path (default: ./output_files) |

### Getting Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com)
2. Click "Get API Key"
3. Click "Create API Key in new project"
4. Copy the generated API key
5. Add to your deployment platform's environment variables

---

## Troubleshooting

### Issue: "Gemini API key not found"

**Solution:** Verify the environment variable is correctly set in your deployment platform:

- **Railway:** Check Variables tab
- **Render:** Check Environment section
- **DigitalOcean:** Check Environment variables in App Platform settings

### Issue: "FFmpeg not found"

**Solution:** The Dockerfile includes FFmpeg installation. If this error occurs:

1. Rebuild the Docker image: `docker build --no-cache .`
2. Redeploy to your platform
3. Clear platform cache if available

### Issue: "Out of memory" or "Timeout"

**Solution:** These errors typically occur when processing large video files. Options:

1. Increase instance size (upgrade to paid tier)
2. Reduce maximum file size: Set `MAX_FILE_SIZE_MB=200`
3. Use smaller video files for testing

### Issue: "Whisper model download fails"

**Solution:** The Whisper model (~1.4GB) downloads on first use. This may fail on resource-constrained environments:

1. Pre-download the model locally
2. Include in Docker image (requires custom Dockerfile modification)
3. Upgrade to a larger instance with more storage

### Issue: "Application runs slowly"

**Solution:** Performance depends on instance resources:

1. Upgrade to a larger instance (more CPU/RAM)
2. Use medium or long recap lengths instead of short
3. Ensure stable internet connection
4. Check platform's resource monitoring for bottlenecks

### Issue: "Port 8501 already in use"

**Solution:** Streamlit is configured to use port 8501. If this port is in use:

1. Change port in Dockerfile: Replace `8501` with available port
2. Update docker-compose.yml port mapping
3. Redeploy application

---

## Production Best Practices

### Security

1. **Never commit API keys:** Use environment variables only
2. **Use HTTPS:** All deployment platforms support HTTPS by default
3. **Monitor logs:** Regularly check logs for errors or suspicious activity
4. **Update dependencies:** Keep Python packages up to date

### Performance

1. **Enable caching:** Streamlit caches function results automatically
2. **Optimize models:** Use smaller Whisper model if needed
3. **Monitor resources:** Watch CPU and memory usage
4. **Scale horizontally:** Use load balancing for high traffic

### Reliability

1. **Set up monitoring:** Enable health checks on your platform
2. **Configure auto-restart:** Most platforms support this
3. **Backup data:** Regularly backup generated scripts and audio files
4. **Test deployments:** Test in staging before production

---

## Comparison Table

| Feature | Railway | Render | DigitalOcean App | DigitalOcean Droplet |
|---------|---------|--------|------------------|----------------------|
| Free Tier | Yes | Yes | Limited | No |
| Ease of Setup | Very Easy | Easy | Medium | Hard |
| Performance | Good | Good | Excellent | Excellent |
| Customization | Limited | Limited | Good | Excellent |
| Cost | $5/month+ | $7/month+ | $5/month+ | $5/month+ |
| Auto-scaling | Yes | No | Yes | Manual |
| Support | Good | Good | Excellent | Self-managed |

---

## Next Steps

1. Choose a deployment platform based on your needs
2. Follow the step-by-step instructions for your chosen platform
3. Configure environment variables with your API keys
4. Deploy and test the application
5. Monitor logs and performance
6. Share the live URL with users

For additional help, refer to the platform's documentation or contact their support team.

---

**Last Updated:** March 31, 2026

For the latest deployment options and updates, check the official documentation of your chosen platform.
