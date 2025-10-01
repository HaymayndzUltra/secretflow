#!/usr/bin/env python3
"""Synthetic latency benchmark harness."""
import json
import random
import time
from dataclasses import dataclass


@dataclass
class LatencySample:
    stage: str
    latency_ms: float


def simulate_stage(name: str, budget: float) -> LatencySample:
    latency = random.uniform(budget * 0.3, budget * 0.9)
    time.sleep(0.01)
    return LatencySample(stage=name, latency_ms=latency)


def run_benchmark() -> dict:
    stages = [
        ("asr_partials", 200),
        ("retrieval", 120),
        ("llm_ttfb", 180),
        ("overlay_render", 80)
    ]
    samples = [simulate_stage(name, budget) for name, budget in stages]
    metrics = {sample.stage: sample.latency_ms for sample in samples}
    metrics["p50"] = sum(s.latency_ms for s in samples) / len(samples)
    metrics["p95"] = max(s.latency_ms for s in samples)
    metrics["p99"] = metrics["p95"]
    return metrics


if __name__ == "__main__":
    results = run_benchmark()
    print(json.dumps(results, indent=2))
