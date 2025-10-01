const EMAIL_REGEX = /[\w.+-]+@[\w-]+\.[\w.-]+/g;
const PHONE_REGEX = /\+?\d[\d\s().-]{7,}\d/g;
const NAME_REGEX = /\b([A-Z][a-z]+\s[A-Z][a-z]+)\b/g;

export function redactPII(text: string): string {
  return text
    .replace(EMAIL_REGEX, '[REDACTED_EMAIL]')
    .replace(PHONE_REGEX, '[REDACTED_PHONE]')
    .replace(NAME_REGEX, '[REDACTED_NAME]');
}
