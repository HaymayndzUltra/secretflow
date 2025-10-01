require('dotenv').config();

const config = {
  // Google Cloud Configuration
  google: {
    projectId: process.env.GOOGLE_CLOUD_PROJECT_ID,
    credentialsPath: process.env.GOOGLE_APPLICATION_CREDENTIALS,
  },

  // OpenAI Configuration
  openai: {
    apiKey: process.env.OPENAI_API_KEY,
  },

  // Application Configuration
  app: {
    port: process.env.PORT || 8080,
    nodeEnv: process.env.NODE_ENV || 'development',
  },

  // Audio Configuration
  audio: {
    sampleRate: parseInt(process.env.AUDIO_SAMPLE_RATE) || 48000,
    channels: parseInt(process.env.AUDIO_CHANNELS) || 2,
  },

  // Logging Configuration
  logging: {
    level: process.env.LOG_LEVEL || 'info',
    file: process.env.LOG_FILE || 'logs/app.log',
  },

  // Security Configuration
  security: {
    jwtSecret: process.env.JWT_SECRET,
    encryptionKey: process.env.ENCRYPTION_KEY,
  },

  // Database Configuration (for analytics)
  database: {
    host: process.env.DB_HOST || 'localhost',
    port: parseInt(process.env.DB_PORT) || 5432,
    name: process.env.DB_NAME || 'ai_call_companion',
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
  }
};

module.exports = config;
