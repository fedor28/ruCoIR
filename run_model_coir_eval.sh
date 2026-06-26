CUDA_VISIBLE_DEVICES=3 \
python sentence_transformermers_run_eval.py \
    --model_name Qwen/Qwen3-Embedding-8B \
    --tasks apps codefeedback-st  stackoverflow-qa cosqa codesearchnet --batch_size 8