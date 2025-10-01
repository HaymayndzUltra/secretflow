const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');
const winston = require('winston');
const path = require('path');
const config = require('../config/environment');

// Import services
const AudioCapture = require('./audio/AudioCapture');
const SpeechService = require('./services/SpeechService');
const SuggestionService = require('./services/SuggestionService');

// Initialize Express app
const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"]
  }
});

// Configure logging
const logger = winston.createLogger({
  level: config.logging.level,
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'ai-call-companion' },
  transports: [
    new winston.transports.File({ filename: config.logging.file }),
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
      )
    })
  ],
});

// Middleware
app.use(cors());
app.use(express.json());

// Initialize services
let audioCapture;
let speechService;
let suggestionService;

async function initializeServices() {
  try {
    logger.info('Initializing AI Call Companion services...');

    // Initialize audio capture
    audioCapture = new AudioCapture(config);
    await audioCapture.initialize();

    // Initialize speech service
    speechService = new SpeechService(config);

    // Initialize suggestion service
    suggestionService = new SuggestionService(config);

    logger.info('All services initialized successfully');
  } catch (error) {
    logger.error('Failed to initialize services:', error);
    throw error;
  }
}

// Socket.io connection handling
io.on('connection', (socket) => {
  logger.info(`Client connected: ${socket.id}`);

  socket.on('start-call', async (data) => {
    try {
      const { sessionId } = data;

      logger.info(`Starting call session: ${sessionId}`);

      // Start recording
      await audioCapture.startRecording(sessionId);

      // Set up real-time transcription
      const transcriptionStream = await speechService.transcribeStreaming(
        getAudioStream(), // You'll need to implement this based on your audio source
        {
          languageCode: 'en-US',
          alternativeLanguages: ['fil-PH'],
          enableSpeakerDiarization: true
        }
      );

      // Listen for transcription events and generate suggestions
      speechService.on('transcription', async (data) => {
        socket.emit('transcription', data);

        // Generate live suggestion if transcript is final
        if (data.isFinal && data.transcript) {
          try {
            const suggestion = await suggestionService.generateSuggestion(data.transcript, { speaker: data.speaker });
            socket.emit('suggestion', { transcript: data.transcript, suggestion, speaker: data.speaker });
          } catch (error) {
            logger.error('Error generating suggestion:', error);
            socket.emit('error', { message: 'Failed to generate suggestion' });
          }
        }
      });

      socket.emit('call-started', { sessionId, status: 'recording' });

    } catch (error) {
      logger.error('Error starting call:', error);
      socket.emit('error', { message: error.message });
    }
  });

  socket.on('stop-call', async () => {
    try {
      const recording = await audioCapture.stopRecording();
      socket.emit('call-stopped', { recording });
      logger.info(`Call stopped for session: ${recording?.sessionId}`);
    } catch (error) {
      logger.error('Error stopping call:', error);
      socket.emit('error', { message: error.message });
    }
  });

  socket.on('get-suggestion', async (data) => {
    try {
      const { transcript, speaker } = data;
      if (suggestionService && suggestionService.openai) {
        const suggestion = await suggestionService.generateSuggestion(transcript, { speaker });
        socket.emit('suggestion', { transcript, suggestion, speaker });
      } else {
        socket.emit('suggestion', { transcript, suggestion: 'Suggestions disabled: No OpenAI key configured.', speaker });
      }
    } catch (error) {
      logger.error('Error generating suggestion:', error);
      socket.emit('error', { message: 'Failed to generate suggestion' });
    }
  });

  socket.on('get-devices', async () => {
    try {
      const devices = await audioCapture.getAudioDevices();
      socket.emit('devices', { devices });
    } catch (error) {
      logger.error('Error getting devices:', error);
      socket.emit('error', { message: error.message });
    }
  });

  socket.on('disconnect', () => {
    logger.info(`Client disconnected: ${socket.id}`);
  });
});

// API Routes
app.get('/', (req, res) => {
  res.json({
    name: 'AI Call Companion',
    version: '1.0.0',
    description: 'Advanced Real-Time AI Assistant for Live Client Calls',
    status: 'running',
    endpoints: {
      health: 'GET /health',
      supportedLanguages: 'GET /supported-languages',
      transcribe: 'POST /transcribe',
      websocket: 'Real-time WebSocket events for live calls',
      webInterface: 'GET /interface - Visual web interface for testing'
    },
    documentation: 'See README.md for detailed usage instructions',
    timestamp: new Date().toISOString()
  });
});

// Serve the web interface
app.get('/interface', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.get('/', (req, res) => {
  res.json({
    name: 'AI Call Companion',
    version: '1.0.0',
    description: 'Advanced Real-Time AI Assistant for Live Client Calls',
    status: 'running',
    endpoints: {
      health: 'GET /health',
      supportedLanguages: 'GET /supported-languages',
      transcribe: 'POST /transcribe',
      websocket: 'Real-time WebSocket events for live calls'
    },
    documentation: 'See README.md for detailed usage instructions',
    timestamp: new Date().toISOString()
  });
});

// Serve the web interface
app.get('/interface', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    services: {
      audioCapture: !!audioCapture,
      speechService: !!speechService,
      suggestionService: !!suggestionService && !!suggestionService.openai
    }
  });
});

app.get('/supported-languages', async (req, res) => {
  try {
    const languages = await speechService.getSupportedLanguages();
    res.json({ languages });
  } catch (error) {
    logger.error('Error getting supported languages:', error);
    res.status(500).json({ error: error.message });
  }
});

app.post('/transcribe', async (req, res) => {
  try {
    const { filePath, options } = req.body;

    if (!filePath) {
      return res.status(400).json({ error: 'File path is required' });
    }

    // Validate file
    await speechService.validateAudioFile(filePath);

    // Transcribe
    const results = await speechService.transcribeAudio(filePath, options);

    res.json({ results });
  } catch (error) {
    logger.error('Transcription error:', error);
    res.status(500).json({ error: error.message });
  }
});

// Error handling middleware
app.use((error, req, res, next) => {
  logger.error('Unhandled error:', error);
  res.status(500).json({ error: 'Internal server error' });
});

// Graceful shutdown
process.on('SIGTERM', async () => {
  logger.info('SIGTERM received, shutting down gracefully');
  if (audioCapture) {
    await audioCapture.stopRecording();
  }
  server.close(() => {
    logger.info('Server closed');
    process.exit(0);
  });
});

process.on('SIGINT', async () => {
  logger.info('SIGINT received, shutting down gracefully');
  if (audioCapture) {
    await audioCapture.stopRecording();
  }
  server.close(() => {
    logger.info('Server closed');
    process.exit(0);
  });
});

// Helper function for audio stream (implement based on your audio source)
function getAudioStream() {
  // For testing without actual audio, return a mock readable stream
  // In production, replace with actual audio source (e.g., from WebRTC or file)
  const { Readable } = require('stream');
  const mockStream = new Readable({
    read() {
      // Mock empty stream for testing
      this.push(null);
    }
  });
  return mockStream;
}

// Start server
async function startServer() {
  try {
    await initializeServices();

    server.listen(config.app.port, () => {
      logger.info(`AI Call Companion server running on port ${config.app.port}`);
      logger.info(`Health check: http://localhost:${config.app.port}/health`);
    });
  } catch (error) {
    logger.error('Failed to start server:', error);
    process.exit(1);
  }
}

// Start the application
if (require.main === module) {
  startServer();
}

module.exports = { app, server, io, audioCapture, speechService };
