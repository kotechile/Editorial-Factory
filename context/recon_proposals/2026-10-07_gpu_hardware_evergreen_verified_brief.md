# Verified Brief: gpu_hardware — 2026-10-07 (evergreen)

Companion to `context/recon_proposals/2026-10-07_gpu_hardware_evergreen_brief.md`
(`<!-- evergreen-gate -->` marker: PASS, 5 rows / 5 hosts). Every claim below was fetched live on
2026-10-07 with the pipeline's own fetcher (`scripts/citation_hub_dossier.fetch_source`); the
Verbatim cell is the primary source's own wording, not a paraphrase.

Decision in play: whether to add a GPU to serve more concurrent sessions, or fix the serving stack
first — and how to compute the per-session key-value cache footprint.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Cache waste | Existing serving systems use only 20.4%–38.2% of the memory they reserve for the key-value cache | VERIFIED | https://arxiv.org/html/2309.06180v1 | "our profiling results in Fig. 2 show that only 20.4% - 38.2% of the KV cache memory is used to store the actual token states in the existing systems" |
| 2 | Cache waste | Pre-paging systems waste 60%–80% of memory on fragmentation and over-reservation | VERIFIED | https://blog.vllm.ai/2023/06/20/vllm.html | "We find that existing systems waste 60% – 80% of memory due to fragmentation and over-reservation." |
| 3 | Paging | Block-paged cache cuts memory waste to under 4% | VERIFIED | https://blog.vllm.ai/2023/06/20/vllm.html | "In PagedAttention, memory waste only happens in the last block of a sequence. In practice, this results in near-optimal memory usage, with a mere waste of under 4%." |
| 4 | Paging | PagedAttention's per-token block addressing is the mechanism: cache blocks do not need to be contiguous and are fetched as needed | VERIFIED | https://arxiv.org/html/2309.06180v1 | "PagedAttention divides the request's KV cache into blocks, each of which can contain the attention keys and values of a fixed number of tokens. In PagedAttention, the blocks for the KV cache are not necessarily stored in contiguous space." |
| 5 | Throughput | vLLM improves throughput 2–4× over FasterTransformer and Orca at the same latency | VERIFIED | https://arxiv.org/html/2309.06180v1 | "vLLM improves the throughput of popular LLMs by 2-4 × with the same level of latency compared to the state-of-the-art systems, such as FasterTransformer and Orca" |
| 6 | Throughput | The vLLM launch post measured up to 24× higher throughput than HuggingFace Transformers and up to 1.7GB of cache for a single LLaMA-13B sequence | VERIFIED | https://blog.vllm.ai/2023/06/20/vllm.html | "it delivers up to 24x higher throughput than HuggingFace Transformers, without requiring any model architecture changes" / "The KV cache is Large: Takes up to 1.7GB for a single sequence in LLaMA-13B." |
| 7 | Weights | A 7-billion-parameter model at 16-bit precision takes roughly 14 GB for weights alone, before any cache | VERIFIED | https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ | "a model with 7 billion parameters (such as Llama 2 7B ), loaded in 16-bit precision (FP16 or BF16) would take roughly 7B * sizeof(FP16) ~= 14 GB in memory" |
| 8 | Sizing rule | Cache size per token = 2 × layers × (heads × head size) × bytes per number; total = batch × sequence × 2 × layers × hidden size × 2 bytes at 16-bit | VERIFIED | https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ | "Size of KV cache per token in bytes = 2 * (num_layers) * (num_heads * dim_head) * precision_in_bytes" / "Total size of KV cache in bytes = (batch_size) * (sequence_length) * 2 * (num_layers) * (hidden_size) * sizeof(FP16)" |
| 9 | Sizing rule | Worked example: Llama 2 7B at 16-bit, 4,096-token context, batch of 1 → about 2 GB of cache | VERIFIED | https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ | "with a Llama 2 7B model in 16-bit precision and a batch size of 1, the size of the KV cache will be 1 * 4096 * 2 * 32 * 4096 * 2 bytes, which is ~2 GB." |
| 10 | Sizing rule | Cache footprint grows linearly with batch size and sequence length, which is what limits long-context throughput | VERIFIED | https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ | "Key-value caching avoids recomputing attention tensors during decoding, but its memory footprint grows linearly with batch size and sequence length, limiting throughput for long-context workloads such as retrieval-augmented generation." |
| 11 | Why memory | Decode is memory-bound; prefill (which processes input tokens in parallel) is the compute-heavy phase | VERIFIED | https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ | "a prefill phase that processes input tokens in parallel and a decode phase that generates output tokens autoregressively and is memory-bound" |
| 12 | Bandwidth | 7B at 16-bit with 14 ms per output token moves 14 GB in 14 ms = 1 TB/sec against a 2 TB/sec card — half the memory speed, i.e. 50% bandwidth use | VERIFIED | https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices | "if a 7B parameter running with 16-bit precision has TPOT equal to 14ms, then it's moving 14GB of parameters in 14ms translating to 1TB/sec bandwidth usage. If the peak bandwidth of the machine is 2TB/sec, we are running at an MBU of 50%." |
| 13 | Bandwidth | Memory bandwidth, not math rate, is the main bottleneck for inference speed; near-100% bandwidth use is the goal | VERIFIED | https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices | "Why is memory bandwidth the main bottleneck for LLM inference speed?" / "MBU values close to 100% imply that the inference system is effectively utilizing the available memory bandwidth." |
| 14 | Batching trade-off | A bigger batch raises throughput but a larger cache — and more GPUs — while slowing each user's token stream | VERIFIED | https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices | "if we process 16 user queries concurrently, we'll have higher throughput compared to running the queries sequentially, but we'll take longer to generate output tokens for each user" / "a large batch means larger KV cache size, and that in turn increases the number of GPUs required to serve the model" |
| 15 | Scheduling | Continuous (iteration-level) batching measured 23× more throughput than request-level batching while cutting median latency | VERIFIED | https://www.anyscale.com/blog/continuous-batching-llm-inference | "How continuous batching enables 23x throughput in LLM inference while reducing p50 latency" / "Dynamic batching is fitting but can be confused with request-level batching, where an LLM inference server uses a static batch whose size is chosen when the current batch has completely finished generation." |
| 16 | Quantization | "An FP8 key-value cache halves cache memory" | REMOVED | https://docs.vllm.ai/en/latest/features/quantization/fp8.html | no retrievable content — the doc page returned 61 characters (no body), so the figure cannot be confirmed. Dropped, not reworded; run it only from a source that states the figure on a fetchable page. |

## Gate rules applied
- 15 of 16 claims VERIFIED; **1 REMOVED** (below the ≥ 2-removed under-sourced threshold).
- All five cited URLs are primary/origin pages (the paper, the project's launch post, the vendor
  engineering blog, the vendor engineering blog, the framework author's own post).
- The 2–4× / 24× / 23× multipliers are each tied to a named baseline in the source; the article must
  carry the baseline, never a naked multiplier.
- The 14 GB, 2 GB, 1 TB/sec, 50% and 1.7GB figures are **as of** the cited publications
  (2023–2024). The article states that, so a reader re-checking in 12 months knows what they are
  reading.
- Rejected as article material: the `customer-truth.md` field anecdote ($28,000 → $9,500/month
  after moving to vLLM with paged attention). It is our own field note, not a fetchable measurement,
  so it stays out of the body rather than shipping as an unsourced number.
