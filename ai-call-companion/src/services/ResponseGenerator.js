const OpenAI = require('openai');

class ResponseGenerator {
  constructor(config) {
    this.config = config;
    this.openai = new OpenAI({
      apiKey: config.openai.apiKey
    });

    this.responseTemplates = {
      BUDGET_DISCUSSION: [
        "Based on similar projects, the typical budget range for this scope is ${minBudget}-${maxBudget}.",
        "I can work within your budget constraints. Let's discuss how we can optimize the scope to fit your needs.",
        "My standard rate for similar projects is ${hourlyRate}/hour. For this specific scope, I'd estimate ${totalEstimate}.",
        "I understand budget is important. Here's how I can deliver value within your budget range..."
      ],
      TIMELINE_INQUIRY: [
        "For a project of this scope, I typically deliver in ${weeks} weeks, including ${milestones} milestones.",
        "I can start immediately and deliver the MVP in ${mvpWeeks} weeks, with full completion in ${totalWeeks} weeks.",
        "Based on similar projects, this would take approximately ${totalTime}. I can adjust based on your urgency.",
        "Let's break this down: Phase 1 (${phase1Time}), Phase 2 (${phase2Time}), with testing in Phase 3."
      ],
      TECHNICAL_REQUIREMENTS: [
        "For this project, I recommend ${recommendedTech} based on ${reason}. I've used it successfully in ${similarProjects} similar projects.",
        "The tech stack I'll use includes ${frontend}, ${backend}, and ${database}. This combination provides ${benefits}.",
        "I have extensive experience with ${primaryTech}. For your specific needs, I can implement ${specificFeatures}.",
        "Let me explain my technical approach: ${explanation}. This ensures ${benefits}."
      ],
      FEATURE_SPECIFICATION: [
        "This solution includes ${coreFeatures}. I can also add ${additionalFeatures} if needed.",
        "The key features will be ${feature1}, ${feature2}, and ${feature3}. Each designed to ${benefits}.",
        "Based on your requirements, I'll implement ${features}. Here's why each is important: ${explanations}.",
        "I can build this with ${technologies} to ensure ${performanceGoals}."
      ],
      RISK_CONCERNS: [
        "I understand your concerns. Based on similar projects, the main risks are ${risks}, but I mitigate them through ${mitigations}.",
        "That's a valid concern. Here's how I handle ${concern}: ${solution}. I've done this successfully in ${examples}.",
        "Let me address that: ${explanation}. This approach has worked well in ${similarCases}.",
        "I appreciate you bringing that up. The solution includes ${safeguards} to prevent ${potentialIssues}."
      ]
    };

    this.personalizationData = {
      experience: "5+ years as a full-stack developer",
      specializations: "React, Node.js, Python, AI integration",
      portfolio: "50+ successful projects on Upwork",
      communication: "Regular updates, transparent process",
      guarantees: "Satisfaction guarantee, post-delivery support"
    };
  }

  async generateResponse(intent, context, clientProfile = {}) {
    try {
      // Get base template for intent
      const templates = this.responseTemplates[intent] || this.responseTemplates.BUDGET_DISCUSSION;

      // Select best template based on context
      const selectedTemplate = await this.selectBestTemplate(templates, context);

      // Personalize the response
      const personalizedResponse = await this.personalizeResponse(selectedTemplate, context, clientProfile);

      // Enhance with AI if needed
      const enhancedResponse = await this.enhanceWithAI(personalizedResponse, context);

      return {
        response: enhancedResponse,
        confidence: this.calculateResponseConfidence(enhancedResponse, context),
        metadata: {
          intent,
          template: selectedTemplate,
          personalized: true,
          aiEnhanced: true
        }
      };
    } catch (error) {
      console.error('Response generation error:', error);
      return this.getFallbackResponse(intent, context);
    }
  }

  async selectBestTemplate(templates, context) {
    // Simple template selection based on context keywords
    let bestTemplate = templates[0];
    let highestScore = 0;

    templates.forEach(template => {
      let score = 0;

      // Score based on context relevance
      if (context.includes('budget') && template.includes('budget')) score += 2;
      if (context.includes('time') && template.includes('week')) score += 2;
      if (context.includes('technical') && template.includes('tech')) score += 2;

      if (score > highestScore) {
        highestScore = score;
        bestTemplate = template;
      }
    });

    return bestTemplate;
  }

