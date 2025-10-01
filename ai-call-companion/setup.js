#!/usr/bin/env node

/**
 * AI Call Companion Setup Script
 *
 * This script helps you set up the necessary configuration for the AI Call Companion.
 * Run this before starting the application for the first time.
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function ask(question) {
  return new Promise((resolve) => {
    rl.question(question, resolve);
  });
}

async function setup() {
  console.log('🚀 AI Call Companion Setup');
  console.log('========================\n');

  console.log('This setup will help you configure the necessary API keys and settings.');
  console.log('You\'ll need:');
  console.log('1. Google Cloud Project ID');
  console.log('2. Path to Google Cloud Service Account Key');
  console.log('3. OpenAI API Key (optional for now)');
  console.log('');

  // Check if .env exists
  const envPath = path.join(__dirname, '.env');
  if (fs.existsSync(envPath)) {
    console.log('⚠️  .env file already exists. This setup will overwrite it.');
    const overwrite = await ask('Do you want to continue? (y/N): ');
    if (overwrite.toLowerCase() !== 'y') {
      console.log('Setup cancelled.');
      rl.close();
      return;
    }
  }

  // Google Cloud Setup
  console.log('\n📋 Google Cloud Setup');
  console.log('1. Go to https://console.cloud.google.com/');
  console.log('2. Create a new project or select existing one');
  console.log('3. Enable Speech-to-Text API and Natural Language API');
  console.log('4. Create a Service Account with appropriate permissions');
  console.log('5. Download the JSON key file');

  const projectId = await ask('Enter your Google Cloud Project ID: ');
  const credentialsPath = await ask('Enter path to your service account key JSON file: ');

  // OpenAI Setup (optional)
  console.log('\n🤖 OpenAI Setup (Optional for basic functionality)');
  console.log('1. Go to https://platform.openai.com/');
  console.log('2. Get your API key from API Keys section');

  const openaiKey = await ask('Enter your OpenAI API Key (press Enter to skip): ');

  // Generate secure secrets
  const jwtSecret = require('crypto').randomBytes(32).toString('hex');
  const encryptionKey = require('crypto').randomBytes(32).toString('hex');

  // Create .env content
  const envContent = `# AI Call Companion Configuration
# Generated on: ${new Date().toISOString()}

# Google Cloud Configuration
GOOGLE_CLOUD_PROJECT_ID=${projectId}
GOOGLE_APPLICATION_CREDENTIALS=${credentialsPath}

# OpenAI Configuration (for future enhancements)
OPENAI_API_KEY=${openaiKey || 'your-openai-api-key-here'}

# Application Configuration
PORT=3000
NODE_ENV=development

# Audio Configuration
AUDIO_SAMPLE_RATE=48000
AUDIO_CHANNELS=2

# Logging Configuration
LOG_LEVEL=info
LOG_FILE=logs/app.log

# Security Configuration
JWT_SECRET=${jwtSecret}
ENCRYPTION_KEY=${encryptionKey}

# Database Configuration (for future analytics)
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ai_call_companion
DB_USER=your-db-user
DB_PASSWORD=your-db-password
`;

  // Write .env file
  fs.writeFileSync(envPath, envContent);

  console.log('\n✅ Setup Complete!');
  console.log('📁 .env file created with your configuration');
  console.log('\n📋 Next Steps:');
  console.log('1. Verify your Google Cloud credentials are working');
  console.log('2. Run: npm start');
  console.log('3. Test the API: curl http://localhost:3000/health');
  console.log('\n🎉 You\'re ready to use AI Call Companion!');

  rl.close();
}

// Run setup if this file is executed directly
if (require.main === module) {
  setup().catch(console.error);
}

module.exports = { setup };
