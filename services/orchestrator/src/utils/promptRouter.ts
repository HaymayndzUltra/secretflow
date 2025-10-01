import { Evidence } from '../clients/retrievalClient';

export type Intent = 'requirements' | 'architecture' | 'integration' | 'risk' | 'generic';

export function detectIntent(text: string): Intent {
  const lowered = text.toLowerCase();
  if (lowered.includes('require') || lowered.includes('needs')) {
    return 'requirements';
  }
  if (lowered.includes('architecture') || lowered.includes('design')) {
    return 'architecture';
  }
  if (lowered.includes('integrat')) {
    return 'integration';
  }
  if (lowered.includes('risk') || lowered.includes('issue')) {
    return 'risk';
  }
  return 'generic';
}

const templates: Record<Intent, string> = {
  requirements: 'Summarize caller requirements with evidence references.',
  architecture: 'Outline technical architecture guidance grounded in evidence.',
  integration: 'Explain integration pathways referencing evidence.',
  risk: 'List key risks and mitigations with citations.',
  generic: 'Assist with the conversation using retrieved evidence.'
};

export function buildPrompt(intent: Intent, evidence: Evidence[], transcript: string): string {
  const header = templates[intent];
  const citations = evidence
    .map(ev => `- [${ev.id}] ${ev.text.slice(0, 200)} (span ${ev.span.join('-')})`)
    .join('\n');
  const degrade = evidence.length === 0 ? '\nNo evidence available. Ask clarifying questions.' : '';
  return `${header}\nIntent: ${intent}\nTranscript:\n${transcript}\nEvidence:\n${citations}${degrade}`;
}