  async personalizeResponse(template, context, clientProfile) {
    let response = template;

    // Replace placeholders with actual data
    response = response.replace('${minBudget}', '2,000');
    response = response.replace('${maxBudget}', '5,000');
    response = response.replace('${hourlyRate}', '75');
    response = response.replace('${totalEstimate}', '3,500');
    response = response.replace('${weeks}', '2-3');
    response = response.replace('${milestones}', '3');
    response = response.replace('${mvpWeeks}', '1');
    response = response.replace('${totalWeeks}', '3');
    response = response.replace('${phase1Time}', '1 week');
    response = response.replace('${phase2Time}', '1-2 weeks');

    // Add personalization based on client profile
    if (clientProfile.industry) {
      response += ` Given your ${clientProfile.industry} background, I can tailor this to your specific needs.`;
    }

    // Add experience highlights
    response += ` ${this.personalizationData.experience} with ${this.personalizationData.specializations}.`;

    return response;
  }

  async enhanceWithAI(baseResponse, context) {
    try {
      const prompt = `
You are an experienced Upwork freelancer having a client call. The client has asked about: "${context}"

Here's my planned response: "${baseResponse}"

Please enhance this response to be:
- More professional and confident
- Specific to the client's context
- Include relevant examples from your experience
- End with a question to continue the conversation

Enhanced response:`;

      const completion = await this.openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [
          {
            role: "system",
            content: "You are an expert Upwork freelancer who communicates professionally and builds trust with clients."
          },
          {
            role: "user",
            content: prompt
          }
        ],
        max_tokens: 200,
        temperature: 0.7
      });

