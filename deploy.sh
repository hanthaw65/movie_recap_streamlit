#!/bin/bash

# Movie Recap AI - Automated Deployment Script
# This script deploys the application to Railway

set -e

echo "🚀 Movie Recap AI - Automated Deployment"
echo "=========================================="

# Get credentials from environment variables
GITHUB_TOKEN="${GITHUB_TOKEN}"
RAILWAY_TOKEN="${RAILWAY_TOKEN}"
GEMINI_API_KEY="${GEMINI_API_KEY}"
GITHUB_USERNAME="${GITHUB_USERNAME}"
REPO_NAME="movie_recap_streamlit"

# Validate credentials
if [ -z "$GITHUB_TOKEN" ] || [ -z "$RAILWAY_TOKEN" ] || [ -z "$GEMINI_API_KEY" ] || [ -z "$GITHUB_USERNAME" ]; then
    echo "❌ Error: Missing environment variables"
    echo ""
    echo "Please set the following environment variables:"
    echo "  export GITHUB_TOKEN=your_github_token"
    echo "  export RAILWAY_TOKEN=your_railway_token"
    echo "  export GEMINI_API_KEY=your_gemini_api_key"
    echo "  export GITHUB_USERNAME=your_github_username"
    echo ""
    exit 1
fi

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${YELLOW}ℹ${NC} $1"
}

# Step 1: Initialize Git Repository
print_info "Step 1: Initializing Git Repository..."
cd /home/ubuntu/movie_recap_streamlit

if [ -d .git ]; then
    print_status "Git repository already initialized"
else
    git init
    git config user.name "Movie Recap Deploy Bot"
    git config user.email "deploy@movie-recap.local"
    print_status "Git repository initialized"
fi

# Step 2: Add all files
print_info "Step 2: Adding files to Git..."
git add .
print_status "Files added"

# Step 3: Create commit
print_info "Step 3: Creating commit..."
if git diff --cached --quiet; then
    print_status "No changes to commit"
else
    git commit -m "Initial commit: Movie Recap AI Streamlit application" || true
    print_status "Commit created"
fi

# Step 4: Add GitHub remote
print_info "Step 4: Adding GitHub remote..."
REPO_URL="https://${GITHUB_TOKEN}@github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"

if git remote get-url origin > /dev/null 2>&1; then
    print_status "Remote already exists"
    git remote set-url origin "$REPO_URL"
else
    git remote add origin "$REPO_URL"
    print_status "Remote added"
fi

# Step 5: Push to GitHub
print_info "Step 5: Pushing to GitHub..."
git branch -M main
git push -u origin main --force || {
    print_error "Failed to push to GitHub"
    echo "Please check your GitHub token"
    exit 1
}
print_status "Pushed to GitHub"

# Step 6: Create Railway project via API
print_info "Step 6: Creating Railway project..."

# Get Railway API endpoint
RAILWAY_API="https://api.railway.app/graphql"

# Create project mutation
CREATE_PROJECT=$(curl -s -X POST "$RAILWAY_API" \
  -H "Authorization: Bearer $RAILWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "mutation { projectCreate(input: {name: \"movie-recap-ai\"}) { project { id name } } }"
  }')

PROJECT_ID=$(echo "$CREATE_PROJECT" | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)

if [ -z "$PROJECT_ID" ]; then
    print_error "Failed to create Railway project"
    echo "Response: $CREATE_PROJECT"
    exit 1
fi

print_status "Railway project created: $PROJECT_ID"

# Step 7: Connect GitHub repository to Railway
print_info "Step 7: Connecting GitHub repository to Railway..."

CONNECT_REPO=$(curl -s -X POST "$RAILWAY_API" \
  -H "Authorization: Bearer $RAILWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"query\": \"mutation { githubIntegrationCreate(input: {projectId: \\\"$PROJECT_ID\\\", owner: \\\"$GITHUB_USERNAME\\\", repo: \\\"$REPO_NAME\\\"}) { integration { id } } }\"
  }")

print_status "GitHub repository connected"

# Step 8: Set environment variables
print_info "Step 8: Setting environment variables..."

SET_ENV=$(curl -s -X POST "$RAILWAY_API" \
  -H "Authorization: Bearer $RAILWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"query\": \"mutation { variableCreate(input: {projectId: \\\"$PROJECT_ID\\\", name: \\\"GEMINI_API_KEY\\\", value: \\\"$GEMINI_API_KEY\\\"}) { variable { id } } }\"
  }")

print_status "GEMINI_API_KEY set"

SET_MAX_SIZE=$(curl -s -X POST "$RAILWAY_API" \
  -H "Authorization: Bearer $RAILWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"query\": \"mutation { variableCreate(input: {projectId: \\\"$PROJECT_ID\\\", name: \\\"MAX_FILE_SIZE_MB\\\", value: \\\"500\\\"}) { variable { id } } }\"
  }")

print_status "MAX_FILE_SIZE_MB set"

# Step 9: Trigger deployment
print_info "Step 9: Triggering deployment..."

DEPLOY=$(curl -s -X POST "$RAILWAY_API" \
  -H "Authorization: Bearer $RAILWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"query\": \"mutation { deploymentTrigger(input: {projectId: \\\"$PROJECT_ID\\\"}) { deployment { id status } } }\"
  }")

print_status "Deployment triggered"

# Step 10: Wait for deployment
print_info "Step 10: Waiting for deployment to complete..."
print_info "This may take 5-10 minutes..."

RETRY_COUNT=0
MAX_RETRIES=60

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    DEPLOYMENT_STATUS=$(curl -s -X POST "$RAILWAY_API" \
      -H "Authorization: Bearer $RAILWAY_TOKEN" \
      -H "Content-Type: application/json" \
      -d "{
        \"query\": \"query { deployments(input: {projectId: \\\"$PROJECT_ID\\\", first: 1}) { edges { node { id status } } } }\"
      }")

    if echo "$DEPLOYMENT_STATUS" | grep -q "SUCCESS"; then
        print_status "Deployment successful!"
        break
    elif echo "$DEPLOYMENT_STATUS" | grep -q "FAILED"; then
        print_error "Deployment failed"
        exit 1
    fi

    echo -ne "\r⏳ Waiting... ($RETRY_COUNT/$MAX_RETRIES)"
    sleep 5
    RETRY_COUNT=$((RETRY_COUNT + 1))
done

echo ""

# Step 11: Get deployment URL
print_info "Step 11: Getting deployment URL..."

DEPLOYMENT_URL=$(curl -s -X POST "$RAILWAY_API" \
  -H "Authorization: Bearer $RAILWAY_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"query\": \"query { project(id: \\\"$PROJECT_ID\\\") { services { edges { node { deployments { edges { node { url } } } } } } }\"
  }" | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4)

if [ -z "$DEPLOYMENT_URL" ]; then
    DEPLOYMENT_URL="https://railway.app/project/$PROJECT_ID"
fi

# Final summary
echo ""
echo "=========================================="
echo -e "${GREEN}✓ Deployment Complete!${NC}"
echo "=========================================="
echo ""
echo "📱 Application Details:"
echo "  Project ID: $PROJECT_ID"
echo "  Repository: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
echo ""
echo "🌐 Access Your Application:"
echo "  URL: $DEPLOYMENT_URL"
echo ""
echo "📊 Railway Dashboard:"
echo "  https://railway.app/project/$PROJECT_ID"
echo ""
echo "⚙️  Environment Variables Set:"
echo "  ✓ GEMINI_API_KEY"
echo "  ✓ MAX_FILE_SIZE_MB"
echo ""
echo "🎉 Your Movie Recap AI is now live!"
echo ""
