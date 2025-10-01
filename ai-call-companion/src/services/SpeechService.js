const speech = require('@google-cloud/speech');
const fs = require('fs');
const path = require('path');

class SpeechService {
  constructor(config) {
    this.config = config;
    this.speechClient = new speech.SpeechClient({
      keyFilename: config.google.credentialsPath,
      projectId: config.google.projectId
    });
  }

  async transcribeAudio(filePath, options = {}) {
    try {
      const audioBytes = fs.readFileSync(filePath).toString('base64');

      const audio = {
        content: audioBytes,
      };

      const config = {
        encoding: options.encoding || 'LINEAR16',
        sampleRateHertz: options.sampleRate || this.config.audio.sampleRate,
        languageCode: options.languageCode || 'en-US',
        alternativeLanguageCodes: options.alternativeLanguages || ['fil-PH'],
        enableAutomaticPunctuation: true,
        enableWordTimeOffsets: true,
        enableSpeakerDiarization: options.enableSpeakerDiarization !== false,
        diarizationSpeakerCount: options.speakerCount || 2,
        minSpeakerCount: 1,
        maxSpeakerCount: 4,
        model: options.model || 'video',
        useEnhanced: true,
        adaptationBias: options.adaptationBias || this.getAdaptationBias()
      };

      const request = {
        audio: audio,
        config: config,
      };

      const [response] = await this.speechClient.recognize(request);

      return this.processTranscriptionResponse(response);
    } catch (error) {
      console.error('Speech recognition error:', error);
      throw error;
    }
  }

  async transcribeStreaming(audioStream, options = {}) {
    const config = {
      encoding: options.encoding || 'LINEAR16',
      sampleRateHertz: options.sampleRate || this.config.audio.sampleRate,
      languageCode: options.languageCode || 'en-US',
      alternativeLanguageCodes: options.alternativeLanguages || ['fil-PH'],
      enableAutomaticPunctuation: true,
      enableWordTimeOffsets: true,
      enableSpeakerDiarization: options.enableSpeakerDiarization !== false,
      diarizationSpeakerCount: options.speakerCount || 2,
      minSpeakerCount: 1,
      maxSpeakerCount: 4,
      model: options.model || 'video',
      useEnhanced: true,
      adaptationBias: options.adaptationBias || this.getAdaptationBias()
    };

    const request = {
      config,
      interimResults: true,
      singleUtterance: false
    };

    const recognizeStream = this.speechClient
      .streamingRecognize(request)
      .on('error', (error) => {
        console.error('Streaming recognition error:', error);
      })
      .on('data', (data) => {
        if (data.results[0] && data.results[0].alternatives[0]) {
          const transcript = data.results[0].alternatives[0].transcript;
          const isFinal = !data.results[0].isFinal;

          // Emit real-time transcription
          this.emit('transcription', {
            transcript,
            isFinal,
            confidence: data.results[0].alternatives[0].confidence,
            speaker: this.getSpeakerFromDiarization(data.results[0])
          });
        }
      });

    // Pipe audio stream to recognizeStream
    audioStream.pipe(recognizeStream);

    return recognizeStream;
  }

  processTranscriptionResponse(response) {
    const results = response.results || [];

    return results.map(result => ({
      transcript: result.alternatives[0].transcript,
      confidence: result.alternatives[0].confidence,
      words: result.alternatives[0].words || [],
      speakerTags: result.speakerTags || [],
      languageCode: result.languageCode
    }));
  }

  getSpeakerFromDiarization(result) {
    if (result.speakerTags && result.speakerTags.length > 0) {
      return result.speakerTags[0].speakerTag;
    }
    return null;
  }

  getAdaptationBias() {
    // Custom vocabulary for freelancer/client conversations
    return {
      phrases: [
        'budget',
        'timeline',
        'deadline',
        'requirements',
        'technical specifications',
        'project scope',
        'deliverables',
        'payment terms',
        'contract',
        'milestone',
        'feedback',
        'revision',
        'deployment',
        'testing',
        'integration',
        'API',
        'database',
        'framework',
        'authentication',
        'security',
        'performance',
        'responsive design',
        'mobile compatibility'
      ]
    };
  }

  // Event emitter for real-time updates
  on(event, callback) {
    this.events = this.events || {};
    this.events[event] = this.events[event] || [];
    this.events[event].push(callback);
  }

  emit(event, data) {
    if (this.events && this.events[event]) {
      this.events[event].forEach(callback => callback(data));
    }
  }

  async getSupportedLanguages() {
    try {
      const [response] = await this.speechClient.getSupportedLanguages();
      return response.languages || [];
    } catch (error) {
      console.error('Error getting supported languages:', error);
      return [];
    }
  }

  async validateAudioFile(filePath) {
    try {
      const stats = fs.statSync(filePath);
      const fileSizeMB = stats.size / (1024 * 1024);

      if (fileSizeMB > 100) {
        throw new Error('Audio file too large (max 100MB)');
      }

      // Basic format validation
      const extension = path.extname(filePath).toLowerCase();
      const supportedFormats = ['.wav', '.flac', '.mp3', '.ogg', '.webm'];

      if (!supportedFormats.includes(extension)) {
        throw new Error(`Unsupported audio format: ${extension}`);
      }

      return true;
    } catch (error) {
      console.error('Audio validation error:', error);
      throw error;
    }
  }
}

module.exports = SpeechService;