      return completion.choices[0].message.content.trim();
    } catch (error) {
      console.error('AI enhancement error:', error);
      return baseResponse; // Fallback to base response
    }
  }

  calculateResponseConfidence(response, context) {
    // Simple confidence calculation
    let confidence = 0.8; // Base confidence

    // Boost confidence if response is well-structured
    if (response.length > 50 && response.length < 300) confidence += 0.1;
    if (response.includes('?')) confidence += 0.05; // Includes question
    if (response.includes('experience') || response.includes('similar')) confidence += 0.05;

    return Math.min(confidence, 1.0);
  }

  getFallbackResponse(intent, context) {
    const fallbacks = {
      BUDGET_DISCUSSION: "I understand budget is important. Based on similar projects, I can work within a reasonable range. What's your budget for this project?",
      TIMELINE_INQUIRY: "For projects like this, I typically deliver in 2-3 weeks. What's your preferred timeline?",
      TECHNICAL_REQUIREMENTS: "I use modern, reliable technologies. What specific tech stack are you looking for?",
      FEATURE_SPECIFICATION: "I'll include the core features you mentioned. What additional functionality would you like?",
      RISK_CONCERNS: "I understand your concerns. I mitigate risks through thorough planning and testing. What specific concerns do you have?"
    };

    return {
      response: fallbacks[intent] || "That's a great question. Let me address that for you.",
      confidence: 0.6,
      metadata: {
        intent,
        fallback: true
      }
    };
  }

  // Generate multiple response options
  async generateResponseOptions(intent, context, clientProfile = {}) {
    const primaryResponse = await this.generateResponse(intent, context, clientProfile);

    // Generate alternative responses
    const alternatives = [];

    // Shorter version
    alternatives.push({
      response: primaryResponse.response.substring(0, Math.floor(primaryResponse.response.length * 0.7)) + "...",
      style: "concise",
      confidence: primaryResponse.confidence * 0.9
    });

    // More detailed version
    alternatives.push({
      response: primaryResponse.response + " I have extensive experience with similar projects and can provide references if needed.",
      style: "detailed",
      confidence: primaryResponse.confidence * 0.95
    });

    return [primaryResponse, ...alternatives];
  }

  // Context-aware response adaptation
  adaptResponseForClient(response, clientProfile) {
    let adaptedResponse = response;

    // Adapt based on client industry
    if (clientProfile.industry === 'healthcare') {
      adaptedResponse = adaptedResponse.replace(/project/g, 'healthcare solution');
      adaptedResponse += " I understand healthcare regulations and compliance requirements.";
    }

    if (clientProfile.industry === 'finance') {
      adaptedResponse = adaptedResponse.replace(/project/g, 'financial application');
      adaptedResponse += " Security and compliance are top priorities for financial systems.";
    }

    // Adapt based on client size
    if (clientProfile.size === 'enterprise') {
      adaptedResponse += " I have experience scaling solutions for enterprise environments.";
    }

    if (clientProfile.size === 'startup') {
      adaptedResponse += " I can help you get to market quickly while ensuring scalability.";
    }

    return adaptedResponse;
  }

  // Conversation flow suggestions
  suggestNextQuestions(intent, currentResponse) {
    const followUpQuestions = {
      BUDGET_DISCUSSION: [
        "What's your budget range for this project?",
        "Are there any budget constraints I should be aware of?",
        "How does this fit into your overall budget for the quarter?"
      ],
      TIMELINE_INQUIRY: [
        "What's your preferred delivery timeline?",
        "Are there any hard deadlines I need to work around?",
        "Would you prefer a phased delivery approach?"
      ],
      TECHNICAL_REQUIREMENTS: [
        "Do you have any preferred technologies or frameworks?",
        "Are there existing systems I need to integrate with?",
        "What are your performance and security requirements?"
      ],
      FEATURE_SPECIFICATION: [
        "What are your must-have features versus nice-to-have?",
        "Are there any specific integrations you need?",
        "How do you envision users interacting with this feature?"
      ],
      RISK_CONCERNS: [
        "What specific concerns do you have about this approach?",
        "Have you encountered similar issues in past projects?",
        "What would make you feel more confident about proceeding?"
      ]
    };

    return followUpQuestions[intent] || ["What other questions do you have?"];
  }

  // Response quality assessment
  assessResponseQuality(response, intent, context) {
    const metrics = {
      relevance: this.assessRelevance(response, intent),
      clarity: this.assessClarity(response),
      professionalism: this.assessProfessionalism(response),
      completeness: this.assessCompleteness(response, context)
    };

    const overallScore = Object.values(metrics).reduce((sum, score) => sum + score, 0) / Object.keys(metrics).length;

    return {
      score: overallScore,
      metrics,
      suggestions: this.generateQualitySuggestions(metrics)
    };
  }

  assessRelevance(response, intent) {
    const intentKeywords = this.responseTemplates[intent]?.[0]?.split(' ') || [];
    const responseWords = response.toLowerCase().split(' ');

    const relevantWords = responseWords.filter(word =>
      intentKeywords.some(keyword => word.includes(keyword.toLowerCase()))
    );

    return Math.min(relevantWords.length / intentKeywords.length, 1.0);
  }

  assessClarity(response) {
    // Simple clarity metrics
    const sentences = response.split(/[.!?]+/).length;
    const avgWordsPerSentence = response.split(' ').length / sentences;

    // Optimal: 10-20 words per sentence
    if (avgWordsPerSentence >= 10 && avgWordsPerSentence <= 20) return 1.0;
    if (avgWordsPerSentence < 10) return 0.8;
    return 0.6;
  }

  assessProfessionalism(response) {
    const professionalIndicators = ['experience', 'similar', 'recommend', 'ensure', 'quality'];
    const casualIndicators = ['kinda', 'sorta', 'maybe', 'guess'];

    const professionalCount = professionalIndicators.filter(indicator =>
      response.toLowerCase().includes(indicator)
    ).length;

    const casualCount = casualIndicators.filter(indicator =>
      response.toLowerCase().includes(indicator)
    ).length;

    return professionalCount > casualCount ? 1.0 : 0.7;
  }

  assessCompleteness(response, context) {
    // Check if response addresses key elements from context
    const keyElements = context.toLowerCase().split(' ');
    const responseElements = response.toLowerCase().split(' ');

    const coveredElements = keyElements.filter(element =>
      responseElements.some(responseElement =>
        responseElement.includes(element) || element.includes(responseElement)
      )
    );

    return Math.min(coveredElements.length / keyElements.length, 1.0);
  }

  generateQualitySuggestions(metrics) {
    const suggestions = [];

    if (metrics.relevance < 0.8) {
      suggestions.push("Make response more relevant to the specific intent");
    }

    if (metrics.clarity < 0.8) {
      suggestions.push("Simplify sentence structure for better clarity");
    }

    if (metrics.professionalism < 0.8) {
      suggestions.push("Use more professional language and tone");
    }

    if (metrics.completeness < 0.8) {
      suggestions.push("Ensure all key points from client question are addressed");
    }

    return suggestions;
  }
}

module.exports = ResponseGenerator;
