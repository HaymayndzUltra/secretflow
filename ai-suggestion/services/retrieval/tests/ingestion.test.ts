import { describe, expect, it } from 'vitest';
import fs from 'fs';
import path from 'path';
import { ingestDirectory } from '../src/services/ingestionService';

const fixtureDir = path.join(__dirname, 'fixtures');
fs.mkdirSync(fixtureDir, { recursive: true });
fs.writeFileSync(path.join(fixtureDir, 'doc.txt'), 'hello world '.repeat(20));

describe('ingestion service', () => {
  it('processes fixture directory', async () => {
    const result = await ingestDirectory(fixtureDir);
    expect(result.processed).toBeGreaterThan(0);
  });
});
