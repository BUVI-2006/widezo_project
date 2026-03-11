# Tamil Speech Recognition Model Evaluation

This project evaluates multiple Tamil Automatic Speech Recognition (ASR) models from Hugging Face using a custom Tamil speech dataset. The goal is to compare models based on transcription accuracy, inference speed, and GPU resource usage.

---

# Project Objective

The objective of this project is to benchmark Tamil speech recognition models and analyze their performance using standard ASR evaluation metrics such as:

- Word Error Rate (WER)
- Character Error Rate (CER)
- Latency
- Real Time Factor (RTF)
- Hallucination Rate
- GPU Memory Usage

These metrics help determine which model provides the best balance between accuracy and speed.

---

# Models Evaluated

The following Tamil ASR models were tested:

- vasista22/whisper-tamil-small
- vasista22/whisper-tamil-medium
- vasista22/whisper-tamil-large-v2
- Additional Tamil Whisper-based models from Hugging Face

These models are fine-tuned versions of OpenAI's Whisper architecture for Tamil speech recognition.

---

# Dataset

The dataset contains Tamil audio recordings along with their corresponding text transcripts.

Dataset structure:

```
dataset/
 ├── audio/
 │   ├── 1.wav
 │   ├── 2.wav
 │   ├── ...
 │
 └── transcripts.tsv
```

Each audio file corresponds to a transcript entry using an index.

Example transcript file:

```
index    sentence
1        Tamil sentence
2        Tamil sentence
```

For evaluation, the first **100 audio samples** were used to compute metrics.

---

# Evaluation Metrics

## Word Error Rate (WER)

WER measures the percentage of incorrectly predicted words.

Formula:

WER = (Substitutions + Deletions + Insertions) / Total Words

Lower WER indicates better transcription accuracy.

---

## Character Error Rate (CER)

CER is similar to WER but calculated at the character level instead of words.

This is useful for languages like Tamil where word boundaries may vary.

Lower CER indicates better performance.

---

## Latency

Latency measures the time taken by the model to transcribe an audio file.

Lower latency means faster transcription.

---

## Real Time Factor (RTF)

RTF measures how fast the model processes audio compared to the audio duration.

RTF = Processing Time / Audio Duration

Example:

RTF < 1 → Faster than real-time  
RTF = 1 → Real-time processing  
RTF > 1 → Slower than real-time

Lower RTF is better for real-time systems.

---

## Hallucination Rate

Hallucination occurs when the model generates extra words that are not present in the audio.

Hallucination Rate = Insertions / Reference Words

Lower hallucination rate means the model produces fewer incorrect words.

---

## GPU Memory Usage

GPU memory metrics help analyze the computational requirements of each model.

Measured metrics include:

- Peak GPU Memory Usage
- Allocated GPU Memory
- Reserved GPU Memory

These values help determine whether the model can run efficiently on available hardware.

---

Pipeline:

```
Audio → Feature Extraction → Neural Network → Text Prediction
```

---



# Evaluation Pipeline

The evaluation process consists of the following steps:

1. Load audio files
2. Convert audio to 16 kHz
3. Extract audio features using the Whisper processor
4. Run model inference
5. Decode predicted tokens into text
6. Compute evaluation metrics

---

# Results

The models were evaluated using:

- WER
- CER
- Latency
- RTF
- Hallucination Rate
- GPU Memory Usage

Results were exported to a spreadsheet for comparison across models.

---

# Conclusion

This project provides a benchmark comparison of Tamil speech recognition models in terms of accuracy, speed, and computational efficiency.

Such evaluations are useful for selecting the best model for real-time Tamil speech recognition systems.

---
