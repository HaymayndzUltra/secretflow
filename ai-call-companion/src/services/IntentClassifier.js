const natural = require('natural');
const compromise = require('compromise');

class IntentClassifier {
  constructor() {
    this.intentCategories = {
      BUDGET_DISCUSSION: {
        keywords: ['budget', 'cost', 'price', 'payment', 'rate', 'fee', 'expensive', 'afford', 'money'],
        patterns: [
          /how much (do you|will it) (cost|charge)/i,
          /what('s| is) your (rate|price|fee)/i,
          /can you work within (my )?budget/i,
          /what('s| is) the (pricing|cost)/i
        ]
      },
      TIMELINE_INQUIRY: {
        keywords: ['when', 'timeline', 'deadline', 'delivery', 'start', 'finish', 'how long', 'duration'],
        patterns: [
          /when (can you|will you) (start|begin|finish|deliver)/i,
          /what('s| is) the (timeline|deadline)/i,
          /how long (will it|does it) (take|require)/i,
          /by when (can you|will you) (complete|finish)/i
        ]
      },
      TECHNICAL_REQUIREMENTS: {
        keywords: ['technology', 'stack', 'framework', 'database', 'api', 'integration', 'technical', 'architecture'],
        patterns: [
          /what (technology|framework|stack) (do you|will you) use/i,
          /how (will you|do you) (integrate|connect|implement)/i,
          /what (database|api|backend) (do you|will you) use/i,
          /(can you|will you) use (react|vue|angular|node|python)/i
        ]
      },
      FEATURE_SPECIFICATION: {
        keywords: ['feature', 'functionality', 'capability', 'integration', 'include', 'provide', 'offer'],
        patterns: [
          /do you (provide|offer|include)/i,
          /will it (have|include|support)/i,
          /can it (handle|support|do)/i,
          /what (features|functionality) (do you|will you) provide/i
        ]
      },
      RISK_CONCERNS: {
        keywords: ['risk', 'issue', 'problem', 'challenge', 'concern', 'worry', 'difficult', 'complex'],
        patterns: [
          /are there any (risks|issues|problems|challenges)/i,
          /what (concerns|worries) (do you|should i) have/i,
          /is this (difficult|complex|challenging)/i,
          /what (could|might) go wrong/i
        ]
      }
    };

    this.classifier = new natural.BayesClassifier();
    this.initializeClassifier();
  }

  initializeClassifier() {
    // Train the classifier with sample phrases
    Object.entries(this.intentCategories).forEach(([intent, data]) => {
      data.keywords.forEach(keyword => {
        this.classifier.addDocument(keyword, intent);
      });

      data.patterns.forEach(pattern => {
        // Add pattern matches as training data
        this.classifier.addDocument(pattern.source, intent);
      });
    });

    this.classifier.train();
  }

  classifyIntent(transcript) {
    // Clean and normalize the transcript
    const normalizedText = this.normalizeText(transcript);

    // Use the trained classifier
    const classification = this.classifier.classify(normalizedText);

    // Calculate confidence based on match strength
    const confidence = this.calculateConfidence(normalizedText, classification);

    // If confidence is low, try pattern matching
    if (confidence < 0.6) {
      const patternMatch = this.patternMatchIntent(normalizedText);
      if (patternMatch) {
        return {
          intent: patternMatch.intent,
          confidence: patternMatch.confidence,
          method: 'pattern_matching'
        };
      }
    }

    return {
      intent: classification,
      confidence: confidence,
      method: 'bayes_classification'
    };
  }

  patternMatchIntent(text) {
    let bestMatch = null;
    let highestScore = 0;

    Object.entries(this.intentCategories).forEach(([intent, data]) => {
      data.patterns.forEach(pattern => {
        const matches = text.match(pattern);
        if (matches) {
          const score = matches[0].length / text.length; // Simple scoring based on match length
          if (score > highestScore && score > 0.3) {
            highestScore = score;
            bestMatch = { intent, confidence: Math.min(score * 2, 1.0) }; // Boost confidence for pattern matches
          }
        }
      });
    });

    return bestMatch;
  }

  normalizeText(text) {
    return text
      .toLowerCase()
      .replace(/[^\w\s]/g, ' ') // Remove punctuation
      .replace(/\s+/g, ' ') // Normalize whitespace
      .trim();
  }

  calculateConfidence(text, predictedIntent) {
    // Simple confidence calculation based on keyword matches
    const keywords = this.intentCategories[predictedIntent]?.keywords || [];
    let matchCount = 0;

    keywords.forEach(keyword => {
      if (text.includes(keyword)) {
        matchCount++;
      }
    });

    return Math.min(matchCount / keywords.length, 1.0);
  }

  // Advanced NLP analysis using compromise
  analyzeConversationContext(transcript) {
    const doc = compromise(transcript);

    return {
      topics: doc.topics().out('array'),
      people: doc.people().out('array'),
      places: doc.places().out('array'),
      organizations: doc.organizations().out('array'),
      questions: doc.questions().out('array'),
      statements: doc.statements().out('array'),
      positiveWords: doc.match('#Positive').out('array'),
      negativeWords: doc.match('#Negative').out('array')
    };
  }

  // Intent refinement based on conversation context
  refineIntentWithContext(initialIntent, context) {
    const { questions, positiveWords, negativeWords } = context;

    // Adjust intent based on context clues
    if (questions.length > 0 && initialIntent === 'TECHNICAL_REQUIREMENTS') {
      return 'TECHNICAL_QUESTION';
    }

    if (negativeWords.length > positiveWords.length && initialIntent === 'FEATURE_SPECIFICATION') {
      return 'RISK_CONCERNS';
    }

    return initialIntent;
  }

  // Extract key entities from transcript
  extractEntities(transcript) {
    const doc = compromise(transcript);

    return {
      technologies: this.extractTechnologies(doc),
      timeframes: this.extractTimeframes(doc),
      budgets: this.extractBudgets(doc),
      requirements: this.extractRequirements(doc)
    };
  }

  extractTechnologies(doc) {
    // Look for technology mentions
    const techTerms = ['react', 'vue', 'angular', 'node', 'python', 'django', 'laravel', 'spring', 'express', 'mongodb', 'postgresql', 'mysql', 'aws', 'azure', 'gcp', 'docker', 'kubernetes'];
    const foundTech = [];

    techTerms.forEach(tech => {
      if (doc.has(tech)) {
        foundTech.push(tech);
      }
    });

    return foundTech;
  }

  extractTimeframes(doc) {
    const timePatterns = [
      /(within|in) (\d+) (days?|weeks?|months?)/i,
      /(\d+) (days?|weeks?|months?) (from now|to complete)/i,
      /by (monday|tuesday|wednesday|thursday|friday|saturday|sunday)/i,
      /next (week|month)/i
    ];

    const timeframes = [];
    timePatterns.forEach(pattern => {
      const match = doc.match(pattern);
      if (match.out('array').length > 0) {
        timeframes.push(match.out('array')[0]);
      }
    });

    return timeframes;
  }

  extractBudgets(doc) {
    const budgetPatterns = [
      /(\$|USD|PHP|EUR)(\d+(?:,\d{3})*(?:\.\d{2})?)/i,
      /(\d+(?:,\d{3})*(?:\.\d{2})?) (dollars?|pesos?|euros?)/i,
      /budget (of|around|approximately) (\d+(?:,\d{3})*(?:\.\d{2})?)/i
    ];

    const budgets = [];
    budgetPatterns.forEach(pattern => {
      const match = doc.match(pattern);
      if (match.out('array').length > 0) {
        budgets.push(match.out('array')[0]);
      }
    });

    return budgets;
  }

  extractRequirements(doc) {
    // Extract feature requirements
    const requirements = [];

    // Look for requirement indicators
    const requirementIndicators = ['need', 'require', 'must have', 'should have', 'want', 'looking for'];
    requirementIndicators.forEach(indicator => {
      const matches = doc.match(`#${indicator}`).out('array');
      requirements.push(...matches);
    });

    return [...new Set(requirements)]; // Remove duplicates
  }

  // Get conversation insights
  getConversationInsights(transcript) {
    const context = this.analyzeConversationContext(transcript);
    const entities = this.extractEntities(transcript);
    const intent = this.classifyIntent(transcript);

    return {
      intent: intent.intent,
      confidence: intent.confidence,
      context,
      entities,
      summary: this.generateConversationSummary(transcript, intent, entities)
    };
  }

  generateConversationSummary(transcript, intent, entities) {
    return {
      mainTopic: intent.intent.replace(/_/g, ' ').toLowerCase(),
      keyTechnologies: entities.technologies,
      mentionedTimeframes: entities.timeframes,
      budgetDiscussions: entities.budgets,
      requirements: entities.requirements,
      overallTone: this.determineOverallTone(transcript)
    };
  }

  determineOverallTone(transcript) {
    const positiveWords = ['great', 'excellent', 'perfect', 'amazing', 'love', 'excited', 'happy'];
    const negativeWords = ['problem', 'issue', 'concern', 'difficult', 'challenging', 'worried'];

    const lowerTranscript = transcript.toLowerCase();
    const positiveCount = positiveWords.filter(word => lowerTranscript.includes(word)).length;
    const negativeCount = negativeWords.filter(word => lowerTranscript.includes(word)).length;

    if (positiveCount > negativeCount) return 'POSITIVE';
    if (negativeCount > positiveCount) return 'NEGATIVE';
    return 'NEUTRAL';
  }
}

module.exports = IntentClassifier;
