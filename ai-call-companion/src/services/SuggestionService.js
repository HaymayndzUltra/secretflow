const OpenAI = require('openai');

class SuggestionService {
  constructor(config) {
    this.config = config;
    if (config.openai && config.openai.key) {
      this.openai = new OpenAI({ apiKey: config.openai.key });
    } else {
      console.warn('OpenAI API key not provided; suggestions will be disabled');
      this.openai = null;
    }
  }

  async generateSuggestion(transcript, context = {}) {
    if (!this.openai) {
      return 'Suggestions disabled: No OpenAI key configured.';
    }

    try {
      const prompt = `You are an AI assistant helping a freelancer during a client discovery call on Upwork. Based on this client transcript: "${transcript}". Context: ${JSON.stringify(context)}. Suggest a concise, professional response or follow-up question. Focus on key Upwork topics like budget, timeline, requirements, or deliverables. Keep it under 100 characters if possible.`;

      const response = await this.openai.chat.completions.create({
        model: 'gpt-3.5-turbo',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 150,
        temperature: 0.7,
      });

      return response.choices[0].message.content.trim();
    } catch (error) {
      console.error('Error generating suggestion:', error);
      throw error;
    }
  }

  // Event emitter for real-time updates (similar to SpeechService)
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
}

module.exports = SuggestionService;
