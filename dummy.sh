set -x
# 激活 Conda 环境
echo "🔄 正在切换到 Conda 环境 pjh_verl..."
eval "$(conda shell.bash hook)"
conda activate pjh_verl

# 检查 conda 环境是否激活成功
if [[ "$CONDA_DEFAULT_ENV" == "pjh_verl" ]]; then
  echo "✅ Conda 环境 pjh_verl 已成功激活！"
else
  echo "❌ Conda 环境激活失败！当前环境为：$CONDA_DEFAULT_ENV"
  exit 1
fi

CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve Qwen/Qwen3-8B --dtype bfloat16 --gpu-memory-utilization 0.9 --tensor-parallel-size 8 --port 8001
